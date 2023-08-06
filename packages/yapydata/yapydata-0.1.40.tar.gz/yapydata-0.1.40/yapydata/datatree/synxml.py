# -*- coding: utf-8 -*-
"""The *YapyData.xml* module provides *XML*.
"""

import os
import re


# Python 2: from xml.etree import cElementTree as ElementTree. 
# Python 3: from xml.etree import ElementTree (the accelerated C version is used automatically).
try:
    # Python 2: 
    import  xml.etree.cElementTree as ET  # @UnusedImport
except:
    # Python 3: -  cElementTree used automatically
    import  xml.etree.ElementTree as ET  # @Reimport

from yapydata.datatree import YapyDataTreeError
from yapydata.datatree.datatree import DataTree


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


#: fixed common keyword for special values - supported case sensitive and literally only
KEYWORDS = {'true':True, 'false': False, 'null':None,}


#: due to XML-1.0/1.1 - leading and trailing white spaces of the content are dropped
#: embedded are kept
_COMPCONT = re.compile(r'^\s*|\s*$')


class YapyDataXMLError(YapyDataTreeError):
    """Common XML syntax error. 
    """
    pass


#             "Abdera_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "Apache_Camel_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "Badgerfish_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "GData_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "Gnome_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "JsonML_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "NewtonSoft_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "oData_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "Parker_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },
#             "Spark_Convention": {
#                 "call": DataTreeXML.readout_data,
#             },


def readout_data(xval, **kargs):
    """Scan tree into JSON representation. Uses recursive calls to 
    readout_data through  the logical tree spanned by *xml.etree*.

    Args:
        xval:
            The input tree as received from 
            *xml.etree.cElementTree*.

        kargs:
            striproot:
                Strips the root node. The named root node is mandatory due
                to the standard of W3C. Common other syntaxes such as *JSON*,
                *YAML*, and *INI* do not have unique baned root nodes at all.
                The *striproot* parameter removes the name root node, thus
                makes the structure of the scanned data tree compatible to
                the other syntax representations. ::

                    striproot := (
                          True    # the named root node is removed
                        | False   # the named root node is preserved
                    )

                    default := False

                The parameter is processed in the first call of the recursion  
                only, thus not passed to further calls.

    Returns:
        The resulting scanned data structure.

    Raises:
        pass-through
        
    """
    _striproot = kargs.get('striproot')
    if _striproot != None:
        # processed in the first call only
        _striproot = kargs.pop('striproot')
    

    if not xval.getchildren():
        #
        # no child objects, but eventually attributes and/or content
        #
        if xval.attrib:
            _xv = DataTreeXML.strtotype(_COMPCONT.sub(r'', xval.text))

            if not isinstance(_xv, dict):
                _xv = {DataTreeXML._content: _xv}

            if _striproot:
                top = _xv
            else:
                top = {xval.tag: _xv}

            for _ak, _av in xval.attrib.items():
                _xv[DataTreeXML._attrpre + _ak] = DataTreeXML.strtotype(_COMPCONT.sub(r'', _av))

        else:
            if _striproot:
                return DataTreeXML.strtotype(_COMPCONT.sub(r'', xval.text))
            else:
                return {xval.tag: DataTreeXML.strtotype(_COMPCONT.sub(r'', xval.text))}

    else:
        if _striproot:
            top = jsub = {}
        else:
            jsub = {}
            top = {xval.tag: jsub}
            
        _sublist = {}  # could be one of list-of-lists - want it in stateless a stream
        _content = xval.text

        for _ka, _va in xval.attrib.items():
            jsub[DataTreeXML._attrpre + _ka] = DataTreeXML.strtotype(_COMPCONT.sub(r'', _va))

        for child in xval:
            _content += child.tail 

            _x = readout_data(child)
            _k, _v = tuple(_x.items())[0]
            _v = DataTreeXML.strtotype(_v)

            if _k in jsub.keys():
                #
                # list
                #
                if _k in _sublist:
                    _sublist[_k].append(_v)
                else:
                    _l = [jsub[_k], _v]
                    _sublist[_k] = _l
                    jsub[_k] = _l

            else:
                jsub[_k] = _v

        if _COMPCONT.sub(r'', _content) != '':
            # only present content is displayed
            jsub[DataTreeXML._content] = _COMPCONT.sub(r'', _content)

    return top


class DataTreeXML(DataTree):
    """Provides XML based read-only configuration of capabilities.
    This in particular comprises the priority based readout
    of values and defaults. The structure hereby includes
    specialization by subcomponents, where the missing value 
    will be tried from the more general enclosing super
    component.
    
    The access to structured data trees offers various method to
    access paths of nested node attributes. This comprises the
    creation as well as the readout.
    
    The following equivalent creation methods are supported, where
    'treenode' could be either the root node, or any subordinated
    branch::

        treenode['subnode0']['subnode1']['subnode7'] = value  # dynamic items
        
        value = treenode(
                    'subnode0', 'subnode1', 'subnode7',
                    create=True,
                )  # dynamic items by '__call__'

        value = treenode.subnode0.subnode1.subnode7           # static attribute addressing style

    The following equivalent readout methods are supported, where
    'treenode' could be either the root node, or any subordinated
    branch::

        value = treenode['subnode0']['subnode1']['subnode7']  # dynamic items
        value = treenode('subnode0', 'subnode1', 'subnode7')  # dynamic items by '__call__'
        value = treenode.subnode0.subnode1.subnode7           # static attribute addressing style

    """

    #: defines the conversion from internal JSON data into XML    
    TOsyntaxdialect = {
    }

    #: attribute prefix
    _attrpre = '@'

    #: attribute name of content
    _content = '__content'

    def __init__(self, data={}, **kargs):
        """
        Args:
            data:
                A JSON compliant in-memory data tree in accordance to RFC-7159::

                    json-value := (
                          object | array
                        | number
                        | string
                        | false  | true
                        | null
                    )

                The equivalent *Python* types are - based on JSON-RFC7159 as canonical in-memory data::

                    RFC-7159-type-for-json := (
                          dict | list            # see: object, array
                        | int  | float           # see: number
                        | str                    # see: unicode / for Python: ISSTR = (str(3) | unicode(2))
                        | None | True  | False   # see: null, true, false
                    )

                The initial data defines the permitted type of the first item
                within the *subpath* of the spanned data tree.
                
                Thus atomic data types define a single node data tree only - new in RFC-7159.

        Returns:
            None / initialized object

        Raises:
            YapyDataDataTreeError

            pass-through

        """
        DataTreeXML.isvalid_top(data)
        super(DataTreeXML, self).__init__(data)

    def __setattr__(self, name, value):
        """Validates types of own data attributes.

        Args:
            name:
                Name of the attribute. Following are reserved and
                treated special:
                
                * type: str - 'data'
                  The value is treated as the replacement of the internal
                  data attribute. Replaces or creates the complete data
                  of teh current instance.

            value:
                The value of the attribute. This by default superposes
                present values by replacement. Non-present are created.

        Returns:

        Raises:
            YapyDataDataTreeError

        """
        if name == 'data':
            #
            # replacement of current managed data
            #
            if not isinstance(value, dict):
                raise YapyDataXMLError(
                    "value must be a 'dict', got: "
                    + str(type(value))
                    ) 

            self.__dict__[name] = value

        else:
            #
            # any standard attribute with standard behavior
            #
            return object.__setattr__(self, name, value)

    @staticmethod
    def strtotype(cdatain):
        """Provides optional automatic type cast for basic atomic types and 
        keywords by basic heuristics.
        
        For advanced generic type casts use e.g. XMLschema.
        
        Args:
            cdatain:
                Character data input. The value eventually representing a
                known non-string type. Supported conversions are::

                    known-types := (
                          int         # integer: [+-][0-9]+
                        | float       # float:   [+-][0-9]+[.][0-9]+
                        | null        # None:    null
                        | true        # True:    true
                        | false       # False:   false
                    )

                The applicable container type *object* is provided by
                the document structure, the type *array* is implemented
                within *readout_data*.

        Returns:
            Converted input, or raw input for unknown.

        Raises:
            pass-throuhg

        """
        try:
            # int
            return int(cdatain)

        except (ValueError, TypeError):
            try:
                # float
                return float(cdatain)

            except (ValueError, TypeError):
                try:
                    # common conceptual keywords: true, false, null
                    return KEYWORDS[cdatain]

                except KeyError:
                    return cdatain
                
                except TypeError:
                    return cdatain

        return cdatain

    #: defines the conversion from XML into internal JSON data    
    FROMsyntaxdialect = {
        'xml': {
            
            "Abdera_Convention": {
                "call": readout_data,
            },
            "Apache_Camel_Convention": {
                "call": readout_data,
            },
            "Badgerfish_Convention": {
                "call": readout_data,
            },
            "GData_Convention": {
                "call": readout_data,
            },
            "Gnome_Convention": {
                "call": readout_data,
            },
            "JsonML_Convention": {
                "call": readout_data,
            },
            "NewtonSoft_Convention": {
                "call": readout_data,
            },
            "oData_Convention": {
                "call": readout_data,
            },
            "Parker_Convention": {
                "call": readout_data,
            },
            "Spark_Convention": {
                "call": readout_data,
            },
        }
    }

    @staticmethod
    def isvalid_top(value, **kargs):
        """NOP"""
        return

    def import_data(self, fpname, key=None, node=None, **kargs):
        """Reads a XML file. This is a simple basic method for the application
        on the lower layers of the software stack. It is designed for minimal
        dependencies. The used library is the standard *xml.etree* library,
        so in the current first release *DOM* based. The data is by not validated.  
        
        Args:
            fpname:
                File path name of the *XML* file. ::

                    fpname := <xml-file-path-name>
                    xml-file-path-name := (
                          <file-path-name>           # with extension
                        | <file-path-name> '.xml'   # without extension, for multiple syntaxes
                    )

            key:
                The key for the insertion point::

                    node[key] = <file-data>

                    default := None - replace self.data, 

                The caller is responsible for the containment of the provided
                node within the data structure represented by this object. No
                checks are performed. 

            node:
                The node for the insertion of the read data.::

                    default := <top>

            kargs:
                striproot:
                    Strips the root node. The named root node is mandatory due
                    to the standard of W3C. Common other syntaxes such as *JSON*,
                    *YAML*, and *INI* do not have unique baned root nodes at all.
                    The *striproot* parameter removes the name root node, thus
                    makes the structure of the scanned data tree compatible to
                    the other syntax representations. ::

                        striproot := (
                              True    # the named root node is removed
                            | False   # the named root node is preserved
                        )

                        default := False

                    The parameter is processed in the first call of the recursion  
                    only, thus not passed to further calls.

        Returns:
            Reference to read data structure.

        Raises:
            YapyDataConfigError

            pass-through

        """
        if not os.path.isfile(fpname):
            if not os.path.isfile(fpname + '.xml'):
                raise YapyDataTreeError("Missing file: " + str(fpname))
            else:
                fpname = fpname + '.xml'

        datafile = os.path.abspath(fpname)
        xval = ET.ElementTree(file=datafile).getroot()
        
        # readout data
        jtree = readout_data(xval, **kargs)

        if key and node == None:
            raise YapyDataTreeError("Given key(%s) requires a valid node." % (str(key)))

        if key:
            node[key] = jtree
        else:
            self.data = jtree

        return jtree

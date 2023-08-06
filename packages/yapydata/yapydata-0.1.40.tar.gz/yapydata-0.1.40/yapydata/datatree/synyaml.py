# -*- coding: utf-8 -*-
"""The *YapyData.xml* module provides *XML*.
"""

import os

import yaml

from yapydata.datatree import YapyDataTreeError
from yapydata.datatree.datatree import DataTree


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyDataYAMLError(YapyDataTreeError):
    """Generic YAML syntax error. 
    """
    pass


def readout_data(xval, **kargs):
    """For API call-compliance with other syntaxes. Returns here the
    input tree only.

    Args:
        xval:
            The input tree from the *DataTreeYAML*- which is
            the result from *yaml.load()*.

    Returns:
        The returns here the input *xval*.

    Raises:
        pass-through
        
    """
    return xval


class DataTreeYAML(DataTree):
    """Provides YAML based read-only configuration of capabilities.
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

    #: defines the conversion from XML into internal JSON data    
#     FROMsyntaxdialect = {
#         'xml': {
#             
#             "Abdera_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "Apache_Camel_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "Badgerfish_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "GData_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "Gnome_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "JsonML_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "NewtonSoft_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "oData_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "Parker_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#             "Spark_Convention": {
#                 "call": DataTreeYAML.readout_data,
#             },
#         }
#     }

    def __init__(self, data=None, **kargs):
        """
        Args:
            data:
                A YAML compliant in-memory data tree::

                    yaml-value := (
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
        DataTreeYAML.isvalid_top(data)
        super(DataTreeYAML, self).__init__(data)

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
#             if not isinstance(value, (dict, list,)):
#                 raise YapyDataXMLError(
#                     "value must be a 'dict' == JSON-object or list == JSON-list, got: "
#                     + str(type(value))
#                     ) 
            self.__dict__[name] = value

        else:
            #
            # any standard attribute with standard behavior
            #
            return object.__setattr__(self, name, value)

    @staticmethod
    def isvalid_top(value, **kargs):
        """NOP"""
        return

    def import_data(self, fpname, key=None, node=None, **kargs):
        """Reads a YAML file. This is a simple basic method for the application
        on the lower layers of the software stack. It is designed for minimal
        dependencies. The used library is the *PyYaml* package.
        
        Args:
            fpname:
                File path name of the *YAML* file. ::

                    fpname := <yaml-file-path-name>
                    yaml-file-path-name := (
                          <file-path-name>           # with extension
                        | <file-path-name> '.yaml'   # without extension, for multiple syntaxes
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

        Returns:
            Reference to read data structure.

        Raises:
            YapyDataConfigError

            pass-through

        """
        if not os.path.isfile(fpname):
            if not os.path.isfile(fpname + '.yaml'):
                raise YapyDataTreeError("Missing file: " + str(fpname))
            else:
                fpname = fpname + '.yaml'

        datafile = os.path.abspath(fpname)
        with open(datafile) as data_file:
            xval = yaml.load(data_file)
        jtree = xval

        if key and node == None:
            raise YapyDataTreeError("Given key(%s) requires a valid node." % (str(key)))

        if key:
            node[key] = jtree
        else:
            self.data = jtree

        return jtree

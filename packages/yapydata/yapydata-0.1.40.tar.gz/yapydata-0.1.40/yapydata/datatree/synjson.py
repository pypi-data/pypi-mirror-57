# -*- coding: utf-8 -*-
"""The *YapyData.json* module provides *JSON* access in compliance to RFC-7159 [RFC7159]_.
"""

import os

import json as myjson

from pythonids import ISSTR

from yapydata.datatree import YapyDataTreeError
from yapydata.datatree.datatree import DataTree, YapyDataDataTreeOidError

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyDataJSONError(YapyDataTreeError):
    """Basic JSON syntax error. 
    """
    pass


def readout_data(xval, **kargs):
    """For API call-compliance with other syntaxes. Returns here the
    input tree only.

    Args:
        xval:
            The input tree from the *DataTreeJSON* - which is 
            the result from *json.load()*.

    Returns:
        The returns here the input *xval*.

    Raises:
        pass-through
        
    """
    return xval


def grow_branch(*subpath, **kargs):
    """Creates a new branch including the assigned value to
    the last node. The node types are defined by the types
    of the *subpath* entries.
    
    Supports a single linear branch only, no sub-branching.
    
    The created path is validated for permitted types.
    The derived types such as JSON have to support their
    own branch method. Thus provided as a static method.

    Args:
        subpath:
            Variable list/tuple of path keys and indexes.

        kargs:
            value:
                Value to be assigned to the final node. 

    Returns:
        A created branch.

    Raises:
        pass-through

    """
    _val = kargs.get('value')
    _subpath=list(subpath)
    try:
        ik = _subpath.pop(0)
    except IndexError:
        return _val
    
    if isinstance(ik, int):
        if ik != 0:
            # no padding
            raise YapyDataDataTreeOidError(
                    "new list requires idx==0: %s\n see: %s\n" %(
                        str(subpath),
                        str(ik)
                    )
                )
        return [grow_branch(*_subpath, value=_val)]

    elif isinstance(ik, ISSTR):
        # python only: (True, False, None,)
        return {ik: grow_branch(*_subpath, value=_val)}
    
    raise YapyDataDataTreeOidError(
            "invalid subpath key/index: %s\n see: %s\n" %(
                str(subpath),
                str(ik)
            )
        )


class DataTreeJSON(DataTree):
    """Provides JSON RFC-7159 compliant in-memory data trees.
    """

    @staticmethod
    def isvalid_top(value, **kargs):
        """Validate conformance of top-node to RFC-7159.
        """

        if (
            not isinstance(
                value, 
                (dict, list, int, float,)
            )
            and value not in (None, True, False,)
            and not isinstance(value, ISSTR)
            ):
                raise YapyDataJSONError(
                    "top 'node' must be a valid JSON-RFC-7159 type, got: "
                    + str(type(value))
                    ) 

    def __init__(self, data=None, **kargs):
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

                The equivalent *Python* types are::

                    data := <RFC-7159-type-for-json>

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
        DataTreeJSON.isvalid_top(data)
        super(DataTreeJSON, self).__init__(data)

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
            DataTreeJSON.isvalid_top(value)
            self.__dict__[name] = value

        else:
            #
            # any standard attribute with standard behavior
            #
            return object.__setattr__(self, name, value)

    def create(self, *subpath, **kargs):
        """Adds constraints in accordance to RFC-7159.
        """
        if subpath:
            DataTreeJSON.isvalid_top(subpath[0])
        else:
            value = kargs.get('value')
            DataTreeJSON.isvalid_top(value)
        return DataTree.create(self, *subpath, **kargs)

    def import_data(self, input, key=None, node=None, **kargs):
        """Reads a JSON file. This is a simple basic method for the application
        on the lower layers of the software stack. It is designed for minimal
        dependencies. The used library is the standard *json* package.
        The data is not validated.  
        
        Args:
            input:
                The source of the *JSON* string data::
                
                    input := (
                           <fpname>        # file path name
                        |  <file-id>       # file pointer id
                        |  <io-stream>     # io stream id
                    )

                    fpname := <json-file-path-name>
                    json-file-path-name := (
                          <file-path-name>           # with extension
                        | <file-path-name> '.json'   # without extension, for multiple syntaxes
                    )
                    file-id := "open file: file_id = open(<fpname>)"
                    io-stream := "open io stream - io_stream = io.StreamIO(<json-string>)"
                    json-string := "a valid string in accordance to RFC-7159"

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
        if isinstance(input, ISSTR):
            if os.path.isfile(input):
                # complete path
                datafile = os.path.abspath(input)
            elif os.path.isfile(input + '.json'):
                # auto extension
                datafile = os.path.abspath(input) + '.json'
            else:
                raise YapyDataTreeError("Missing file: " + str(input))

            with open(datafile) as data_file:
                jval = myjson.load(data_file)

        elif hasattr(input, 'read'):
            jval = myjson.load(input)

        else:
            raise YapyDataTreeError("Cannot read data: " + str(input))

        if key and node == None:
            raise YapyDataTreeError("Given key(%s) requires a valid node." % (str(key)))

        if key:
            node[key] = jval
        else:
            self.data = jval

        return jval

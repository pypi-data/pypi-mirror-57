# -*- coding: utf-8 -*-
"""The *YapyData.json4627* module provides *JSON* access in compliance to RFC-4627 [RFC4627]_.
"""

from yapydata.datatree.synjson import DataTreeJSON, YapyDataJSONError

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyDataJSON4627Error(YapyDataJSONError):
    """Basic JSON syntax error. 
    """
    pass


class DataTreeJSON4627(DataTreeJSON):
    """Provides additional constraints for JSON based on RFC-4627.
    
    The main point is here probably the required *object* or *array*
    as the root node, while RFC-7159 permits in general values.
    """

    @staticmethod
    def isvalid_top(value, **kargs):
        """Validate conformance of top-node to RFC-4627.
        """

        if not isinstance(value, (dict, list,)):
            raise YapyDataJSON4627Error(
                "top 'node' must be a valid JSON-RFC-4627 type, got: "
                + str(type(value))
                ) 

    def __init__(self, data, **kargs):
        """
        Args:
            data:
                Configuration data in accordance to RFC-4627::

                    data := <RFC-4627-type-for-json>

                    RFC-4627-type-for-json := (
                          dict | list            # see: object, list
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
        DataTreeJSON4627.isvalid_top(data)
        super(DataTreeJSON4627, self).__init__(data)

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
            DataTreeJSON4627.isvalid_top(value)
            self.__dict__[name] = value

        else:
            #
            # any standard attribute with standard behavior
            #
            return object.__setattr__(self, name, value)


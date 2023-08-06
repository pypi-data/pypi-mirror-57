# -*- coding: utf-8 -*-
"""The *YapyData.ini* module provides the extended *INI* file syntax access 
with optional extended syntax features.
The core syntax is defined by the standard library *configparser.ConfigParser*,
*YapyData.data* supports *Python2.7*, and *Python3.5+*.

"""

from __future__ import absolute_import

import os
import sys
import re

import itertools

from pythonids import PYV35Plus, ISSTR
from sourceinfo.fileinfo import getcaller_filename, getcaller_linenumber 


if PYV35Plus:
    import configparser  # @UnusedImport @UnresolvedImport
else:
    # requires 'strict' parameter, thus the back-port,
    # for now keep the construct
    #import ConfigParser as configparser  # @Reimport @UnusedImport @UnresolvedImport

    # decided to switch to the backport from Python3 - need __getitem__
    import configparser  # @UnusedImport # @Reimport


try:
    from ConfigParser import ConfigParser  # @UnusedImport
except:
    from configparser import ConfigParser  # @Reimport @UnusedImport


from collections import OrderedDict

import yapydata
from yapydata.datatree import YapyDataTreeError
from yapydata.datatree.datatree import DataTree, YapyDataDataTreeOidError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyDataINIError(YapyDataTreeError):
    """Generic INI syntax error. 
    """
    pass


#: fixed common keyword for special values - supported case sensitive and literally only
_KEYWORDS = {'true':True, 'false': False, 'null':None,}


#
# container types
#
_C_LIST = 1  #: list
_C_DICT = 2  #: dict

_C_BYTEARRAY = 4
_C_TUPLE = 8
_C_SET = 16


#: container markers - default generic base types
_CONTAINERS = {
    'default': _C_LIST,             # default
    '': _C_LIST,                    # default too, will pop the empty item
    'list': _C_LIST,                # generic base type: list - array
    'dict': _C_DICT,                # generic base type: dict - object
}


#: Container markers for extended types specific to this module.
#: Do not use them in multi-syntax environments.
#: These are meant to be concatenated to _CONTAINERS by choice.
#: Some constraints apply to these types for Python.
#: E.g. immutable, non-subscriptable, so applicable in specific
#: data tree contexts only.
_CONTAINERSX = {
    'bytearray': _C_BYTEARRAY,      # array of bytes {0..256}
    'tuple': _C_TUPLE,              # immutable tuple
    'set': _C_SET,                  # non-subscriptable set
}


#: Gets list entries.
#: win uses '\n' too: _CONCAT_LIST=re.compile(os.linesep + r'[ \t]*,')
_CONCAT_LIST=re.compile(r'\r{0,1}\n[ \t]*,')

#: Compiles regexpr for search paths spanning multiple lines.
_CONCAT_PATH=re.compile(r'\r{0,1}\n[ \t]*[:]')

#: Compiles regexpr for search paths spanning multiple lines.
_CLEAR_KEY=re.compile(r'^[ \t]*(.*?)[ \t]*$')


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

    elif isinstance(ik, ISSTR) or ik in (True, False, None,):
        # python only: (True, False, None,)
        return {ik: grow_branch(*_subpath, value=_val)}
    
    elif isinstance(ik, frozenset):
        # python only
        return {ik: grow_branch(*_subpath, value=_val)}
    
    raise YapyDataDataTreeOidError(
            "invalid subpath key/index: %s\n see: %s\n" %(
                str(subpath),
                str(ik)
            )
        )


def readout_data(xval, **kargs):
    """Scan tree into JSON representation. Uses recursive calls to 
    readout_data through  the logical tree spanned by *ConfigParser*.

    Args:
        xval:
            The loaded input tree as received from *ConfigDataINIX*,
            which is defined by *ConfigParser.read_file()*.

            For example a node *cf*::

                datafile = os.path.abspath(fpname)
                cf = ConfigDataINIX(datafile)
                cf.load_parser()
                cf.import_data(datafile)

            is read out as ::

                datatree = readout_data(cf)

                
    Returns:
        The resulting scanned data structure.

    Raises:
        pass-through
        
    """
    return xval.readout_data()


class MultiOrderedDict(OrderedDict):
    """Add lists for multi-key items.
    """
    def __setitem__(self, key, value):
        """Intercept keys which are already present.
        """
        if key in self:
            if isinstance(value, list):
                if isinstance(self[key], list):
                    try:
                        self[key].extend(value)
                    except KeyError:
                        self[key] = value
                else:
                    self.__dict__[key] = value
                return
                # elif isinstance(value,str):
                #    return
        super(MultiOrderedDict, self).__setitem__(key, value)


class CaseSensitiveConfigParser(configparser.ConfigParser):
    """Preserves case of all keys - including DEFAULT section.
    Suppress formatting of *optionstr*, preserves upper case characters.
    """
    def optionxform(self, optionstr):
        return optionstr


class DataTreeINI(DataTree):
    """The the supported in-memory data tree representation of the *INI* syntax 
    supports a JSON compatible in memory data structure. The supported structure 
    relies on the standard *ConfigParser* - of *Python2* and *Python3* - with a 
    minimum set of custom addons. For a full set of extensions refer to the 
    package *multiconf*.

    The basic scheme of the stored syntax is::
    
        ini-for-in-memory-json := {
            <sections>
        }
        sections := <section> [, <sections>]
        section := <section-attributes>
        section-attributes := <attr-value-pairs> [, <section-attributes>]
        attr-value-pairs :=  <attr-value-pair> [, <attr-value-pairs>]
        attr-value-pair := <attr-name> <separator> <attr-value>
        attr-name := "any valid ConfigParser string compatible to a JSON string"
        attr-value := (
              <integer>   | <integer-as-string>
            | <float>     | <float-as-string>
            | <string>
            | <list>
            | <dict>
            | <boolean>   | <boolean-as-string>
            | <null>      | <null-as-string>
        )

        integer-as-string := '"' <integer> '"'                  # treated as string
        integer := "any non-quoted valid integer value"         # treated as integer
        float-as-string := '"' <float> '"'                      # treated as string
        float := "any non-quoted valid integer value"           # treated as float
        string := "any valid string"
        boolean := (true | false)
        boolean-as-string := '"' <boolean> '"'                  # treated as string
        null := null
        null-as-string := '"' <null> '"'                        # treated as string
        separator := ( ':' | '=' )

    The following derived proprietary container types are provided. These are
    compatible with the basic representation of the higher layer *multiconf*
    package, which also provides command line compilation and cross-conversion 
    utilies.
    
    The *list* entries are represented as multiple lines of entries with leading
    white-spaces and a comma. ::

        list := <proprietary-basic-multiline-list-syntax>
        proprietary-basic-multiline-list-syntax := <attr-name> <separator> <list-item> <CR> <list-items-multiline> <CR>
        list-items-multiline := <ws> ',' <list-item> <CR> [<list-items-multiline>]
        list-item := attr-value
        ws := "arbitrary whitespace - <SPACE>, <tab>"
        CR := "new line"

    The *dict* entries are represented as multiple lines of entries with leading 
    white-spaces and a comma::

        dict := <proprietary-basic-multiline-dict-syntax>
        proprietary-basic-multiline-dict-syntax := <attr-name> <separator> <attr-dict-item> <CR> <dict-items-multiline> <CR>
        dict-items-multiline := <ws> ',' <dict-item> <CR> [<dict-items-multiline>]
        dict-item := attr-value-pair
        ws := "arbitrary whitespace - <SPACE>, <tab>"
        CR := "new line"

    The data tree is compatible with the standard packas *json*.

    """

    @staticmethod
    def isvalid_top(value, **kargs):
        """Validate compliance of top-node.
        """
        if not isinstance(value, (dict, list, )):
            raise YapyDataINIError(
                "top 'node' must be a valid INI type for RFC-4627 processing: (dict, list), got: "
                + str(type(value))
                ) 
        return

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

            kargs:
                syntax:
                    Defines the syntax variant::

                        syntax := (
                              'base'  # base core syntax for multi-syntax environments with global types 
                            | 'ext'   # extended syntax with specific extension for this module
                            | 'auto'  # for now enables all choices - basically the same as 'ext'
                        )
                        
                        default := 'base'  # maximum compatibility for multi-syntax environments

        Returns:
            None / initialized object

        Raises:
            YapyDataDataTreeError

            pass-through

        """
        
        _syn = kargs.get('syntax')
        if _syn in ('ext', 'auto',):
            # enable optional syntax extensions 
            global _CONTAINERS
            _CONTAINERS.update(_CONTAINERSX)
        
        # check data validity - pass eventual syntax parameters
        DataTreeINI.isvalid_top(data, **kargs)
        
        # actually initialize Python
        # enabled syntax variant is not checked in depth - used currently by 'trust' ... and exceptions...
        super(DataTreeINI, self).__init__(data)

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
            YapyDataINIError

        """
        if name == 'data':
            #
            # replacement of current managed data
            #
            DataTreeINI.isvalid_top(value)
            self.__dict__[name] = value

        else:
            #
            # any standard attribute with standard behavior
            #
            return object.__setattr__(self, name, value)

    def import_data(self, fpname, key=None, node=None, **kargs):
        """Reads an INI file. This is a simple basic method for the application
        on the lower layers of the software stack. It is designed for minimal
        dependencies. The used library is the standard *configparser* package.
        
        Args:
            fpname:
                File path name of the *INI* file. ::

                    fpname := <ini-file-path-name>
                    ini-file-path-name := (
                          <file-path-name>           # with extension
                        | <file-path-name> '.ini'    # without extension, for multiple syntaxes
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
            if not os.path.isfile(fpname + '.ini'):
                raise YapyDataINIError("Missing file: " + str(fpname))
            else:
                fpname = fpname + '.ini'

        datafile = os.path.abspath(fpname)
        cf = ConfigDataINIX(datafile)
        cf.load_parser()
        cf.import_data(datafile)

        jval = cf.readout_data()

        if key and node == None:
            raise YapyDataINIError("Given key(%s) requires a valid node." % (str(key)))

        if key:
            node[key] = jval
        else:
            self.data = jval

        return jval


class ConfigDataINIX(object):
    """A simple configuration file parser based on the standard *ConfigParser* class.
    
    The final resulting data with completely applied syntax-extensions is available by
    the method *readout_data()*.
    
    Supports the data types::
    
        int, float, str
    
        multi-line lists,
        multi-line search-paths
       
        null
        true, false
       
    The optional structure::
        
        global-attributes-without-section
    
    The standard file extensions are::
    
       '.ini'

    The supported stnadard features of *ConfigParser* include::

        interpolation

    For detailed information refer to the parameters of the *__init__* method.
    """

    suffixes = ('ini', ) #: standard suffixes for INI


    def __init__(self, conf, **kargs):
        """
        Args:
            **conf**:
                The file path name of the configuration file.
        
           kargs:
                For additional parameters see *ConfigData*.
                
                allow_no_value:
                    Enables the support for keys without values
                    of *INI* format files. Supported by the standard
                    library based *configparser* . The value
                    could be applied to derived custom parser::
                    
                        default := False
                    
                    See parameter *allow_no_value* of
                    *configparser.ConfigParser*.
                
                casesens:
                    Preserves case of keys::
                
                        default := False
                
                comment_prefixes:
                    Defines the comment prefixes::
                
                        default := ('#', ';')
                
                delimiters:
                    Defines the delimiters for *INI* format based
                    files. Supported by the standard library based
                    *configparser* . The value could be applied to
                    derived custom parser::

                        default := ('=', ':',)
                
                dict_type:
                    The type of dictionary to be used by the parent class::
                
                        default := None
                
                empty_lines_in_values::

                    default := False
                
                inline_comment_prefixes:
                    Defines the inline comment prefixes::

                        default := None
                
                interpolation:
                    Enables the creation and replacement of variables
                    within configuration files. Depends on the derived
                    class, when not supported simply ignored::
                
                        default := True
                
                    See parameter *interpolation* of
                    *configparser.ConfigParser*.
                
                sectionpaths:
                    Enables the conversion and interpretation of section names
                    as path entries. This is required, when the versatility
                    of the converted and/or merged syntaxes are of different degree,
                    and the actual used syntax data path elements could not be
                    converted. In this case an intermediate sub-syntax is supported
                    by a dotted path notation, which could be converted between the 
                    applied syntaxes::
                    
                        sectionpaths := (
                             True         # long data paths e.g. from *JSON* are 
                                          # converted to dotted section names
                                          # and vice versa
                           | False        # requires compatible versatility,
                                          # else raises exception
                        )
                        
                        default := True
                
                   
                    sectionpaths=True:
                        The section names of the native *INIX* syntax by default 
                        constitute a one-level-only depth of data structures for 
                        the complexity of structure definition.
                        
                    sectionpaths=False:
                        
                
                sectionpathsep:
                    Defines the character used in section names as path separator.
                    The character has to be valid as provided by the config parser of the syntax, 
                    in particular a valid character for section names of *INI* files, and has
                    to be semantically suitable as a special separator character::
                      
                        sectionpathsep := []
                        
                        default := '.'
                   
                    Valid only when *sectionpaths* is active. 
                
                strict:
                    Controls the verification of duplicate sections
                    when these are used::
                
                        strict := (
                              True    # raise an exception for duplicates
                            | False   # accept
                        )
                        
                        default := False
                
                    See *strict* option of *ConfigParser*.
                
                quiet:
                    Suppresses display of non-errors::

                        default := False
        
        Returns:
            None/object
        
        Raises:
            pass-through

        """
        self.allow_no_value = kargs.get('allow_no_value', False)
        self.casesens = kargs.get('casesens', False)
        self.comment_prefixes = kargs.get('comment_prefixes', ('#', ';'))
        self.delimiters = kargs.get('delimiters', ('=', ':',))
        self.dict_type = kargs.get('dict_type', None)
        self.empty_lines_in_values = kargs.get('empty_lines_in_values', False)
        self.inline_comment_prefixes = kargs.get('inline_comment_prefixes', None)
        self.interpolation = kargs.get('interpolation', True)
        self.quiet = kargs.get('quiet', False)
        self.strict = kargs.get('strict', False) # changed default

    def __bool__(self):
        try:
            return len(self.confdata.sections()) > 0
        except Exception:
            return False

    def __nonzero__(self):
        try:
            return len(self.confdata.sections()) > 0
        except Exception:
            return False

    def __getitem__(self, key):
        """Get the section object.
       Requires for Python2 the backport from Python3 "configparser", see PyPI
        """
        return self.confdata[key]

    def get(self, key):
        """Get the section object - compatible to Python3 and
        the backport of the *configparser*.
        """
        if key in self.confdata.sections():
            return self.confdata[key]
        return None

    def import_data(self, conf, **kargs):
        """Reads the configuration file and imports data. Supported standard types are::
   
           'cfg', 'conf', 'ini',
        
        The imported data for the suported standard syntax is interpreted as:
        
            +----------------------------------------+-------------+-------------------+-------------+-------------------------+----------------------------------------------+
            | syntax of imported config              | sections as | keys as           | path as     | insertion position      | remark                                       |
            +========================================+=============+===================+=============+=========================+==============================================+
            | `conf <parser_conf.html>`_             | sections    | keys to <section> | --          | top, <section>, DEFAULT | no rename and no nested sections, no globals |
            +----------------------------------------+-------------+-------------------+-------------+-------------------------+----------------------------------------------+
            | `ini <parser_ini.html>`_               | sections    | keys by section   | --          | top, <section>, DEFAULT | no rename and no nested sections, no globals |
            +----------------------------------------+-------------+-------------------+-------------+-------------------------+----------------------------------------------+
            | `inix <parser_inix.html>`_             | sections    | keys by section   | --          | top, <section>, DEFAULT | no rename and no nested sections, no globals |
            +----------------------------------------+-------------+-------------------+-------------+-------------------------+----------------------------------------------+
        
        Args:
            conf:
                The file path name of the configuration file.
        
           kargs:
                Unknown options are passed through to the
                configuration parser.
        
                anchor:
                    The insertion point for the imported data::
        
                      anchor := (
                           <section>
                         | 'DEFAULT'
                         | <top>
                      )
                      
                      top := "imports valid INIX/INI/CONF files with sections only"
                      section := "the name of the section"
                      'DEFAULT' := "keyword defined by the standard library as 
                                    global defaults for interpolation"
        
                      default := <top>
        
                strict:
                    Activates validation. The boolean value is
                    mapped to the corresponding option of the
                    called import parser:
        
                        +------------+----------+-------+--------+
                        | parser     | option   | True  | False  |
                        +============+==========+=======+========+
                        | conf       | strict   | True  | False  |
                        +------------+----------+-------+--------+
                        | ini        | strict   | True  | False  |
                        +------------+----------+-------+--------+
                        | inix       | strict   | True  | False  |
                        +------------+----------+-------+--------+
        
                syntax:
                    Force the provided syntax. For available
                    values refer to syntax multiplexer
                    *self.synmux*.
        
        Returns:
            True for success, else False or raises an exception.
        
        Raises:
            pass-through

        """

        # sectionless
        # add '[globaldummy]' for 'configparser'
        # will be removed by 'read_out'
        with open(conf) as fp:
            self.confdata.read_file(
                itertools.chain(['[globaldummy]'], fp),
                source=os.path.dirname(conf)
                )
        return self.confdata != []

 
    def keys(self):
        return self.confdata.sections()

    def load_parser(self, **kargs):
        """Loads the syntax parser *configparser.ConfigParser* and
        patches the behaviour for common 'conf' and 'cfg' format.
        Supports the most of the files in '/etc' of POSIX based
        OS.
        
        Args:
            kargs:
                For the description of the options refer to the
                method header of *multiconf.data.load_parser()*.
                Unknown are passed through to the loaded
                configuration parser.
        
                For the following parameters see __init__: 
        
                * **allow_no_value**
                * **casesens**
                * **comment_prefixes**
                * **inline_comment_prefixes**
                * **delimiters**
                * **dict_type**
                * **empty_lines_in_values**
                * **interpolation**
                * **strict**
                * **quiet**
        
        Returns:
            True, or raises an exception.
        
        Raises:
            pass-through
        
        """
        kw_optparser = {}

        try:
            kw_optparser['strict'] = kargs.pop('strict')
        except:
#             try:
#                 kw_optparser['strict'] = self.conf['strict']
#             except KeyError:
#                 kw_optparser['strict'] = self.strict
            pass

#         _ip = self.conf.get('interpolation')
#         if _ip:
#             if _ip.lower() in ('false', '0', 'off', 'no'):
#                 kw_optparser['interpolation'] = None
#             elif _ip.lower() not in ('false', '0', 'off', 'no'):
#                 raise MultiConfError("invalid value: interpolation=" + str(_ip))
#         elif self.interpolation == False:
#             kw_optparser['interpolation'] = None

#         _d = self.conf.get('delimiters', None)
#         if _d:
#             kw_optparser['delimiters'] = tuple(_d)
#         elif self.delimiters:
#             kw_optparser['delimiters'] = self.delimiters
# 
# 
#         _d = self.conf.get('comment_prefixes', None)
#         if _d:
#             kw_optparser['comment_prefixes'] = tuple(_d)
# 
#         _d = self.conf.get('inline_comment_prefixes', None)
#         if _d:
#             kw_optparser['inline_comment_prefixes'] = tuple(_d)
# 
#         _d = self.conf.get('empty_lines_in_values', None)
#         if _d:
#             kw_optparser['empty_lines_in_values'] = tuple(_d)
# 
#         _d = self.conf.get('allow_no_value', None)
#         if _d:
#             kw_optparser['allow_no_value'] = _d
#         elif not kargs.get('allow_no_value'):
#             kw_optparser['allow_no_value'] = self.allow_no_value
# 
#         dict_type = kargs.get('dict_type', self.dict_type)
#         if _d:
#             kw_optparser['dict_type'] = dict_type
# 
#         try:
#             _quiet = kargs.pop('quiet')
#         except:
#             pass

        # activate case senitivity
#        _cs = self.conf.get('casesens', False)
#         _cs = self.conf.get('casesens')
#         if _cs == None:
#             _cs = kargs.get('casesens', False)
#         if _cs not in (True, False):
#             if _cs is None:
#                 _cs = False
#             elif _cs.lower() in ('false', '0', 'off', 'no'):
#                 _cs = False
#             elif _cs.lower() not in ('true', '1', 'on', 'yes'):
#                 raise MultiConfError("invalid value: casesens=" + str(_cs))

        _cs = True
        if _cs:
            _parser = CaseSensitiveConfigParser
        else:
            _parser = configparser.ConfigParser

        if yapydata._debug > 1:
            sys.stderr.write(
                "DBG:%s:%s:_parser = %s\n" %(
                str(getcaller_filename()), 
                str(getcaller_linenumber()),
                str(_parser)
                )
            )
            sys.stderr.write(
                "DBG:%s:%s:kw_optparser = %s\n" %(
                str(getcaller_filename()), 
                str(getcaller_linenumber()),
                str(kw_optparser)
                )
            )

#         self.kw_optparser = kw_optparser
#         if dict_type:
#             self.confdata = _parser(
#                 dict_type=dict_type,
#                 **kw_optparser
#                 )
#         else:
#             self.confdata = _parser(
#                 **kw_optparser
#                 )

        self.confdata = _parser(
            **kw_optparser
            )

        return True

    def readout_data(self, **kargs):
        """Returns the configuration as JSON compatible format.
        Removes the special dummy section header 'globaldummy',
        see *import_data*.
        
        Args:
            kargs:
                stronly:
                    Scans all as *str* only. ::
        
                      stronly := (
                            True    # int and float are
                                    # converted to str
                          | False   # numeric values are kept
                      )
        
                    default := False
        
        Returns:
            In-memory JSON compatible data.
        
        Raises:
            pass-through

        """
        if self.confdata == None:
            return
        elif not self.confdata:
            return str(self.confdata)

        _stronly = kargs.get('stronly', False)

        res = {}
        for s in self.confdata.sections():
            if s == 'globaldummy':
                for k, v, in self.confdata.items(s):
                    if _stronly:
                        res[k] = v
                        continue

                    try:
                        # int
                        res[k] = int(v)
                    except (ValueError, TypeError):
                        try:
                            # float
                            res[k] = float(v)
                        except (ValueError, TypeError):
                            try:
                                # common conceptual keywords: true, false, null
                                res[k] = _KEYWORDS[v]
                            except KeyError:
#                                 try:
#                                     # is meta keyword only - maps the multi-line entry to a container type syntax
#                                     # default set is (dict, list), with the default selection of list
#                                     container = _CONTAINERS[v]
#                                 except KeyError:
                                try:
                                    _v = _CONCAT_LIST.split(v)
                                    if len(_v) > 1:

                                        # is meta keyword only - maps the multi-line entry to a container type syntax
                                        # default is list
                                        try:
                                            container = _CONTAINERS[_v[0]]
                                            _v.pop(0)
                                        except KeyError:
                                            container = _C_LIST  #: default container type

                                        if container == _C_DICT:
                                            # process comma separated multi-line dictionaries
                                            res[k] = {}
                                            for _vi in _v:
                                                _dk,_dv = re.split(r'[=:]', _vi, 1)
                                                _dk = str(_CLEAR_KEY.sub(r'\1', _dk))
                                                try:
                                                    res[k][_dk] = int(_dv)
                                                except (ValueError, TypeError):
                                                    try:
                                                        res[_dk] = float(_dv)
                                                    except (ValueError, TypeError):
                                                        res[_dk] = _dv

                                        elif container == _C_BYTEARRAY:
                                            # process comma separated multi-line bytearray
                                            # it is native and mutable, so do not need intermediate list
                                            res[k] = bytearray()
                                            for _vi in _v:
                                                try:
                                                    res[k].append(int(_vi))
                                                except ValueError:
                                                    # wrong range as well as non-int have ValueError
                                                    raise YapyDataTreeError(
                                                        "Bytearray(0..256) failed: [%s] = %s" %(
                                                            str(k),
                                                            str(_vi),
                                                            )
                                                        )

                                        else: # elif container == _C_LIST:
                                            # process comma separated multi-line lists and related
                                            res[k] = []
                                            for _vi in _v:
                                                try:
                                                    res[k].append(int(_vi))
                                                except (ValueError, TypeError):
                                                    try:
                                                        res[k].append(float(_vi))
                                                    except (ValueError, TypeError):
                                                        res[k].append(_vi)

                                            # now cast to closely related types
                                            if container == _C_TUPLE:
                                                res[k] = tuple(res[k])
                                            elif container == _C_SET:
                                                res[k] = set(res[k])

                                    else:
                                        res[k] = v
                                        
                                except TypeError:
                                    res[k] = v

            else:
                res[s] = {}
                for k, v, in self.confdata.items(s):
                    if _stronly:
                        res[s][k] = v
                        continue

                    try:
                        # int
                        res[s][k] = int(v)
                    except (ValueError, TypeError):
                        try:
                            # float
                            res[s][k] = float(v)
                        except (ValueError, TypeError):
                            try:
                                # common conceptual keywords: true, false, null
                                res[s][k] = _KEYWORDS[v]
                            except KeyError:
                                try:
                                    _v = _CONCAT_LIST.split(v)
                                    if len(_v) > 1:
                                        # is meta keyword only - maps the multi-line entry to a container type syntax
                                        # default is list
                                        try:
                                            container = _CONTAINERS[_v[0]]
                                            _v.pop(0)
                                        except KeyError:
                                            container = _C_LIST  #: default container type

                                        if container == _C_DICT:
                                            res[s][k] = {}
                                        else:  # elif container == _C_LIST:
                                            res[s][k] = []
                                        
                                        if container == _C_DICT:
                                            # process comma separated multi-line dictionaries
                                            #res[k] = {}
                                            for _vi in _v:
                                                _dk,_dv = re.split(r'[=:]', _vi, 1)
                                                _dk = str(_CLEAR_KEY.sub(r'\1', _dk))
                                                try:
                                                    res[s][k][_dk] = int(_dv)
                                                except (ValueError, TypeError):
                                                    try:
                                                        res[s][k][_dk] = float(_dv)
                                                    except (ValueError, TypeError):
                                                        res[s][k][_dk] = _dv

                                        elif container == _C_BYTEARRAY:
                                            # process comma separated multi-line bytearray
                                            # it is native and mutable, so do not need intermediate list
                                            res[s][k] = bytearray()
                                            for _vi in _v:
                                                try:
                                                    res[s][k].append(int(_vi))
                                                except ValueError:
                                                    # wrong range as well as non-int have ValueError
                                                    raise YapyDataTreeError(
                                                        "Bytearray(0..256) failed: [%s] = %s" %(
                                                            str(k),
                                                            str(_vi),
                                                            )
                                                        )

                                        else: # elif container == _C_LIST:
                                            # process comma separated multi-line lists and related
                                            res[s][k] = []
                                            for _vi in _v:
                                                try:
                                                    res[s][k].append(int(_vi))
                                                except (ValueError, TypeError):
                                                    try:
                                                        res[s][k].append(float(_vi))
                                                    except (ValueError, TypeError):
                                                        res[s][k].append(_vi)

                                            # now cast to closely related types
                                            if container == _C_TUPLE:
                                                res[s][k] = tuple(res[s][k])
                                            elif container == _C_SET:
                                                res[s][k] = set(res[s][k])

                                    else:
                                        res[s][k] = v

                                except TypeError:
                                    if v == None:
                                        res[s][k] = None
                                    else:
                                        raise

        return res

    def set(self, section, option, value):
        return self.confdata.set(section, option, value)


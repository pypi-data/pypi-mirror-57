# -*- coding: utf-8 -*-
"""The *YapyData.datatree* module provides the core class for the handling of
simple data classes for the most common data representation languages. The
provided core class *DataTree* provided the *Python* data types, which comprise
the most standard data types.

The derived classes support for the most common data description languages
and add therefore the specific constraints and extensions. The package provides
these features for low-level libraries of the software stack, therefore depends 
whenever possible on standard libraries only. It supports low-level read-only access
to files and in-memory data. The read data could be modified in-memory only for 
example in order to superpose higher priority data read from the call options
of the command line .

The internal representation of the DDLs is exclusively compatible to the standard
*json* package in accordance to *RFC-7159*. The supported DDLs of the read files are:

* *INI*
* *JSON*
* *XML*
* *YAML*

A similar package for higher application layer levels is available by *multiconf*,
which provides sophisticated features such as cross-conversion and mixed-mode applications
by modularization, and enhanced processing plugins for various DDLs.    

The validation and preparation including cross-conversion is supported by
**multiconf**, while the specifics of the *DL* is supported by the language
module such as *jsondata* and *xmldata*.
"""

from yapydata.datatree import YapyDataTreeError

import os

try:
    import cPickle as pickle  # @UnusedImport
except:
    import pickle  # @Reimport

from pythonids import ISSTR


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyDataDataTreeError(YapyDataTreeError):
    """Common access error. 
    """
    pass


class YapyDataTypeError(YapyDataTreeError):
    """Common access error. 
    """
    pass

def readout_data(xval, **kargs):
    """For API call-compliance with other syntaxes. Returns here the
    input tree only.

    Args:
        xval:
            The input tree from the *DataTree*.

    Returns:
        The returns here the input *xval*.

    Raises:
        pass-through
        
    """
    return xval


class YapyDataDataTreeOidError(YapyDataDataTreeError):
    """Requested object name is not present.
    """
    def __init__(self, message='', *args, **kargs):
        """Displays the issue of the exception.
        
        Args:
            message:
                The message to be displayed.
                Addition options *pathhook*, *path*, and
                *trailer* are appended when present.
                These are also provided as memmeber variables
                for derived exceptions.

            kargs:
                pathhook:
                    The missing item of the path.

                path:
                    Resolved path.

                searchpath:
                    Optional search path.

                trailer:
                    Optional textual hint.

        Returns:
            the raised exception
            
        Raises:
            itself
        """
        self.message_in = message
        message_out = message[:]
        
        try:
            self.pathhook = kargs.pop('pathhook')
        except KeyError:
            self.pathhook = ''

        try:
            self.path = kargs.pop('path')
        except KeyError:
            self.path = ''
        try:
            self.searchpath = kargs.pop('searchpath')
        except KeyError:
            self.searchpath = ''
        try:
            self.trailer = kargs.pop('trailer')
        except KeyError:
            self.trailer = ''
             
        if self.pathhook or self.path:
            message_out +=  "Missing subpath hook:"

        if self.pathhook:
            message_out +=  "\n  pathhook:     %s" % (str(self.pathhook))

        if self.path:
            message_out +=  "\n  path:         %s" % (str(self.path))

        if self.searchpath:
            message_out +=  "\n  searchpath:   %s" % (str(self.searchpath))

        if self.trailer:
            message_out +=  str(self.trailer)

        self.message_out = message_out

        super(YapyDataDataTreeOidError, self).__init__(message_out, *args, **kargs)


# mode
M_COMP = 1     #: complete
M_FRAG = 2     #: fragment
M_INC = 4      #: increment


# strategy
S_CREA = 256   #: create
S_DEL = 512    #: delete
S_JOIN = 1024  #: join
S_MOD = 2048   #: modify
S_REP  = 4096  #: replace


_debug = 0
_verbose = 0


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

                default := None

    Returns:
        A created branch.

    Raises:
        YapyDataDataTreeOidError

        pass-through

    """
    _val = kargs.get('value')
    _subpath=list(subpath)
    try:
        ik = _subpath.pop(0)
    except IndexError:
        return _val
    
    if isinstance(ik, (bool, float, frozenset)) or ik == None  or isinstance(ik, ISSTR):
        # python only: (True, False,), None, ...
        return {ik: grow_branch(*_subpath, value=_val)}

    elif isinstance(ik, int):
        if ik != 0:
            # no padding
            raise YapyDataDataTreeOidError(
                    "new list requires idx==0: %s\n see: %s\n" %(
                        str(subpath),
                        str(ik)
                    )
                )
        return [grow_branch(*_subpath, value=_val)]

    raise YapyDataDataTreeOidError(
            "invalid subpath key/index: %s\n see: %s\n" %(
                str(subpath),
                str(ik)
            )
        )
        

class DataTree(object):
    """Provides JSON based read-only configuration of capabilities.
    
    The access to structured data trees offers various methods to
    access paths of nested node attributes. This comprises the
    creation as well as the readout.

    The following equivalent creation methods are supported, where
    'treenode' could be either the root node, or any subordinated
    branch::

        treenode['subnode0']['subnode1']['subnode7'] = value  # dynamic items
        
        value = treenode.create(                              # dynamic items by 'create()'
                    'subnode0', 'subnode1', 'subnode7',
                )

        value = treenode.subnode0.subnode1.subnode7           # static attribute addressing style

    The following equivalent readout methods are supported, where
    'treenode' could be either the root node, or any subordinated
    branch::

        value = treenode['subnode0']['subnode1']['subnode7']  # dynamic items
        value = treenode('subnode0', 'subnode1', 'subnode7')  # dynamic items by '__call__'
        value = treenode.subnode0.subnode1.subnode7           # static attribute addressing style

    """

    M_FIRST = 1   # use first matching node
    M_LAST = 2    # use last matching node
    M_ALL = 3     # use all - iterate all matches

    match_map = {
        M_FIRST: 1,
        M_LAST: 2,
        M_ALL: 3,
        'first': 1,
        'last': 2,
        'all': 3,
    }    

    @staticmethod
    def isvalid_top(value, **kargs):
        """Validate compliance of top-node. To be provided by derived classes
        for specific syntaxes.
        
        Args:
            value:
                Top node.

            kargs:
                Specific syntax related dynamic parameters to be defined
                by derived classes.

        Returns:
            None

        Results:
            YapyDataTreeError:
                Raises exception when not valid.

        """
        pass

    def __init__(self, data=None):
        """
        Args:
            data:
                Configuration data in accordance to the selected data language syntax.
                The default is the Python syntax including the appropriate data types. 
                This may impose additional constraints by derived classes e.g. in case
                of persistent data such as JSON and XML - see other classes within
                this module.
                
                The default Python DL implementation supports in-memory access only,
                while persistence will be available for example by pickling.

                The initial *data* defines the permitted type of the first item
                within the *subpath* of the spanned data tree. The default value acts
                here as a placeholder for an empty structure, which could be defined
                by following extension operations arbitrarily.

                The basic constraint introduced here is that intermediate nodes
                require support of subscription. This is due to the addressing concepts
                implemented by *DataTree*. Thus even though a *set* could technically
                be an intermediate node, it could not be indexed, thus could not be
                addressed by the standard member functions. Resulting 'set' and 'frozenset'
                are supported by *DataTree* as end-nodes only, same as atomic data types.
                
                Anyhow, the <top-node> is by default permitted to be an end-node. Thus
                the context defines the applicability dynamically.

                The consistency of the data tree including the valid intermediate nodes
                is verified by access, so basically within the responsibility of the caller.

        Returns:

            None / initialized object

        Raises:
            YapyDataDataTreeError

            pass-through

        """
        self.data = data

    def __call__(self, *subpath, **kargs):
        """Readout the value of a node, or an attribute. The name binding
        of the path is provided as a tuple of path items. 

        Args:
            subpath:
                The list of keys constituting a branch of a data tree.
                The *subpath* is treated as a branch of one of the nodes
                of a provided *searchpath* - which is by default the top node.
                The supported values are::

                    subpath := <list-of-node-ids>
                    <list-of-node-ids> := <node-id> [',' <list-of-node-ids>]
                    node-id := (
                          str            # string:  dict
                        | int            # integer: lists, tuple, dict
                    )

                The value of the node within *data*::

                    nodeid := (
                          <single-nodeid>
                        | <list-of-nodeids>
                        | <tuple-of-nodeids>
                    )
                    single-nodeid := <nodeid>
                    list-of-nodeids := '[' <nodeidlists> ']'
                    tuple-of-nodeids := '(' <nodeidlists> ')'
                    nodeidlists := <nodeid> [',' <nodeidlists>]
                    nodeid := (
                          ItemKey
                        | ListIndex
                    )
                    ItemKey := "valid dict-key"
                    ListIndex := "valid list-index"

                The derived syntax classes may impose specific constraints.
                Thus it is recommended to use integers and strings only
                for maximum compatibility, and the ease of using mixed syntaxes::  

                    ItemKey :=    str  # string:  dict
                    ListIndex :=  int  # integer: lists, tuple, dict

            kargs:
                searchpath:
                    Optional search path for the match of the provided 
                    address *subpath*. The provided *subpath* is applied
                    to each node of the *searchpath* in accordance to the 
                    *direction* option. This provides the search and 
                    enumeration of side branches::

                        searchpath := <path-item-list> 

                        path-item-list := <path-item> [, <path-item-list>]
                        path-item := (
                              str  # item name 
                            | int  # item index
                        ) 

                        default := <top-node>

                    The search path entries has to be actually present by default.
                    These  could be either created by loading a complete tree
                    structure, or by using the *Capabilities.create()* member.
                    See also parameter 'strict'.

                direction:
                    The search direction of the *subpath* within the 
                    *searchpath*. In case of multiple superpositioned
                    attributes the first traversed match.

                    The provided values are::

                        direction := (
                              up   | 0  | False # search from right-to-left
                            | down | 1  | True  # search from left-to-right
                        )

                        default:= up

                match:
                    Sets the match criteria for the search operation.
                    Interferes with *direction*::

                        match := (
                              M_FIRST | 'first'   # use first matching node
                            | M_LAST  | 'last'    # use last matching node
                            | M_ALL   | 'all'     # use all - iterate all matches
                        )

                        default := M_FIRST

                partial:
                    Enables the return of partial sub paths in case the requested
                    path is not completely present. ::

                        partial := (
                              True   # when not completely present, the longest 
                                     # existing part is returned, the completeness
                                     # is provided by the result attribute <partial>
                            | False  # when not completely present an exception
                                     # is raised 
                        )

                strict:
                    Controls the required consistency. This comprises:

                    1. the presence of the search path entries

                    2. the presence of the requested subpath within the set
                       of search paths

                pysyn:
                    Activates full *Python* syntax. This in particular enables all
                    container types of intermediate nodes for arbitrary paths.
                    Includes *tuple*, *set*, *frozenset*, etc. ::

                        pysyn := (
                              True   # allows all python types as container nodes
                            | False  # allows list and dict only as container nodes
                        )

                        default := False

        Returns:
            In case of a match returns the tuple::

                return := (<attr-value-path>, <attr-value>, <partial>)

                attr-value-path := (
                      "the list of keys of the top-down path"
                    | "empty list when no item exists"        # see <complete>
                )
                attr-value := "value of the targeted node/attribute"
                partial := (
                      False   # the complete requested path
                    | True    # the actually present part of the path
                )

            Else raises *YapyDataDataTreeOidError*.

        Raises:
            YapyDataDataTreeOidError

            pass-through

        """
        _srch = kargs.get('searchpath', ())
        _dir = kargs.get('direction', 0)
        _match = kargs.get('match', DataTree.M_FIRST)
        _pysyn = kargs.get('pysyn')
        
        if not isinstance(_srch, (tuple, list,)):
            raise YapyDataDataTreeError(
                "search path requires 'tuple' or'list', got: "
                + str(_srch)
                ) 

        #
        # match criteria
        #
        try:
            _match = self.match_map[_match]
        except IndexError:
            try:
                _match = self.match_map[str(_match).lower()] 
            except KeyError:
                raise YapyDataDataTreeError(
                    "valid match are (first, %d, last, %d, all, %d,), got: %s" %(
                        DataTree.M_FIRST,
                        DataTree.M_LAST,
                        DataTree.M_ALL,
                        str(_match)
                    )
                )

        #
        # search direction
        #
        if _dir in (True, False,):
            pass
        else:
            _dir = str(_dir).lower()
            if _dir in ('up', '0',):
                _dir = False
            elif _dir in ('down', '1',):
                _dir = True
            else:
                raise YapyDataDataTreeError(
                    "valid directions are (up, 0, down, 1), got: "
                    + str(_dir)
                    ) 

        # collect the nodes on the searchpath
        _path_nodes = [self.data,]
        _cur = self.data
        if _srch:
            for x in _srch:
                try:
                    _cur = _cur[x]
                except (IndexError, KeyError, TypeError):
                    raise YapyDataDataTreeOidError(
                            "invalid search path: %s\n see: %s\n" %(
                                str(_srch),
                                str(x)
                            )
                        )
                _path_nodes.append(_cur)

        # revert for bottom-up search direction        
        if not _dir:
            # upward - up | 0 | False
            _path_nodes = reversed(_path_nodes)

        # now search the subpath for each node of the search path
        # first match wins
        for _pn in _path_nodes:
            _cur = _pn
            _idx_subpath = 0  # reset here
            for x in subpath:
                _excep = False
                try:
                    _cur = _cur[x]

                except (IndexError, KeyError,):
                    # a valid type - but missing value
                    # continue with next level - only when nodes do not fit
                    _cur = None
                    _excep = True
                    break
                
                except TypeError:
                    # not a valid data type
                    if _pysyn:
                        try:
                            _cur = getattr(_cur, x)

                        except TypeError:
                            if isinstance(_cur, set):
                                try:
                                    _cur=_cur & set([x])
                                    _cur = list(_cur)[0]

                                except:
                                    _cur = None
                                    _excep = True
                                    break

                        except AttributeError:
                            try:
                                _cur = _cur[int(x)]
                            
                            except Exception as e:  # for debug
                                _cur = None
                                _excep = True
                                break

                        except Exception as e:  # for debug
                            _cur = None
                            _excep = True
                            break
                    else:
                        # continue with next level - only when nodes do not fit
                        _cur = None
                        _excep = True
                        break

            if not _excep:
                break  # has hit a regular match

        if _excep:
            # no match - prefer a message with error hint here
            raise YapyDataDataTreeOidError(
                        '',
                        pathhook=str(subpath[_idx_subpath - 1]),
                        path=str(subpath),
                        searchpath=str(_srch),
                )

        return _cur

#     def __str__(self):
#         res = ''
#         return res


    def create(self, *subpath, **kargs):
        """Creates a *subpath* to a given node, default is from top.
        Reuses existing nodes, starts the creation at the first point
        of branch-out from the exiting tree.
        
        In general no padding of pre-required entries is done. This e.g.
        requires in case of a *list* the start with the index *0*, while
        in case of the *dict* arbitrary keys could be assigned.

        Args:
            subpath:
                The list of keys constituting a branch of a data tree.
                The *subpath* is treated as a branch of one of the nodes
                of a provided *searchpath* - which is by default the top node.
                The supported values are::

                    subpath := <list-of-node-ids>
                    <list-of-node-ids> := <node-id> [',' <list-of-node-ids>]
                    node-id := (
                          <present-intermediate-node>
                        | <new-node>
                    )
                    present-intermediate-node := (
                          str             # string:  dict
                        | int             # integer: lists, tuple, dict
                        | True | False    # logic:   dict
                        | None            # null:    dict
                    )
                    new-node := (
                          str             # string:  dict
                        | int             # integer: list
                        | True | False    # logic:   dict
                        | None            # null:    dict
                    )

                Some *Python* data types are immutable, which could be subscripted read-only,
                e.g. strings. While others such as sets are iterable, but not subscriptable
                at all. Refer to the manual for a detailed list.

            kargs:
                hook:
                    Optional node as parent of the insertion point for the new sub path.
                    The node must exist and be part of the targeted data structure. No 
                    additional checks are done::

                        hook := <memory-node>
                        memory-node := "node address"

                        default := <top-node>

                    The *hook* node could either be a border node of the existing tree,
                    or any arbitrary node with a partial of complete part of the requested
                    *subpath*. Existing nodes are reused.

                strict:
                    If *True* requires all present nodes of the *subpath* to of the
                    appropriate type, missing are created. When *False* present nodes
                    of inappropriate type are simply replaced. ::

                        strict := (
                              True   # nodes must be present
                            | False  # missing are created
                        )
                        default := False

                    Nodes of type *None* are always treated as non-present placeholder,
                    thus replaced in any case.

                value:
                    Value of the created final node::

                        value := <value-of-node>

                        value-of-node := <valid-json-node-type>
                        valid-json-node-type := (
                                              int | float
                                            | str                  # unicode
                                            | dict | list
                                            | None | True | False  # equivalent: null|true|false
                                            )

                        default := None

        Returns:
            In case of success the in-memory nodes of the sub path::

                return := (<attr-value-path>)

                attr-value-path-tuple := (
                      <in-memory nodes>
                    | <non-subscriptable-node>
                )
                in-memory nodes := (
                    "the list of in-memory nodes with support of subscription"
                )
                non-subscriptable-node := "any valid type"

            else raises *YapyDataDataTreeOidError*.

            The last node contains in case of an atomic type the value
            of the node, while the intermediate nodes represent the
            indexed containers.

        Raises:
            YapyDataDataTreeOidError

            pass-through

        """

        _strict = kargs.get('strict', False)
        _val = kargs.get('value', None)

        if not subpath and isinstance(subpath, (tuple,)):
            # no path supported at all - so it is a replacement value for self.data only
            self.data = _val
            return (self.data,)

        # collect the nodes on the search path
        # requires a stepwise lookahead, doing it recursive
        _last = None  # last successful container-node
        _hook = kargs.get('hook', self.data)  # the current insertion point
        _path_nodes = []
        _subpath = list(subpath)
        while _subpath:
            try:
                # iterate the present nodes
                _hook = _hook[_subpath[0]]
                _path_nodes.append(_hook)
                _last = _subpath.pop(0)  # store it for backlog of branch-out on non-container hook

            #
            # now work out and create missing nodes
            #
            except IndexError:
                # it is a new item in a list, so to be appended - sparse in not permitted/supported
                if _subpath[0] != len(_hook):
                    raise YapyDataDataTreeOidError(
                            '',
                            pathhook=str(_subpath[0]),
                            path=str(subpath),
                    )
                _k = _subpath.pop(0)

                # now build the new part
                _path_nodes.append(grow_branch(*_subpath, value=_val))
                _hook.append(_path_nodes[-1])
                return tuple(_path_nodes)
            
            except KeyError:
                # it is a new item in a 'dict' - just insert it
                # now build the new part
                _k = _subpath.pop(0)
                _node = grow_branch(*_subpath, value=_val)

                _hook[_k] = _node
                _path_nodes.append(_node)

                # add created subpaths for result vector
                for _kx in _subpath:
                    _path_nodes.append(_path_nodes[-1][_kx])

                return tuple(_path_nodes)

            except TypeError:
                # it is a new item, but not within a container,
                # so replaces if permitted for replacement,
                # check of valid condition by:
                #
                # - _strict==False - replace as required if valid
                # - None - placeholder for non-present
                #
                if _strict:
                    # at least one present node does not match required strict type-condition
                    # requires a container, got an atomic or non-indexable(set, ...)
                    raise YapyDataDataTreeOidError(
                        "invalid subpath: %s\n see: subpath[%s] = %s\n" %(
                            str(subpath),
                            str(subpath.index(_subpath[0])),  # for robustness...
                            str(_subpath[0])
                        )
                    )

                if _last == None:
                    # so it was the first attempt
                    #
                    # here the self.data is the first created node, thus included in the return
                    # can check it by id(<self-obj>.data) == id(<return-val>[0])
                    #
                    self.data = grow_branch(*_subpath, value=_val)

                    # add created subpaths for result vector
                    _k = _subpath.pop(0)
                    _path_nodes.append(self.data[_k])
                    for _kx in _subpath:
                        _path_nodes.append(_path_nodes[-1][_kx])
                    
                    return tuple(_path_nodes)


                #***
                #*** here we had a partial resolution with a trailing non-container node ***
                #*** the node-value is released for replacement by strict==False *** 
                #***

                # no container type fixed yet, 
                # so now add, and drop/replace the non-container node 
                _k = _subpath.pop(0)
                if isinstance(_k, int):
                    # key is 'int' so as defined the (default) container is a list
                    # 'int' keys of 'dict' are not supported for creation, while the read access is provided 
                    # so create them manually, use them as you like
                    if _k == 0:  # requires _k==0 because here it is the first
                        raise YapyDataDataTreeOidError(
                            "invalid subpath inital index range for new 'list': %s\n see: subpath[%s] = %s\n" %(
                                str(subpath),
                                str(subpath.index(_k)),  # for robustness...
                                str(_k)
                            )
                        )

                    _path_nodes[-1] = _path_nodes[-2][_last] = [ grow_branch(*_subpath, value=_val), ]
                    return tuple(_path_nodes)

                elif isinstance(_k, ISSTR):
                    # this basically should never fail - as long as '_k' is immutable...
                    # so for now want the eventual exception including it's stack...  
                    if _path_nodes:
                        if len(_path_nodes) >1:
                            _path_nodes[-1] = _path_nodes[-2][_last] = { _k: grow_branch(*_subpath, value=_val)}
                            _path_nodes.append(_path_nodes[-1][_k])

                            # add created subpaths for result vector
                            for _kx in _subpath:
                                _path_nodes.append(_path_nodes[-1][_kx])

                        else:  # ==1
                            self.data[_last] = {_k: grow_branch(*_subpath, value=_val)}
                            _path_nodes[-1] = self.data[_last]
                            _path_nodes.append(self.data[_last][_k])

                    else:
                        self.data = {_k: grow_branch(*_subpath, value=_val)}
                        _path_nodes.append(self.data)

                    return tuple(_path_nodes)

                else:
                    raise YapyDataDataTreeOidError(
                        "invalid subpath key/index type: %s\n see: subpath[%s] = %s\n" %(
                            str(subpath),
                            str(subpath.index(_k)),  # for robustness...
                            str(_k)
                        )
                    )

        #
        # here we did not had any exception, that means the path is present, 
        # now let us check the value of the last item
        #
        try:
            _path_nodes[-1] = _val
            _path_nodes[-2][_last] = _val
        except:
            _path_nodes[-1] = self.data = _val
        
        return tuple(_path_nodes)

    def get(self, *path):
        """Gets the value of the path within the member 'data'::

            self.data[key]
            self.data[key0][key1][key2]...
            
        
        Args:
            key:
                The value of the node within *data*::

                    key := (
                          <single-key>
                        | <list-of-keys>
                        | <tuple-of-keys>
                    )
                    single-key := <key>
                    list-of-keys := '[' <keylists> ']'
                    tuple-of-keys := '(' <keylist> ')'
                    keylist := <key> [',' <keylist>]
                    key := (
                          ItemKey
                        | ListIndex
                    )
                    ItemKey := "valid dict-key"
                    ListIndex := "valid list-index"

        Returns:
            The value of the addressed node/value.

        Raises:
            pass-through

        """
        """Gets the value of the path within the member 'data'::

            self.data[nodeid]
            self.data[nodeid0][nodeid1][nodeid2]...

        When fails, a final trial is given to *list* and *dict* classes
        including mixins::

            self[nodeid]

        When finally still missing at all, an exception is raised.

        Args:
            nodeid:
                The value of the node within *data*::

                    nodeid := (
                          <single-nodeid>
                        | <list-of-nodeids>
                        | <tuple-of-nodeids>
                    )
                    single-nodeid := <nodeid>
                    list-of-nodeids := '[' <nodeidlists> ']'
                    tuple-of-nodeids := '(' <nodeidlists> ')'
                    nodeidlists := <nodeid> [',' <nodeidlists>]
                    nodeid := (
                          ItemKey
                        | ListIndex
                    )
                    ItemKey := "valid dict-key"
                    ListIndex := "valid list-index"

                The derived syntax classes may impose specific constraints.
                Thus it is recommended to use integers and strings only
                for maximum compatibility, and the ease of using mixed syntaxes::  

                    ItemKey :=    str  # string:  dict
                    ListIndex :=  int  # integer: lists, tuple, dict

        Returns:
            The value of the addressed node/value.

        Raises:
            pass-through

        """
        try:
            return self(*path)
        except:
            return None

    def import_data(self, fpname, key=None, node=None, **kargs):
        """The core class *DataTree *does not support serialization.
        
        For serialization use either a derived syntax class, or 
        serialize it e..g. by pickling and use the in-memory data.
        For example by pickling:: 

            def import_data(self, fpname, key=None, node=None, **kargs):
                if not os.path.isfile(fpname):
                    if not os.path.isfile(fpname + '.pkl'):
                        raise YapyDataTreeError(
                            "Missing file: " + str(fpname))
                    else:
                        fpname = fpname + '.pkl'
                 
                if key and node == None:
                    raise YapyDataTreeError(
                        "Given key(%s) requires a valid node." % (str(key)))
                 
                datafile = os.path.abspath(fpname)
                with open(datafile, 'rb') as data_file:
                    pval = pickle.load(data_file)
                 
                if key:
                    node[key] = pval
                else:
                    self.data = pval
                 
                return pval

            See manuals for security issues of pickling.

        """
        raise NotImplementedError(
            """Use a derived syntax class, or serialize by pickler."""
            )

    def join(self, data, keyidx=None, hook=None):
        """Superposes a JSON structure onto an existing. This
        is a fixed mode and strategy special case of the generic
        method *superpose()*. Implemented by recursion. The reduced
        parameter set provides better performance on large trees
        while the graph parameters still could be efficiently set
        by default values.
        
        The superpositioning is supported by multiple strategies
        defined by the parameter *mode*. The provided algorithm
        of the strategy is *join*, where the input data is processed
        on the exisiting tree by modification and creation as required.

        * branches are resolved from top to the leafs 
        * missing sub-branches are created
        * missing leafs are created
        * existing leafs are replaced

        This implements a last-wins strategy, thus in particular supports
        incremental load of configurations by raising priority.

        Args:
            data:
                Top node of the data tree to be superposed.

            keyidx:
                Key or index to be used at the insertion node. 
                If not given the insertion node is::
                
                    into dict: update by the new node
                    into list: append the new node

                    default := None 

            hook:
                The insertion node for the new data:: 

                    when  not given: use top. 

                    default := None 

        Returns:
            Returns the merged data tree,
            raises an exception in case of failure.

        Raises:
            YapyDataDataTreeError

            pass-through

        """
        if not data:
            return

        if not hook:
            hook=self.data

        if isinstance(hook, dict):
            
            if isinstance(data, (int, float,)) or isinstance(data, ISSTR):  # data is atom
                if not keyidx:
                    raise YapyDataDataTreeError(
                        "update dict item(%s) requires key" % (str(type(data)))
                        )
                
                hook[keyidx] = data

            elif isinstance(data, dict):  # data is dict
                try:
                    _hookx = hook[keyidx]
                except KeyError:
                    _hookx = hook

                if isinstance(_hookx, dict):
                    # will use itself - including keys - for update
                    for k,v in data.items():
                         
                        if _hookx.get(k):
                            # replace an existing sub-tree
                            self.join(v, k, _hookx)
                        else:
                            # add a new subtree
                            _hookx[k] = v

                elif isinstance(_hookx, list):

                    if keyidx == None:
                        raise YapyDataDataTreeOidError(
                                "Insertion into list requires index, got: " + str(keyidx)
                            )

                    elif isinstance(keyidx,ISSTR):
                        try:
                            hook[keyidx] = data
                        except KeyError:
                            raise YapyDataDataTreeOidError(
                                    "Insertion into or replacement of list failed: %s" % (
                                            str(keyidx),
                                        )
                                )
                        hook[keyidx] = data

                    else:
                        self.join(data, keyidx, hook)

            else:  # data is list or atom
                if not keyidx:  # requires a key
                    raise YapyDataDataTreeError(
                        "cannot update dict with %s" % (str(type(data)))
                        )

                else:
                    if not hook.get(keyidx):
                        # a new branch - yust add it
                        hook[keyidx] = data

                    elif type(hook.get(keyidx)) != type(data):
                        # icompatible types - for now replace
                        hook[keyidx] = data

                    else:
                        # superpose existing by leafs, missing by branches and/or leafs
                        _hookx = hook[keyidx] 
                        for i in range(len(data)):
                            if i < len(_hookx):
                                # superpose an existing sub-tree
                                self.join(data[i], i, _hookx)
                            elif i == len(_hookx):
                                # add a new subtree
                                _hookx.append(data[i])
                            else:
                                # add a new subtree
                                raise YapyDataDataTreeOidError(
                                        "index(%s) out of range(%s). " % (
                                            str(i),
                                            str(len(_hookx)),
                                        )
                                    )
                
        elif isinstance(hook, list):
            if keyidx == None or keyidx == len(hook):
                # so fill incrementally by default
                hook.append(data)
            
            elif keyidx > len(hook):
                # no sparse lists suported
                raise YapyDataDataTreeOidError(
                        "Insertion index(%s) out of range(%s). " % (
                            str(len(hook)),
                            str(keyidx),
                        )
                    )
            elif (
                    isinstance(data, (int, float,)) or isinstance(data, ISSTR)  # data is atom
                    or not isinstance(hook[keyidx], (dict, list,))  # target is atom
                ):
                if keyidx == None:
                    raise YapyDataDataTreeError(
                        "update dict item(%s) requires key" % (str(type(data)))
                        )
                
                hook[keyidx] = data

            else:
                # superpose an existing item
                self.join(data, keyidx, hook)
        
        return

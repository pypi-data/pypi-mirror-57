# -*- coding: utf-8 -*-

"""
file: graph_mixin.py

Defines an abstract base class for node and edge tool classes that are used for
dynamic (ORM based) Graph class creation.
Node and Edge tools are used (sub)graphs containing a single node or single edge
respectively.
"""

import abc

from graphit.graph_py2to3 import to_unicode
from graphit.graph_helpers import make_edges


__all__ = ['NodeTools', 'EdgeTools']


class NodeEdgeToolsBaseClass(object):
    """
    Abstract Base class for node specific tools operating on node data in single
    node graphs.
    """
    __metaclass__ = abc.ABCMeta
    __isnetbc__ = True

    def __call__(self):
        """
        Implement class __call__

        :return: default value using value_tag
        """

        return self.get()

    @abc.abstractmethod
    def __contains__(self, key):
        """
        Check if node/edge dictionary contains key

        :param key: key to check

        :rtype:     :py:bool
        """

        return False

    def __getattr__(self, key):
        """
        Implement class __getattr__

        Expose node or edge dictionary keys as class attributes.
        Called after the default __getattribute__ lookup it will raise a
        AttributeError if the attribute was not found.
        If the key is present, the `get` method is called for it's value.

        :param key: attribute name
        :return:    attribute value
        """

        if key not in self.__slots__:
            value = self.get(key=key, default='_Graph_no_key__')
            if value == '_Graph_no_key__':
                raise AttributeError('No such node or edge attribute: {0}'.format(key))

            return value

        return object.__getattribute__(self, key)

    def __getitem__(self, key):
        """
        Implement class __getitem__

        Return node or edge attributes by dictionary lookup
        It will raise a GraphitException if the attribute was not found, else
        the `get` method is called for it's value.

        :param key: attribute name
        :return:    attribute value
        """

        value = self.get(key=key, default='_Graph_no_key__')
        if value == '_Graph_no_key__':
            raise KeyError('No such node or edge attribute: {0}'.format(key))

        return value

    def __setattr__(self, key, value):
        """
        Implement class __setattr__

        Setattr method for Graph classes that resolves attribute assignment in
        the following order:

        1 Class attributes defined by __slots__. Graph objects do not allow for
          additional attributes not defined in __slots__ to be assigned on the
          class.
        2 Graph setter handled by property methods
        3 Any attribute not assigned by step 1 or 2 is considered a node or
          edge attribute and will be set by the respective storage driver
        4 None of the above will raise an AttributeError. __setattr__ doe not
          support assignment of new attributes to nodes or edges. Use the 'set'
          or __setitem__ methods instead.

        :param key:  attribute name.
        :param value: attribute value
        """

        propobj = getattr(self.__class__, key, None)

        if key in self.__slots__:
            return dict.__setattr__(self, key, value)
        elif isinstance(propobj, property) and propobj.fset:
            propobj.fset(self, value)
        elif key in self:
            self.set(key, value)
        else:
            raise AttributeError('Graph object does not support attribute assignment for: {0}'.format(key))

    def __setitem__(self, key, value):
        """
        Implement class __setitem__

        Set node or adge attributes using dictionary style attribute access in
        the following order:

        1 Graph setter handled by property methods
        2 Any attribute not assigned by step 1 is considered a node or
          edge attribute and will be set by the respective storage driver

        :param key:   attribute name
        :type key:    str
        :param value: attribute value
        """

        propobj = getattr(self.__class__, key, None)

        if isinstance(propobj, property) and propobj.fset:
            propobj.fset(self, value)
        else:
            self.set(key, value)

    @abc.abstractmethod
    def get(self, key=None, default=None, defaultattr=None):
        """
        Return node/edge value

        Implement to provide direct access to a node or edge key/value pair
        preferably by using the `get` method of the node/edge storage API.
        The method can be used to manipulate data in the model before returning
        it to the user.

        The method is also used by all format import and export functions to
        get and set (using `set` method) the data from and set to a specific
        format respectively. The graph classes therefor do not have separate
        serializer methods but instead use different get methods to serialize
        the data.

        :param key:         node value attribute name. If not defined then
                            attempt to use class wide `value_tag` attribute.
        :type key:          mixed
        :param defaultattr: node or edge value attribute to use as source of
                            default data when `key` attribute is not present.
        :type defaultattr:  mixed
        :param default:     value to return when all fails
        :type default:      mixed
        """

        return

    def new(self, **kwargs):
        """
        Custom initiation method for new nodes or edges

        Called once by the add_node or add_edge method to allow custom classes
        to perform any initiation on the newly created node or edge
        """

        return

    @abc.abstractmethod
    def nid(self):
        """
        Property returning the current node or edge ID.

        This should return a single value as this property should only be
        implemented on graphs having a single node or edge
        """

        return

    @abc.abstractmethod
    def set(self, key, value, **kwargs):
        """
        Set node/edge key/value pair

        Implement to provide a direct setter for node or edge key/value pairs
        preferably by using the `set` method of the node/edge storage API.

        :param key:         node/edge key to set
        :param value:       node/edge value
        """

        return

    def validate(self, key=None):
        """
        Validate the current node

        Contains validation code for the data represented by the node.

        :param key: key of specific key/value pair to validate
        :type key:  :py:str

        :return:    validation success
        :rtype:     :py:bool
        """

        return True

    def update(self, data):
        """
        Python dict-like update method for node or edge data

        :param data: source dictionary
        :type data:  :py:dict
        """

        if not isinstance(data, dict):
            raise AssertionError('Dictionary required')

        for key, value in data.items():
            self.set(key, value)


class NodeTools(NodeEdgeToolsBaseClass):
    """
    Node specific tools
    """

    def __contains__(self, key):
        """
        Check if node/edge dictionary contains key

        :param key: key to check

        :rtype:     :py:bool
        """

        nid = self.nid
        if nid:
            return key in self.nodes[self.nid]
        return False

    def __repr__(self):
        """
        Implement class __repr__

        String representation of the node class.

        :rtype: :py:str
        """

        data = self.nodes.get(self.nid, {})
        return '<{0} "{1}" node object {2}, id {3}: {4} nodes, {5} edges>'.format(
            type(self).__name__,
            data.get(self.data.key_tag, ''),
            id(self),
            data.get('_id', '-'),
            len(self.nodes),
            len(self.edges)
        )

    @property
    def isleaf(self):
        """
        Check if the current selected node is a leaf node.

        :rtype: bool
        """

        return len(self.origin.adjacency.get(self.nid, [])) <= 1

    @property
    def nid(self):
        """
        Return the nid of the current selected node.

        :return: node nid
        """

        if len(self.nodes) == 1:
            return list(self.nodes.keys())[0]

        return None

    def add_connect(self, node=None, node_kwargs=None, edge_kwargs=None):
        """
        Convenient method to connect a new node to the present node.

        Combined the add_node and add_edge functionality in one method

        :param node:        node to add
        :type node:         any hashable object
        :param node_kwargs: keyword arguments for the add_node method
        :type node_kwargs:  :py:dict
        :param edge_kwargs: keyword arguments for the add_edge method
        :type edge_kwargs:  :py:dict

        :return:            node ID (nid)
        :rtype:             py:int
        """

        node_kwargs = node_kwargs or {}
        edge_kwargs = edge_kwargs or {}

        nid = self.origin.add_node(node=node, **node_kwargs)
        self.origin.add_edge(self.nid, nid, **edge_kwargs)

        return nid

    def connected_edges(self):
        """
        Return the connected edges to a node

        :return: connected edges
        :rtype:  list
        """

        if self.masked:
            return [edge for edge in self.edges if self.nid in edge]
        return [edge for edge in self.origin.edges if self.nid in edge]

    def get(self, key=None, default=None, defaultattr=None):
        """
        Return node value

        Get direct access to relevant node attributes. If `key` is not defined
        the method returns the value of the default value_tag which is
        equivalent to returning the value for a dictionary key where the key
        is either the nid or the key_tag attribute.

        :param key:         node value attribute name. If not defined then
                            attempt to use class wide `value_tag` attribute.
        :type key:          mixed
        :param defaultattr: node or edge value attribute to use as source of
                            default data when `key` attribute is not present.
        :type defaultattr:  mixed
        :param default:     value to return when all fails
        :type default:      mixed
        """

        # If empty return default
        if self.empty():
            return default

        # Get node attributes
        target = self.nodes[self.nid]

        key = key or self.data.value_tag
        if key in target:
            return target[key]
        return target.get(defaultattr, default)

    def set(self, key, value=None):
        """
        Set node attribute values.

        :param key:   node attribute key
        :param value: node attribute value
        """

        self.nodes[self.nid][to_unicode(key)] = to_unicode(value)


class EdgeTools(NodeEdgeToolsBaseClass):
    """
    Edge specific tools
    """

    def __contains__(self, key):
        """
        Check if node/edge dictionary contains key

        :param key: key to check

        :rtype:     :py:bool
        """

        nid = self.nid
        if nid:
            return key in self.edges[self.nid]
        return False

    def __repr__(self):
        """
        Implement class __repr__

        String representation of the edge class.

        :rtype: :py:str
        """

        data = self.edges.get(self.nid, {})
        return '<{0} "{1}" edge object {2}, id {3}: {4} nodes, {5} edges>'.format(
            type(self).__name__,
            data.get(self.data.key_tag, ''),
            id(self),
            self.nid,
            len(self.nodes),
            len(self.edges)
        )

    @property
    def is_directed(self):
        """
        Determine if edge is directed based

        An edge is undirected if both edges of a pair pointing in opposite
        directions are present.

        :rtype: :py:bool
        """

        edges = make_edges(self.nid, directed=False)
        return not all([edge in self.origin.edges for edge in edges])

    @property
    def nid(self):
        """
        Return the eid of the current selected edge.

        :return: edge eid
        """

        if len(self.edges) == 1:
            return list(self.edges.keys())[0]

        return None

    def get(self, key=None, default=None, defaultattr=None):
        """
        Return edge value

        Used by the `value` method to get direct access to relevant node or
        edge attributes. The `value` method itself is a placeholder method
        that can be overloaded by custom classes to post process the data
        before returning it.

        :param key:         node or edge value attribute name. If not defined
                            then attempt to use class wide `key_tag`
                            attribute.
        :type key:          mixed
        :param defaultattr: node or edge value attribute to use as source of
                            default data when `key` attribute is not present.
        :type defaultattr:  mixed
        :param default:     value to return when all fails
        :type default:      mixed
        """

        # Get edge attributes
        target = self.edges[self.nid]

        key = key or self.data.value_tag
        if key in target:
            return target[key]

        if defaultattr:
            return target.get(defaultattr, default)
        return default

    def set(self, key, value, **kwargs):
        """
        Set edge attribute values.
        The method may be overloaded in custom classes to pre-process data
        before setting.

        :param key:   edge attribute key
        :param value: edge attribute value
        """

        self.edges[self.nid][to_unicode(key)] = to_unicode(value)

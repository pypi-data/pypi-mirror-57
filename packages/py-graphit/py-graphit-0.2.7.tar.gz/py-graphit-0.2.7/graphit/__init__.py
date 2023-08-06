# -*- coding: utf-8 -*-

"""
#Graph module

###Basic graph structure
A graph represented by a Graph class is an object that stores nodes, edges and
adjacency information in seperate DictStorage classes. A DictStorage class is a
subclass of the standard Python dictionary and collections MutableMappings
Abstract Base Class (ABC).

The nodes and edges DictStorage objects store node and edge attributes respectivly
based on the node ID (nid).
The graph DictStorage object stores node adjacency and is the primary store for
the graph topology.

###Node ID
The node ID or nid for short is the unique identifier of a node and derived edges
in the graph. The nid itself can be any hasable object except None. Set auto_nid
to True in the graph to ensure all added nodes are automatically assigned a unique
auto incremented integer ID.

###Graph directionality
A graph is undirected by default storing an two edges for every connected node,
one in each direction.
Change the graph directed attribute to True will ensure that every every newly
added edge is directed. Directed and undirected edges can be mixed in the same
graph.

###Graph query and iteration
The graph module has a rich palet of functions to query and analyze graphs.
For performance reasons, most of these will return node or edge IDs. New Graph
object representing a node and/or edge selection can returned using one of the
following Graph methods:

* getnodes: return subgraph based on one or more nodes
* getedges: return subgraph based on one or more edges
* iternodes: iterate over nodes in the graph. Uses getnodes
* iteredges: iterate over edges in the graph. Uses getedges
* query_nodes: return subgraph based on a query over node attributes
* query_edges: return subgraph based on a query over edge attributes

The subgraphs returned by these methods are implemented as a dictionary view over
the keys in the nodes and edges DictStorage objects.
By default this means that the subgraphs are fully isolated from the parent graph.
Returning a single node using getnodes will have no neighbors.
This may not be desirable in circumstances where you want a view over nodes but
retain connectivity with nodes outside of the view. This behaviour is enabled by
switching the Graph masked to False.
"""

import os

__module__ = 'graphit'
__docformat__ = 'restructuredtext'
__version__ = (0, 2, 7)
__author__ = 'Marc van Dijk'
__status__ = 'release v1'
__date__ = '15 april 2016'
__licence__ = 'Apache Software License 2.0'
__url__ = 'https://py-graphit.github.io'
__copyright__ = '{0}, VU University, Amsterdam'.format(__author__)
__rootpath__ = os.path.dirname(__file__)


# Functions defined at package initiation to prevent circular import problems
def check_graphbase_instance(*args, **kwargs):
    """
    Validate if all objects in `args` are instances of the GraphBase class

    :param exception: raise exception if check failed
    :type exception:  :py:bool
    :param args:      Arguments to check

    :return:          True if validation successful
    :rtype:           :py:bool
    :raises:          AttributeError if validation fails
    """

    # Validate arguments, should be Graph instance
    if not all([isinstance(graph, Graph) for graph in args]):
        if kwargs.get('exception', True):
            raise AttributeError('All arguments need be of type Graph')
        return False

    return True


def check_graphaxis_instance(*args, **kwargs):
    """
    Validate if all objects in `args` are instances of the GraphAxis class

    :param exception: raise exception if check failed
    :type exception:  :py:bool
    :param args:      Arguments to check

    :return:          True if validation successful
    :rtype:           :py:bool
    :raises:          AttributeError if validation fails
    """

    # Validate arguments, should be GraphAxis instance
    if not all([isinstance(graph, GraphAxis) for graph in args]):
        if kwargs.get('exception', True):
            raise AttributeError('All arguments need be of type Graph')
        return False

    return True


def version(digits=3):
    """
    Return a string representation of the graphit __version__

    Graphit version follows the  semantic versioning guidelines formatted as

    <major version int>.<minor version int>.<micro version int>

    The full version string is returned by default but number of significant
    version digits can be set using the `digits` argument.

    :param digits: number of digits to format version string
    :type digits:  :py:int

    :rtype: :py:str
    """

    if digits > len(__version__):
        digits = len(__version__)

    return '.'.join([str(__version__[i]) for i in range(digits)])


# Component imports
from .graph import GraphBase as Graph
from .graph_axis.graph_axis_class import GraphAxis


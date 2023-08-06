# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2018
# Author:  Marc van Dijk (marcvdijk@gmail.com)
# file: io_tgf_format.py

"""
Functions for reading and writing graphs defined in Trivial Graph Format (.tgf)
a simple text-based file format for describing graphs. It consists of a list of
node definitions, which map node IDs to labels, followed by a list of edges,
which specify node pairs and an optional edge label. Node IDs can be arbitrary
identifiers, whereas labels for both nodes and edges are plain strings.

The graph may be interpreted as a directed or undirected graph.
For directed graphs, to specify the concept of bi-directionality in an edge,
one may either specify two edges (forward and back) or differentiate the edge
by means of a label.

TGF format only described the nodes themselves and edges connecting them.
Node data (attributes) are not represented.

Example:
    1 January
    2 March
    3 April
    4 May
    5 December
    6 June
    7 September
    #
    1 2
    3 2
    4 3
    5 1 Happy New Year!
    5 3 April Fools Day
    6 3
    6 1
    7 5
    7 6
    7 1

Reference: https://en.wikipedia.org/wiki/Trivial_Graph_Format
"""

from graphit import Graph
from graphit.graph_exceptions import GraphitException
from graphit.graph_py2to3 import StringIO
from graphit.graph_io.io_helpers import coarse_type, open_anything

__all__ = ['read_tgf', 'write_tgf']


def read_tgf(tgf, graph=None):
    """
    Read graph in Trivial Graph Format

    TGF format dictates that nodes to be listed in the file first with each
    node on a new line. A '#' character signals the end of the node list and
    the start of the edge list.

    Node and edge ID's can be integers, float or strings. They are parsed
    automatically to their most likely format.
    Simple node and edge labels are supported in TGF as all characters that
    follow the node or edge ID's. They are parsed and stored in the Graph
    node and edge data stores using the graphs default or custom 'key_tag'.

    TGF data is imported into a default Graph object if no custom Graph
    instance is provided. The graph behaviour and the data import process is
    influenced and can be controlled using a (custom) Graph class.

    .. note:: TGF format always defines edges in a directed fashion.
              This is enforced even for custom graphs.

    :param tgf:             TGF graph data.
    :type tgf:              File, string, stream or URL
    :param graph:           Graph object to import TGF data in
    :type graph:            :graphit:Graph

    :return:                Graph object
    :rtype:                 :graphit:Graph
    """

    tgf_file = open_anything(tgf)

    if graph is None:
        graph = Graph()
    elif not isinstance(graph, Graph):
        raise GraphitException('Unsupported graph type {0}'.format(type(graph)))

    # TGF defines edges in a directed fashion. Enforce but restore later
    default_directionality = graph.directed
    graph.directed = True

    # TGF node and edge labels are unique, turn off auto_nid
    graph.data['auto_nid'] = False

    # Start parsing. First extract nodes
    nodes = True
    node_dict = {}
    for line in tgf_file.readlines():

        line = line.strip()
        if len(line):

            # Reading '#' character means switching from node
            # definition to edges
            if line.startswith('#'):
                nodes = False
                continue

            # Coarse string to types
            line = [coarse_type(n) for n in line.split()]

            # Parse nodes
            if nodes:

                attr = {}
                # Has node data
                if len(line) > 1:
                    attr = {graph.data.key_tag: ' '.join(line[1:])}
                nid = graph.add_node(line[0], **attr)
                node_dict[line[0]] = nid

            # Parse edges
            else:
                e1 = node_dict[line[0]]
                e2 = node_dict[line[1]]

                attr = {}
                # Has edge data
                if len(line) > 2:
                    attr = {graph.data.key_tag: ' '.join(line[2:])}
                graph.add_edge(e1, e2, **attr)

    tgf_file.close()

    # Restore directionality
    graph.directed = default_directionality

    return graph


def write_tgf(graph):
    """
    Export a graph in Trivial Graph Format

    .. note::for
    TGF graph export uses the Graph iternodes and iteredges methods to retrieve
    nodes and edges and 'get' the data labels. The behaviour of this process is
    determined by the single node/edge mixin classes and the ORM mapper.

    :param graph:         Graph object to export
    :type graph:          :graphit:Graph

    :return:              TGF graph representation
    :rtype:               :py:str
    """

    # Define node and edge data tags to export
    key_tag = graph.data.key_tag

    # Create empty file buffer
    string_buffer = StringIO()

    # Export nodes
    for node in graph.iternodes():
        string_buffer.write('{0} {1}\n'.format(node.nid, node.get(key_tag, default='')))

    # Export edges
    string_buffer.write('#\n')
    for edge in graph.iteredges():
        e1, e2 = edge.nid
        string_buffer.write('{0} {1} {2}\n'.format(e1, e2, edge.get(key_tag, default='')))

    # Reset buffer cursor
    string_buffer.seek(0)
    return string_buffer.read()

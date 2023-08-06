# -*- coding: utf-8 -*-

import copy
import logging

from graphit import __module__
from graphit.graph_exceptions import GraphitNodeNotFound

logger = logging.getLogger(__module__)


def share_common_origin(*args):
    """
    Check if (sub)graphs share the same origin graph based
    on object id.

    :param args: list of graphs
    :rtype:      :py:bool
    """

    return len(set([id(graph.origin) for graph in args])) == 1


def edges_between_nodes(graph, nodes):
    """
    Return all edges in graph that connect the nodes

    :param graph:
    :param nodes:
    :return:
    """

    edge_selection = []
    # TODO: graph.origin or graph
    for edge in graph.origin.edges:
        if edge[0] in nodes and edge[1] in nodes:
            edge_selection.append(edge)

    return edge_selection


def adjacency_to_edges(nodes, adjacency, node_source):
    """
    Construct edges for nodes based on adjacency.

    Edges are created for every node in `nodes` based on the neighbors of
    the node in adjacency if the neighbor node is also in `node_source`.
    The source of adjacency information would normally be self.graph and
    self.nodes for `node_source`. However, `node_source may` also equal
    `nodes` to return edges for the isolated graph.

    :param nodes:       nodes to return edges for
    :type nodes:        list
    :param adjacency:   node adjacency (self.graph)
    :type adjacency:    dict
    :param node_source: other nodes to consider when creating edges
    :type node_source:  list
    """

    edges = []
    for node in nodes:
        edges.extend([tuple([node, e]) for e in adjacency[node] if e in node_source])

    return edges


def edge_list_to_adjacency(edges):
    """
    Create adjacency dictionary based on a list of edges

    :param edges: edges to create adjacency for
    :type edges:  :py:list

    :rtype:       :py:dict
    """

    adjacency = dict([(n, []) for n in edge_list_to_nodes(edges)])
    for edge in edges:
        adjacency[edge[0]].append(edge[1])

    return adjacency


def edge_list_to_nodes(edges):
    """
    Create a list of nodes from a list of edges

    :param edges: edges to create nodes for
    :type edges:  list
    """

    return list(set(sum(edges, ())))


def make_undirected_edges(edges):
    """
    Complete a list of (directed) edges with their undirected equivalent

    :param edges:
    :return:
    """

    reverse = [edge[::-1] for edge in edges]
    return set(edges + reverse)


def make_edges(nodes, directed=True):
    """
    Create an edge tuple from two nodes either directed
    (first to second) or undirected (two edges, both ways).

    :param nodes:    nodes to create edges for
    :type nodes:     :py:list, py:tuple
    :param directed: create directed edge or not
    :type directed:  bool
    """

    edges = [tuple(nodes)]
    if not directed:
        edges.append(nodes[::-1])

    return edges


def group_edge_pairs(edges):
    """
    Group pairs of forward and reverse edges between nodes as tuples in a
    list together with single directed edges if any

    :param edges:   list of edges
    :type edges:    :py:list

    :return:        paired edges
    :rtype:         :py:list
    """

    pairs = []
    done = []
    for e in edges:

        if e in done:
            continue

        reverse_e = e[::-1]
        if reverse_e in edges:
            pairs.append((e, reverse_e))
            done.append(reverse_e)
        else:
            pairs.append(e)
        done.append(e)

    return pairs


def renumber_id(graph, start):
    """
    Renumber all node ID's in the graph from a new start ID and adjust edges
    accordingly. Useful when duplicating a graph substructure.
    If the graph uses auto_nid, the node nid is also changed.

    #TODO: this one failes if run on a subgraph. Probably need to make changes
    #to nids in place instead of registering new storage

    :param graph:   Graph object to renumber
    :type graph:    Graph object
    :param start:   New start number to renumber from
    :type start:    :py:int
    :return:        Renumber graph and mapping of old to new ID
    :rtype:         Graph object, :py:dict
    """

    start = copy.copy(start)
    mapper = {}
    for nid in sorted(graph.nodes.keys()):
        mapper[graph.nodes[nid]['_id']] = start

        # Renumber
        graph.nodes[nid]['_id'] = start
        start += 1

    # Update root and auto_nid
    graph.data['nodeid'] = start
    if graph.root:
        graph.root = mapper[graph.root]

    # Update nid if auto_nid
    newnodes = {}
    if graph.data.auto_nid:
        newnodes = {v: graph.nodes[k] for k, v in mapper.items()}

    # Update edges.
    newedges = {}
    for eid, edge in graph.edges.items():
        newedges[(mapper.get(eid[0], eid[0]), mapper.get(eid[1], eid[1]))] = edge

    graph.nodes, graph.edges, graph.adjacency, graph.data = graph.storagedriver(newnodes, newedges, graph.data)

    return graph, mapper


def graph_directionality(graph, has_data_reference=True):
    """
    Return a graph overall directionality as 'directional', 'undirectional'
    or 'mixed' based on node adjacency.

    * undirected:  forward and reverse edges exists between every node
    * directional: edges between nodes are one directional only
    * mixed:       a mix of undirected and directed edges

    Graphit represent edges in an undirected graph as linked pairs of
    forward and reversed edges. That means that strictly considering the
    existence of a pair of bidirectional edges between nodes or their
    adjacency equivalent is not a unique identifier of directionality in
    graphit.
    This is resolved by checking for linked edges to identify a graphit graph
    as truly undirectional. This check can be disabled using the
    `has_data_reference` attribute.

    :param graph:               Graph to asses directionality of
    :type graph:                :graphit:Graph
    :param has_data_reference:  Check for linked edges
    :type has_data_reference:   :py:bool

    :return:      'directional', 'undirectional' or 'mixed'
    :rtype:       :py:str
    """

    edge_directionality = []
    for node, adj in graph.adjacency.items():
        edge_directionality.extend([node in graph.adjacency[n] for n in adj])

    if all(edge_directionality):

        # check for linked edges
        if has_data_reference:
            pairs = []
            for edge in graph.edges:
                linked_edge = graph.edges.get_data_reference(edge)
                if linked_edge:
                    pairs.append(edge)
                    pairs.append(linked_edge)

            if len(pairs) == len(graph.edges):
                return 'undirectional'
            elif not len(pairs):
                return 'directional'
            else:
                return 'mixed'

        return 'undirectional'
    elif any(edge_directionality):
        return 'mixed'
    else:
        return 'directional'


def check_nodes_in_graph(graph, nodes):
    """
    Validate if nodes are in graph

    :param graph: graph that should contain nodes
    :type graph:  :graphit:GraphBase
    :param nodes: nodes to check
    :type nodes:  :py:list

    :return:      True if validation successful
    :rtype:       :py:bool
    :raises       GraphitNodeNotFound
    """

    nodes_not_present = [nid for nid in nodes if nid not in graph.nodes.keys()]
    if nodes_not_present:
        raise GraphitNodeNotFound('Nodes not in graph: {0}'.format(repr(nodes_not_present).strip('[]')))

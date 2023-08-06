# -*- coding: utf-8 -*-

"""
file: module_axis_test.py

Unit tests for the Graph axis methods
"""

import os
from tests.module.unittest_baseclass import UnittestPythonCompatibility

from graphit.graph_exceptions import GraphitException
from graphit.graph_io.io_jgf_format import read_jgf
from graphit.graph_axis.graph_axis_methods import (node_children, node_parent, node_all_parents, node_neighbors,
                                                   node_ancestors, node_descendants, node_leaves, node_siblings)
from graphit.graph_axis.graph_axis_mixin import NodeAxisTools


class GraphAxisChildrenTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertItemsEqual(node_children(self.graph, 5, self.graph.root), [])
        self.assertItemsEqual(node_children(self.graph, 3, self.graph.root), [4, 5, 6, 7])
        self.assertItemsEqual(node_children(self.graph, 9, self.graph.root), [10])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.children(5).nodes.keys(), [])
        self.assertItemsEqual(self.graph.children(3).nodes.keys(), [4, 5, 6, 7])
        self.assertItemsEqual(self.graph.children(9).nodes.keys(), [10])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.children(5, return_nids=True), [])
        self.assertItemsEqual(self.graph.children(3, return_nids=True), [4, 5, 6, 7])
        self.assertItemsEqual(self.graph.children(9, return_nids=True), [10])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(26)
        self.assertItemsEqual(sub.children().nodes.keys(), [32, 33, 34, 35])
        self.assertItemsEqual(sub.children(return_nids=True), [32, 33, 34, 35])

    def test_axis_method_change_root(self):
        """
        Test axis method when graph root is changed
        """

        # Default root 1
        self.assertItemsEqual(self.graph.children(2, return_nids=True), [3, 12])

        # Change root to 12
        self.graph.root = 12
        self.assertItemsEqual(self.graph.children(2, return_nids=True), [1, 3])

        # Change root to 11. Could be both [1, 3] and [3, 12]. Return first
        # result after sorting based on node ID
        self.graph.root = 11
        self.assertItemsEqual(self.graph.children(2, return_nids=True), [3, 12])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        # One node in isolation
        sub = self.graph.getnodes(26)
        self.assertItemsEqual(sub.children().nodes.keys(), [])

        # Subgraph with same root
        sub = self.graph.getnodes([1, 2, 11, 12, 23])
        self.assertItemsEqual(sub.children(1, return_nids=True), [2, 11, 23])
        self.assertItemsEqual(sub.children(2, return_nids=True), [12])
        self.assertItemsEqual(sub.children(11, return_nids=True), [12])
        self.assertItemsEqual(sub.children(23, return_nids=True), [])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        self.graph.root = 25
        self.assertItemsEqual(self.graph.children(27, return_nids=True), [24, 28, 29])

        # Only edge from 27 to 29 not reverse.
        self.graph.remove_edge(27, 29, directed=True)
        self.assertItemsEqual(self.graph.children(27, return_nids=True), [24, 28])

        # Opposite still possible
        self.graph.add_edge(27, 29, directed=True)
        self.graph.remove_edge(29, 27, directed=True)
        self.assertItemsEqual(self.graph.children(27, return_nids=True), [24, 28, 29])

    def test_axis_method_one_node(self):
        """
        Test axis method containing only one node.
        Should not include NodeTools
        """

        sub = self.graph.getnodes(9)

        self.assertEqual(len(sub), 1)
        self.assertEqual(list(sub), [sub])

        for n in sub:
            self.assertEqual(n, sub)


class GraphAxisParentTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertEqual(node_parent(self.graph, 1, self.graph.root), None)
        self.assertEqual(node_parent(self.graph, 15, self.graph.root), 11)

        # Two parents, return one with lowest node ID
        self.assertEqual(node_parent(self.graph, 27, self.graph.root), 24)

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.parent(1).nodes.keys(), [])
        self.assertItemsEqual(self.graph.parent(15).nodes.keys(), [11])
        self.assertItemsEqual(self.graph.parent(27).nodes.keys(), [24])

        # Return nids instead of graph objects
        self.assertEqual(self.graph.parent(1, return_nids=True), None)
        self.assertEqual(self.graph.parent(15, return_nids=True), 11)
        self.assertEqual(self.graph.parent(27, return_nids=True), 24)

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(20)
        self.assertItemsEqual(sub.parent().nodes.keys(), [15])
        self.assertEqual(sub.parent(return_nids=True), 15)

        sub = self.graph.getnodes(1)
        self.assertItemsEqual(sub.parent().nodes.keys(), [])
        self.assertEqual(sub.parent(return_nids=True), None)

    def test_axis_method_change_root(self):
        """
        Test axis method when graph root is changed
        """

        # Default root 1
        self.assertEqual(self.graph.parent(27, return_nids=True), 24)

        # Change root to 26
        self.graph.root = 26
        self.assertEqual(self.graph.parent(27, return_nids=True), 25)

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        # One node in isolation
        sub = self.graph.getnodes(18)
        self.assertItemsEqual(sub.parent().nodes.keys(), [])

        # Subgraph
        sub = self.graph.getnodes([12, 13, 14])
        self.assertEqual(sub.parent(return_nids=True), None)

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        # Using 1 as root, 15 is parent of 18
        self.assertEqual(self.graph.parent(18, return_nids=True), 15)

        # Remove edge 15,18 makes 18 unreachable
        self.graph.remove_edge(15, 18, directed=True)
        self.assertEqual(self.graph.parent(18, return_nids=True), None)

        # Opposite still possible
        self.graph.add_edge(15, 18, directed=True)
        self.graph.remove_edge(18, 15, directed=True)
        self.assertEqual(self.graph.parent(18, return_nids=True), 15)


class GraphAxisAllParentTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertItemsEqual(node_all_parents(self.graph, 1, self.graph.root), [])
        self.assertItemsEqual(node_all_parents(self.graph, 15, self.graph.root), [11])

        # Two parents, return one with lowest node ID
        self.assertItemsEqual(node_all_parents(self.graph, 27, self.graph.root), [24, 25])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.all_parents(1).nodes.keys(), [])
        self.assertItemsEqual(self.graph.all_parents(15).nodes.keys(), [11])
        self.assertItemsEqual(self.graph.all_parents(27).nodes.keys(), [24, 25])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.all_parents(1, return_nids=True), [])
        self.assertItemsEqual(self.graph.all_parents(15, return_nids=True), [11])
        self.assertItemsEqual(self.graph.all_parents(27, return_nids=True), [24, 25])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(20)
        self.assertItemsEqual(sub.all_parents().nodes.keys(), [15])
        self.assertItemsEqual(sub.all_parents(return_nids=True), [15])

        sub = self.graph.getnodes(12)
        self.assertItemsEqual(sub.all_parents().nodes.keys(), [2, 11])
        self.assertItemsEqual(sub.all_parents(return_nids=True), [2, 11])

    def test_axis_method_change_root(self):
        """
        Test axis method when graph root is changed
        """

        # Default root 1
        self.assertItemsEqual(self.graph.all_parents(27, return_nids=True), [24, 25])

        # Change root to 26
        self.graph.root = 31
        self.assertItemsEqual(self.graph.all_parents(27, return_nids=True), [29])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        # One node in isolation
        sub = self.graph.getnodes(18)
        self.assertItemsEqual(sub.all_parents().nodes.keys(), [])

        # Subgraph
        sub = self.graph.getnodes([2, 11, 12, 13, 14, 15])

        # Root node for masked reset to node in selection
        self.assertEqual(sub.root, 2)
        self.assertItemsEqual(sub.all_parents(12, return_nids=True), [2, 11])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        # Using 1 as root, 15 is parent of 18
        self.assertItemsEqual(self.graph.all_parents(27, return_nids=True), [24, 25])

        # Remove edge 24, 27
        self.graph.remove_edge(24, 27, directed=True)
        self.assertItemsEqual(self.graph.all_parents(27, return_nids=True), [25])


class GraphAxisNeighborsTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertItemsEqual(node_neighbors(self.graph, 3), [2, 4, 5, 6, 7])
        self.assertItemsEqual(node_neighbors(self.graph, 10), [9])
        self.assertItemsEqual(node_neighbors(self.graph, 27), [24, 25, 28, 29])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.neighbors(3).nodes.keys(), [2, 4, 5, 6, 7])
        self.assertItemsEqual(self.graph.neighbors(10).nodes.keys(), [9])
        self.assertItemsEqual(self.graph.neighbors(27).nodes.keys(), [24, 25, 28, 29])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.neighbors(3, return_nids=True), [2, 4, 5, 6, 7])
        self.assertItemsEqual(self.graph.neighbors(10, return_nids=True), [9])
        self.assertItemsEqual(self.graph.neighbors(27, return_nids=True), [24, 25, 28, 29])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(27)
        self.assertItemsEqual(sub.neighbors().nodes.keys(), [24, 25, 28, 29])
        self.assertItemsEqual(sub.neighbors(return_nids=True), [24, 25, 28, 29])

        sub = self.graph.getnodes(10)
        self.assertItemsEqual(sub.neighbors().nodes.keys(), [9])
        self.assertItemsEqual(sub.neighbors(return_nids=True), [9])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        sub = self.graph.getnodes(3)
        self.assertItemsEqual(sub.neighbors().nodes.keys(), [])
        self.assertItemsEqual(sub.neighbors(return_nids=True), [])

        sub = self.graph.getnodes([24, 25, 27, 28])
        self.assertItemsEqual(sub.neighbors(27).nodes.keys(), [24, 25, 28])
        self.assertItemsEqual(sub.neighbors(27, return_nids=True), [24, 25, 28])

        sub = self.graph.getnodes([1, 23])
        self.assertItemsEqual(sub.neighbors().nodes.keys(), [23])
        self.assertItemsEqual(sub.neighbors(return_nids=True), [23])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        self.assertItemsEqual(self.graph.neighbors(15, return_nids=True), [11, 16, 17, 18, 19, 20])

        # Only edge from 15 to 20 not reverse.
        self.graph.remove_edge(15, 20, directed=True)
        self.assertItemsEqual(self.graph.neighbors(15, return_nids=True), [11, 16, 17, 18, 19])

        # Opposite still possible
        self.graph.add_edge(15, 20, directed=True)
        self.graph.remove_edge(20, 15, directed=True)
        self.assertItemsEqual(self.graph.neighbors(15, return_nids=True), [11, 16, 17, 18, 19, 20])


class GraphAxisLeavesTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertItemsEqual(node_leaves(self.graph, 3),
                         [4, 5, 6, 8, 10, 13, 14, 16, 17, 18, 19, 21, 22, 28, 30, 31, 32, 33, 34, 35])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.leaves().nodes.keys(),
                         [4, 5, 6, 8, 10, 13, 14, 16, 17, 18, 19, 21, 22, 28, 30, 31, 32, 33, 34, 35])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.leaves(return_nids=True),
                         [4, 5, 6, 8, 10, 13, 14, 16, 17, 18, 19, 21, 22, 28, 30, 31, 32, 33, 34, 35])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.descendants(3)
        self.assertItemsEqual(sub.leaves().nodes.keys(), [4, 5, 6, 8, 10])
        self.assertItemsEqual(sub.leaves(return_nids=True), [4, 5, 6, 8, 10])

        self.assertItemsEqual(self.graph.getnodes(16).leaves().nodes.keys(), [16])
        self.assertItemsEqual(self.graph.getnodes(16).leaves(return_nids=True), [16])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        sub = self.graph.getnodes(3)
        self.assertItemsEqual(sub.leaves().nodes.keys(), [])
        self.assertItemsEqual(sub.leaves(return_nids=True), [])

        sub = self.graph.getnodes([12, 13, 14])
        self.assertItemsEqual(sub.leaves().nodes.keys(), [13, 14])
        self.assertItemsEqual(sub.leaves(return_nids=True), [13, 14])

        # Include root is false by default
        sub = self.graph.getnodes([1, 23])
        self.assertItemsEqual(sub.leaves().nodes.keys(), [23])
        self.assertItemsEqual(sub.leaves(return_nids=True), [23])

        self.assertItemsEqual(sub.leaves(include_root=True).nodes.keys(), [1, 23])
        self.assertItemsEqual(sub.leaves(include_root=True, return_nids=True), [1, 23])

        # Get a subgraph with isolated node
        sub = self.graph.getnodes([12, 13, 14, 31])
        self.assertItemsEqual(sub.leaves(return_nids=True), [13, 14])
        self.assertItemsEqual(sub.leaves(return_nids=True, include_isolated=True), [13, 14, 31])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        sub = self.graph.descendants(15, include_self=True)

        self.assertItemsEqual(sub.leaves(return_nids=True), [16, 17, 18, 19, 21, 22])

        # Removing parent-leaf edge isolates them
        sub.remove_edge(15, 16)
        sub.remove_edge(15, 17)

        self.assertItemsEqual(sub.leaves(return_nids=True), [18, 19, 21, 22])

        # Unless include_isolated equals True
        self.assertItemsEqual(sub.leaves(return_nids=True, include_isolated=True), [16, 17, 18, 19, 21, 22])


class GraphAxisAncestorsTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertItemsEqual(node_ancestors(self.graph, 20, self.graph.root), [1, 11, 15])
        self.assertItemsEqual(node_ancestors(self.graph, 27, self.graph.root, include_self=True), [1, 23, 24, 27])
        self.assertItemsEqual(node_ancestors(self.graph, 1, self.graph.root), [])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.ancestors(20).nodes.keys(), [1, 11, 15])
        self.assertItemsEqual(self.graph.ancestors(27, include_self=True).nodes.keys(), [1, 23, 24, 27])
        self.assertItemsEqual(self.graph.ancestors(1).nodes.keys(), [])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.ancestors(20, return_nids=True), [1, 11, 15])
        self.assertItemsEqual(self.graph.ancestors(27, include_self=True, return_nids=True), [1, 23, 24, 27])
        self.assertItemsEqual(self.graph.ancestors(1, return_nids=True), [])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(27)

        self.assertItemsEqual(sub.ancestors().nodes.keys(), [1, 23, 24])
        self.assertItemsEqual(sub.ancestors(include_self=True).nodes.keys(), [1, 23, 24, 27])
        self.assertItemsEqual(sub.ancestors(return_nids=True), [1, 23, 24])
        self.assertItemsEqual(sub.ancestors(include_self=True, return_nids=True), [1, 23, 24, 27])

        sub = self.graph.getnodes(7)

        self.assertItemsEqual(sub.ancestors().nodes.keys(), [1, 2, 3])
        self.assertItemsEqual(sub.ancestors(return_nids=True), [1, 2, 3])

        sub = self.graph.getnodes(1)

        self.assertItemsEqual(sub.ancestors().nodes.keys(), [])
        self.assertItemsEqual(sub.ancestors(return_nids=True), [])

    def test_axis_method_change_root(self):
        """
        Test axis method when graph root is changed
        """

        # Default root 1
        self.assertItemsEqual(self.graph.ancestors(27, return_nids=True), [1, 23, 24])

        # Change root to 32
        self.graph.root = 32
        self.assertItemsEqual(self.graph.ancestors(27, return_nids=True), [32, 26, 25])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        sub = self.graph.getnodes([11, 12, 15, 15, 17])
        self.assertItemsEqual(sub.ancestors(17, return_nids=True), [11, 15])

        sub = self.graph.getnodes([24, 27, 26, 28, 29])
        self.assertItemsEqual(sub.ancestors(29, return_nids=True), [24, 27])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        self.assertItemsEqual(self.graph.ancestors(34, return_nids=True), [1, 23, 25, 26])

        # Cut 23 - 25, but still reachable using a longer path
        self.graph.remove_edge(23, 25, directed=True)
        self.assertItemsEqual(self.graph.ancestors(34, return_nids=True), [1, 23, 24, 27, 25, 26])

        # Also cut that path node no longer reachable from root 1
        self.graph.remove_edge(24, 27, directed=True)
        self.assertItemsEqual(self.graph.ancestors(34, return_nids=True), [])

        # Change root
        self.graph.root = 27
        self.assertItemsEqual(self.graph.ancestors(34, return_nids=True), [27, 25, 26])


class GraphAxisDescendantsTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        # Node 11 is circular linked and this will result in the full graph designated
        # as descendant except node 11 itself
        self.assertItemsEqual(node_descendants(self.graph, 11, self.graph.root),
                         [i for i in self.graph.nodes if i != 11])
        self.assertItemsEqual(node_descendants(self.graph, 4, self.graph.root), [])
        self.assertItemsEqual(node_descendants(self.graph, 15, self.graph.root), [16, 17, 18, 19, 20, 21, 22])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.descendants(11).nodes.keys(),
                              [i for i in self.graph.nodes if i != 11])
        self.assertItemsEqual(self.graph.descendants(4).nodes.keys(), [])
        self.assertItemsEqual(self.graph.descendants(15).nodes.keys(), [16, 17, 18, 19, 20, 21, 22])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.descendants(11, return_nids=True),
                         [i for i in self.graph.nodes if i != 11])
        self.assertItemsEqual(self.graph.descendants(4, return_nids=True), [])
        self.assertItemsEqual(self.graph.descendants(15, return_nids=True), [16, 17, 18, 19, 20, 21, 22])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(11)
        self.assertItemsEqual(sub.descendants().nodes.keys(),
                              [i for i in self.graph.nodes if i != 11])
        self.assertItemsEqual(sub.descendants(return_nids=True), [i for i in self.graph.nodes if i != 11])

        sub = self.graph.getnodes(4)
        self.assertItemsEqual(sub.descendants().nodes.keys(), [])
        self.assertItemsEqual(sub.descendants(return_nids=True), [])

        sub = self.graph.getnodes(15)
        self.assertItemsEqual(sub.descendants(include_self=True).nodes.keys(), [15, 16, 17, 18, 19, 20, 21, 22])
        self.assertItemsEqual(sub.descendants(include_self=True, return_nids=True), [15, 16, 17, 18, 19, 20, 21, 22])

    def test_axis_method_change_root(self):
        """
        Test axis method when graph root is changed
        """

        # Create copy of subgraph
        sub = self.graph.getnodes(list(range(2, 11))).copy()

        self.assertItemsEqual(sub.descendants(return_nids=True), [3, 4, 5, 6, 7, 8, 9, 10])

        sub.root = 10
        self.assertItemsEqual(sub.descendants(7, return_nids=True), [3, 8, 2, 4, 5, 6])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection.
        This prevents the circular linkage problem in this graph.
        """

        self.graph.masked = True

        sub = self.graph.getnodes([11, 12, 13, 14, 15, 16, 17, 20])

        self.assertEqual(sub.root, 11)
        self.assertItemsEqual(sub.descendants(12, return_nids=True), [13, 14])
        self.assertItemsEqual(sub.descendants(12, return_nids=True, include_self=True), [12, 13, 14])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        self.assertItemsEqual(self.graph.descendants(11, return_nids=True), [i for i in self.graph.nodes if i != 11])

        # Remove edge 12 - 2 prevents circular backtracking
        self.graph.remove_edge(12, 2, directed=True)
        self.assertItemsEqual(self.graph.descendants(11, return_nids=True),
                              [12, 15, 13, 14, 16, 17, 18, 19, 20, 21, 22])

        # Other way around still works
        self.graph.add_edge(12, 2, directed=True)
        self.graph.remove_edge(2, 12, directed=True)
        self.assertItemsEqual(self.graph.descendants(11, return_nids=True), [i for i in self.graph.nodes if i != 11])


class GraphAxisSiblingsTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_axis_function(self):
        """
        Test function call to method, always returns nids
        """

        self.assertItemsEqual(node_siblings(self.graph, 1, self.graph.root), [])
        self.assertItemsEqual(node_siblings(self.graph, 2, self.graph.root), [11, 23])
        self.assertItemsEqual(node_siblings(self.graph, 7, self.graph.root), [4, 5, 6])

    def test_axis_method(self):
        """
        Test call to function as class method
        """

        # Return graph objects
        self.assertItemsEqual(self.graph.siblings(1).nodes.keys(), [])
        self.assertItemsEqual(self.graph.siblings(2).nodes.keys(), [11, 23])
        self.assertItemsEqual(self.graph.siblings(7).nodes.keys(), [4, 5, 6])

        # Return nids instead of graph objects
        self.assertItemsEqual(self.graph.siblings(1, return_nids=True), [])
        self.assertItemsEqual(self.graph.siblings(2, return_nids=True), [11, 23])
        self.assertItemsEqual(self.graph.siblings(7, return_nids=True), [4, 5, 6])

    def test_axis_method_on_subgraph(self):
        """
        Test call to function as class method of subgraph
        """

        sub = self.graph.getnodes(1)
        self.assertItemsEqual(sub.siblings().nodes.keys(), [])
        self.assertItemsEqual(sub.siblings(return_nids=True), [])

        sub = self.graph.getnodes(2)
        self.assertItemsEqual(sub.siblings().nodes.keys(), [11, 23])
        self.assertItemsEqual(sub.siblings(return_nids=True), [11, 23])

    def test_axis_method_change_root(self):
        """
        Test axis method when graph root is changed
        """

        self.assertItemsEqual(self.graph.siblings(2, return_nids=True), [11, 23])

        self.graph.root = 12
        self.assertItemsEqual(self.graph.siblings(2, return_nids=True), [11, 13, 14])

    def test_axis_method_on_masked_graph(self):
        """
        Test call to function as class method when graph is masked
        Masked graphs have no edges and adjacency outside of selection
        """

        self.graph.masked = True

        sub = self.graph.getnodes(2)
        self.assertItemsEqual(sub.siblings().nodes.keys(), [])
        self.assertItemsEqual(sub.siblings(return_nids=True), [])

        sub = self.graph.getnodes([1, 2, 11, 3, 12])
        self.assertItemsEqual(sub.siblings(2).nodes.keys(), [11])
        self.assertItemsEqual(sub.siblings(2, return_nids=True), [11])

    def test_axis_method_directed_graph(self):
        """
        Test axis method while traversing directed graphs
        """

        self.assertItemsEqual(self.graph.siblings(2, return_nids=True), [11, 23])

        # Remove edge 1 to 11
        self.graph.remove_edge(1, 11, directed=True)
        self.assertItemsEqual(self.graph.siblings(2, return_nids=True), [23])

        # Other way around still works
        self.graph.add_edge(1, 11, directed=True)
        self.graph.remove_edge(11, 1, directed=True)
        self.assertItemsEqual(self.graph.siblings(2, return_nids=True), [11, 23])


class GraphAxisRootTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)

    def test_graph_axis_root_definition(self):
        """
        Axis based methods require a root node to be defined.
        """

        # Root automatically define at data import stage
        self.assertEqual(self.graph.root, 1)

        # Root node inherited in sub graph if not masked
        sub = self.graph.getnodes(5)
        self.assertEqual(sub.root, 1)

        # Root node reset in sub graph if masked
        self.graph.masked = True
        sub = self.graph.getnodes(5)
        self.assertEqual(sub.root, 5)

        # If root not defined, raise exception
        self.graph.root = None
        self.assertRaises(GraphitException, self.graph.children)


class GraphAxisNodeToolsTests(UnittestPythonCompatibility):
    currpath = os.path.dirname(__file__)
    _axis_graph = os.path.join(currpath, '../files/graph_axis.jgf')

    def setUp(self):
        """
        Graph axis test class setup

        Load graph from graph_axis.jgf in JSON format
        """

        self.graph = read_jgf(self._axis_graph)
        self.graph.node_tools = NodeAxisTools

    def test_axis_node_tools_path(self):
        """
        Test breadcrumb path generation
        """

        node = self.graph.getnodes(21)

        self.assertEqual(node.path(key='_id'), '1.11.15.20.21')

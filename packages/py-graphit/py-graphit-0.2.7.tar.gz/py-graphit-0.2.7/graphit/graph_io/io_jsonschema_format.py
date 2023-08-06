# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2018
# Author:  Marc van Dijk (marcvdijk@gmail.com)
# file: io_jsonschema_format.py

"""
Functions for building and validating graphs based on a JSON schema definition.
http://json-schema.org
"""

import os
import json
import logging
import uritools

from graphit import __module__
from graphit.graph_py2to3 import urlparse, PY_STRING
from graphit.graph_exceptions import GraphitException
from graphit.graph_axis.graph_axis_class import GraphAxis
from graphit.graph_combinatorial.graph_split_join_operations import graph_join
from graphit.graph_io.io_helpers import open_anything
from graphit.graph_io.io_jsonschema_format_drafts import JSONSchemaValidatorDraft07, JSONSchemaORMDraft07

__all__ = ['read_json_schema']
logger = logging.getLogger(__module__)


def resolve_json_ref(graph, **kwargs):
    """
    Resolve JSON Schema $ref pointers

    :param graph:   Graph to resolve $ref for
    """

    # Get path to current document for resolving relative document $ref
    path = graph.get_root().document_path

    for nid, ref in [(k, v['$ref']) for k, v in graph.nodes.items() if '$ref' in v]:

        # Parse JSON $ref
        parsed = uritools.urisplit(ref)

        # Internal ref to definition
        def_graph = None
        if parsed.fragment and parsed.fragment.startswith('/definitions') and not len(parsed.path):
            result = graph.xpath(parsed.fragment.replace('/definitions', '/'))
            if not result.empty():
                def_graph = result.descendants(include_self=True).copy()

        # Include ref from another JSON Schema
        elif len(parsed.path) and os.path.isfile(os.path.abspath(os.path.join(os.path.dirname(path), parsed.path))):
            external = read_json_schema(os.path.abspath(os.path.join(os.path.dirname(path), parsed.path)), **kwargs)
            fragment = parsed.fragment or 'root'
            result = external.xpath('{0}'.format(fragment.replace('/definitions', '/')))
            if not result.empty():
                def_graph = result.descendants(include_self=True).copy()

        else:
            logging.warn('Unresolvable JSON schema $ref pointer: {0}'.format(ref))

        # Merge definitions with target
        # TODO: check for property overloading at merge level
        if def_graph:
            def_root = def_graph.get_root()
            def_target = graph.getnodes(nid)

            # If def_root is not the JSON Schema document root then
            # update target node dictionary
            if not def_root.get('document_path'):
                for k, v in def_root.nodes[def_root.nid].items():
                    if k not in def_target:
                        def_target.set(k, v)

            if len(def_graph) > 1:
                links = [(nid, child) for child in def_root.children(return_nids=True)]
                def_graph.remove_node(def_root.nid)

                graph_join(graph, def_graph, links=links)

    # Remove 'definitions' from graph
    for nodes in graph.query_nodes(schema_label='definitions'):
        graph.remove_nodes(nodes.descendants(include_self=True, return_nids=True))


def parse_schema_meta_data(metadata):

    if 'draft' not in metadata:
        metadata['draft'] = 'general'
        if '$schema' in metadata:
            url = urlparse.urlparse(metadata['$schema'])
            for path_element in url.path.split('/'):
                if 'draft-' in path_element:
                    metadata['draft'] = path_element.replace('draft-', '')
                    break


def read_json_schema(schema, graph=None, exclude_args=None, resolve_ref=True):
    """
    Import hierarchical data structures defined in a JSON schema format

    :param schema:            JSON Schema data format to import
    :type schema:             dict, file, string, stream or URL
    :param graph:             graph object to import TGF data in
    :type graph:              :graphit:Graph
    :param exclude_args:      JSON schema arguments to exclude from import
    :type exclude_args:       :py:list
    :param resolve_ref:       Parse JSON schema 'definitions'
    :type resolve_ref:        :py:bool

    :return:                  Graph object
    :rtype:                   :graphit:Graph
    """

    json_schema = schema
    if not isinstance(schema, dict):

        # Try parsing the string using default Python json parser
        json_schema = open_anything(schema)
        try:
            json_schema = json.load(json_schema)
        except (IOError, ValueError) as error:
            logger.error('Unable to decode JSON string: {0}'.format(error))
            return

    # User defined or default Graph object
    if graph is None:
        graph = GraphAxis()
    elif not isinstance(graph, GraphAxis):
        raise GraphitException('Unsupported graph type {0}'.format(type(graph)))

    if graph.empty():
        rid = graph.add_node('root')
        graph.root = rid

    # Build JSON schema parser ORM with format specific conversion classes
    graph.node_tools = JSONSchemaValidatorDraft07
    graph.orm = JSONSchemaORMDraft07

    # What data-blocks to parse, properties by default, definitions if required
    datablock = ['properties']
    if resolve_ref:
        datablock.append('definitions')

    if exclude_args is None:
        exclude_args = []

    def walk_schema(schema_block, parent=None):

        # Get all JSON schema definitions for this data instance
        attributes = dict([(k, v) for k, v in schema_block.items() if not isinstance(v, dict)
                           and k not in exclude_args])
        node = graph.getnodes(parent)
        node.update(attributes)

        # Get 'required' attribute
        required = schema_block.get('required', [])
        if not isinstance(required, list):
            required = []

        # Store default data or None
        if attributes.get('default') is not None:
            node.set(graph.data.value_tag, attributes.get('default'))

        # For all child elements in datablock, make new node
        # and parse using recursive calls to parse_schema
        for block in schema_block.keys():
            if block in datablock:
                for child, attr in schema_block[block].items():
                    nid = graph.add_node(child)

                    # Register block_name in child attributes
                    attr['schema_label'] = block

                    # Register 'required' elements
                    if child in required:
                        attr['required'] = True

                    graph.add_edge(parent, nid)
                    walk_schema(attr, parent=nid)

    walk_schema(json_schema, graph.root)

    # Parse schema meta data
    document_path = ''
    if isinstance(schema, PY_STRING):
        document_path = os.path.abspath(schema)

    root = graph.get_root()
    root.set('document_path', document_path)
    parse_schema_meta_data(root)

    # Resolve JSON Schema $ref
    if resolve_ref:
        resolve_json_ref(graph, exclude_args=exclude_args)

    return graph

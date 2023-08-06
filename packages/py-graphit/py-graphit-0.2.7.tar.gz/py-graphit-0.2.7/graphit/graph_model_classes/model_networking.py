# -*- coding: utf-8 -*-

"""
file: model_networking.py

Graph model classes for dealing with network communication
"""

import re
import logging
import ipaddress
import uritools
import socket

from graphit import __module__
from graphit.graph_py2to3 import to_unicode, PY_STRING
from graphit.graph_mixin import NodeEdgeToolsBaseClass

__all__ = ['IP4Address', 'IP6Address']
logger = logging.getLogger(__module__)

HOSTNAME_REGEX = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)


class IP4Address(NodeEdgeToolsBaseClass):

    def set(self, key, value=None):
        """
        Validate and set IP4 address according to the "dotted-quad" ABNF
        syntax as defined in RFC 2673
        """

        if key == self.data.key_tag:
            try:
                ip = ipaddress.ip_address(to_unicode(value))
                if ip.version != 4:
                    logger.error('{0} is of IP protocol {1} not 4'.format(value, ip.version))
            except ipaddress.AddressValueError:
                logger.error('{0} not a valid IP4 address'.format(value))

        self.nodes[self.nid][key] = value


class IP6Address(NodeEdgeToolsBaseClass):

    def set(self, key, value=None):
        """
        Validate and set IP6 address according to RFC 4291
        """

        if key == self.data.key_tag:
            try:
                ip = ipaddress.ip_address(to_unicode(value))
                if ip.version != 6:
                    logger.error('{0} is of IP protocol {1} not 6'.format(value, ip.version))
            except ipaddress.AddressValueError:
                logger.error('{0} not a valid IP6 address'.format(value))

        self.nodes[self.nid][key] = value


class Hostname(NodeEdgeToolsBaseClass):

    @staticmethod
    def hostname():
        """
        Get hostname of current machine
        """

        return socket.gethostname()

    def set(self, key=None, value=None):
        """
        Validate and set a hostname according to RFC 1034 with idn support in
        as in RFC 5890.
        Set to current hostname if called without arguments.

        * Should be string
        * Maximum length of DNS name is 253 characters
        * Validate against hostname regex
        """

        key = key or self.data.value_tag
        if key == self.data.value_tag:
            if not value:
                value = self.hostname()
            if not isinstance(value, PY_STRING) or len(value) > 253 or not HOSTNAME_REGEX.match(value):
                logger.error('Not a valid hostname: {0}'.format(value))
                return

        self.nodes[self.nid][key] = value


class URI(NodeEdgeToolsBaseClass):
    """
    Methods for working with Universal Resource Identifiers (URIs) in
    accordance to RFC 3986 with support for unicode.
    """

    @property
    def scheme(self):

        uri = self.get()
        if uri:
            parts = uritools.urisplit(uri)
            return parts.scheme

    @property
    def authority(self):

        uri = self.get()
        if uri:
            parts = uritools.urisplit(uri)
            return parts.authority

    @property
    def port(self):

        uri = self.get()
        if uri:
            parts = uritools.urisplit(uri)
            return parts.port

    @property
    def path(self):

        uri = self.get()
        if uri:
            parts = uritools.urisplit(uri)
            return parts.path

    @property
    def query(self):

        uri = self.get()
        if uri:
            parts = uritools.urisplit(uri)
            return parts.query

    @property
    def fragment(self):

        uri = self.get()
        if uri:
            parts = uritools.urisplit(uri)
            return parts.fragment

    @staticmethod
    def compose(scheme=None, authority=None, path=None, query=None, fragment=None, port=None):

        parts = uritools.uricompose(scheme=scheme, host=authority, port=port, path=path, query=query, fragment=fragment)
        return uritools.uriunsplit(parts)

    def set(self, key, value, **kwarg):
        """
        Validate and set RFC 3986 compliant, Unicode-aware, scheme-agnostic URIs
        """

        if key == self.data.value_tag:
            if isinstance(value, PY_STRING):

                parsed = uritools.urisplit(value)
                if parsed.scheme and parsed.authority and parsed.path:
                    logger.error('No valid URI: {0}'.format(value))
                    return

        self.nodes[self.nid][key] = value


"""
Definitions of tree structures.
"""

from typing import Tuple, List, Mapping, Any

from penman.types import (Variable, Role)
from penman.epigraph import Epidata

# Tree types
Branch = Tuple[Role, Any, Epidata]
Node = Tuple[Variable, List[Branch]]


class Tree:
    """
    A tree structure.

    A tree is essentially a node that contains other nodes, but this
    Tree class is useful to contain any metadata and to provide
    tree-based methods.
    """

    __slots__ = 'node', 'metadata'

    def __init__(self,
                 node: Node,
                 metadata: Mapping[str, str] = None):
        self.node = node
        self.metadata = metadata or {}

    def __eq__(self, other) -> bool:
        if isinstance(other, Tree):
            other = other.node
        return self.node == other

    def __repr__(self) -> str:
        return 'Tree({!r})'.format(self.node)

    def __str__(self) -> str:
        return 'Tree(\n  {})'.format(_format(self.node, 2))

    def nodes(self):
        """
        Return the nodes in the tree as a flat list.
        """
        return _nodes(self.node)


def _format(node, level):
    var, edges = node
    next_level = level + 2
    indent = '\n' + ' ' * next_level
    edges = [_format_edge(edge, next_level) for edge in edges]
    return '({!r}, [{}{}])'.format(var, indent, (',' + indent).join(edges))


def _format_edge(edge, level):
    role, target, epidata = edge
    if is_atomic(target):
        target = repr(target)
    else:
        target = _format(target, level)
    return '({!r}, {}, {!r})'.format(role, target, epidata)


def _nodes(node):
    var, edges = node
    ns = [] if var is None else [node]
    for _, target, _ in edges:
        # if target is not atomic, assume it's a valid tree node
        if not is_atomic(target):
            ns.extend(_nodes(target))
    return ns


def is_atomic(x) -> bool:
    """
    Return ``True`` if *x* is a valid atomic value.
    """
    return x is None or isinstance(x, (str, int, float))

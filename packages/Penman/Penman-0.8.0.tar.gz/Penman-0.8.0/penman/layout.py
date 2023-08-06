# -*- coding: utf-8 -*-

"""
Interpreting trees to graphs and configuring graphs to trees.

In order to serialize graphs into the PENMAN format, a tree-like
layout of the graph must be decided. Deciding a layout includes
choosing the order of the edges from a node and the paths to get to a
node definition (the position in the tree where a node's concept and
edges are specified). For instance, the following graphs for "The dog
barked loudly" have different edge orders on the ``b`` node::

  (b / bark-01           (b / bark-01
     :ARG0 (d / dog)        :mod (l / loud)
     :mod (l / loud))       :ARG0 (d / dog))

With re-entrancies, there are choices about which location of a
re-entrant node gets the full definition with its concept (node
label), etc. For instance, the following graphs for "The dog tried to
bark" have different locations for the definition of the ``d`` node::

  (t / try-01              (t / try-01
     :ARG0 (d / dog)          :ARG0 d
     :ARG1 (b / bark-01       :ARG1 (b / bark-01
        :ARG0 d))                :ARG0 (d / dog))

With inverted edges, there are even more possibilities, such as::

  (t / try-01                (t / try-01
     :ARG0 (d / dog             :ARG1 (b / bark-01
        :ARG0-of b)                :ARG0 (d / dog
     :ARG1 (b / bark-01))             :ARG0-of t)))

This module introduces two epigraphical markers so that a pure graph
parsed from PENMAN can retain information about its tree layout
without altering its graph properties. The first marker type is
:class:`Push`, which is put on a triple to indicate that the triple
introduces a new node context, while the sentinel :data:`POP`
indicates that a triple is at the end of one or more node contexts.
These markers only work if the triples in the graph's data are
ordered. For instance, one of the graphs above (repeated here) has the
following data::

  PENMAN                 Graph                            Epigraph
  (t / try-01            [('t', ':instance', 'try-01'),   :
     :ARG0 (d / dog)      ('t', ':ARG0', 'd'),            : Push('d')
     :ARG1 (b / bark-01   ('d', ':instance', 'dog'),      : POP
        :ARG0 d))         ('t', ':ARG1', 'b'),            : Push('b')
                          ('b', ':instance', 'bark-01'),  :
                          ('b', ':ARG0', 'd')]            : POP
"""

from typing import Union, Mapping, Callable, Any
import copy
import logging

from penman.exceptions import LayoutError
from penman.types import Variable, BasicTriple
from penman.epigraph import Epidatum
from penman.tree import (Tree, Node, Branch, is_atomic)
from penman.graph import (Graph, CONCEPT_ROLE)
from penman.model import Model


logger = logging.getLogger(__name__)

_default_model = Model()

_Nodemap = Mapping[Variable, Union[Node, None]]


# Epigraphical markers

class LayoutMarker(Epidatum):
    """Epigraph marker for layout choices."""


class Push(LayoutMarker):
    """Epigraph marker to indicate a new node context."""

    __slots__ = 'variable',

    def __init__(self, variable):
        self.variable = variable

    def __repr__(self):
        return 'Push({})'.format(self.variable)


class _Pop(LayoutMarker):
    """Epigraph marker to indicate the end of a node context."""

    __slots__ = ()

    def __repr__(self):
        return 'POP'


#: Epigraphical marker to indicate the end of a node context.
POP = _Pop()


# Tree to graph interpretation ################################################

def interpret(t: Tree, model: Model = None) -> Graph:
    """
    Interpret tree *t* as a graph using *model*.

    Tree interpretation is the process of transforming the nodes and
    edges of a tree into a directed graph. A semantic model determines
    which edges are inverted and how to deinvert them. If *model* is
    not provided, the default model will be used.

    Args:
        t: the :class:`Tree` to interpret
        model: the :class:`~penman.model.Model` used to interpret *t*
    Returns:
        The interpreted :class:`~penman.graph.Graph`.
    Example:

        >>> from penman.tree import Tree
        >>> from penman import layout
        >>> t = Tree(
        ...   ('b', [
        ...     ('/', 'bark', []),
        ...     ('ARG0', ('d', [
        ...       ('/', 'dog', [])]), [])]))
        >>> g = layout.interpret(t)
        >>> for triple in g.triples:
        ...     print(triple)
        ...
        ('b', ':instance', 'bark')
        ('b', ':ARG0', 'd')
        ('d', ':instance', 'dog')

    """
    if model is None:
        model = _default_model
    top, triples, epidata = _interpret_node(t.node, model)
    g = Graph(triples, top=top, epidata=epidata, metadata=t.metadata)
    logger.info('Interpreted: %s', g)
    return g


def _interpret_node(t: Node, model: Model):
    triples = []
    epidata = {}
    var, edges = t
    for role, target, epis in edges:
        if role == '/':
            role = CONCEPT_ROLE
        # atomic targets
        if is_atomic(target):
            child = ()
            target_var = target
        # nested nodes
        else:
            child = target
            target_var = target[0]
        triple = model.deinvert((var, role, target_var))
        triples.append(triple)
        epidata[triple] = epis
        # recurse to nested nodes
        if child:
            epidata[triple].append(Push(target_var))
            _, _triples, _epis = _interpret_node(child, model)
            triples.extend(_triples)
            epidata.update(_epis)
            epidata[triples[-1]].append(POP)

    return var, triples, epidata


# Graph to tree configuration #################################################

def configure(g: Graph,
              top: Variable = None,
              model: Model = None,
              strict: bool = False) -> Tree:
    """
    Create a tree from a graph by making as few decisions as possible.

    A graph interpreted from a valid tree using :func:`interpret` will
    contain epigraphical markers that describe how the triples of a
    graph are to be expressed in a tree, and thus configuring this
    tree requires only a single pass through the list of triples. If
    the markers are missing or out of order, or if the graph has been
    modified, then the configuration process will have to make
    decisions about where to insert tree branches. These decisions are
    deterministic, but may result in a tree different than the one
    expected.

    Args:
        g: the :class:`~penman.graph.Graph` to configure
        top: the variable to use as the top of the graph; if ``None``,
            the top of *g* will be used
        model: the :class:`~penman.model.Model` used to configure the
            tree
        strict: if ``True``, raise :exc:`~penman.exceptions.LayoutError`
            if decisions must be made about the configuration
    Returns:
        The configured :class:`Tree`.
    Example:

        >>> from penman.graph import Graph
        >>> from penman import layout
        >>> g = Graph([('b', ':instance', 'bark'),
        ...            ('b', ':ARG0', 'd'),
        ...            ('d', ':instance', 'dog')])
        >>> t = layout.configure(g)
        >>> print(t)
        Tree(
          ('b', [
            ('/', 'bark', []),
            (':ARG0', ('d', [
              ('/', 'dog', [])]), [])]))
    """
    if model is None:
        model = _default_model
    node, data, nodemap = _configure(g, top, model, strict)
    # if any data remain, the graph was not properly annotated for a tree
    while data:
        skipped, var, data = _find_next(data, nodemap)
        data_count = len(data)
        if var is None or data_count == 0:
            raise LayoutError('possibly disconnected graph')
        _configure_node(var, data, nodemap, model)
        if len(data) >= data_count:
            raise LayoutError('possible cycle in configuration')
        data = skipped + data
        # remove any superfluous POPs
        while data and data[-1] is POP:
            data.pop()
    tree = Tree(node, metadata=g.metadata)
    logger.debug('Configured: %s', tree)
    return tree


def _configure(g, top, model, strict):
    """
    Create the tree that can be created without any improvising.
    """
    if len(g.triples) == 0:
        return (g.top, []), [], {}

    nodemap: _Nodemap = {var: None for var in g.variables()}
    if top is None:
        top = g.top
    if top not in nodemap:
        raise LayoutError('top is not a variable: {!r}'.format(top))
    nodemap[top] = (top, [])

    data = list(reversed(_preconfigure(g, strict)))
    node = _configure_node(top, data, nodemap, model)

    return node, data, nodemap


def _preconfigure(g, strict):
    """
    Arrange the triples and epidata for ordered traversal.

    Also perform some basic validation.
    """
    data = []
    epidata = g.epidata
    pushed = set()
    for triple in g.triples:
        push, pops, others = None, [], []
        for epi in epidata.get(triple, []):
            if isinstance(epi, Push):
                if push is not None or epi.variable in pushed:
                    if strict:
                        raise LayoutError(
                            "multiple node contexts for '{}'"
                            .format(epi.variable))
                    pass  # change to 'continue' to disallow multiple contexts
                if epi.variable not in (triple[0], triple[2]):
                    if strict:
                        raise LayoutError(
                            "node context '{}' invalid for triple: {}"
                            .format(epi.variable, triple))
                    continue
                pushed.add(epi.variable)
                push = epi
            elif epi is POP:
                pops.append(epi)
            else:
                others.append(epi)

        if strict and push and pops:
            raise LayoutError(
                'incompatible node context changes on triple: {}'
                .format(triple))

        data.append((triple, others, push))
        data.extend(pops)

    return data


def _configure_node(var, data, nodemap, model):
    """
    Configure a node and any descendants.

    Side-effects:
      * *data* is modified
      * *nodemap* is modified
    """
    node = nodemap[var]
    edges = node[1]

    while data:
        datum = data.pop()
        if datum is POP:
            break

        triple, epidata, push = datum
        if triple[0] == var:
            source, role, target = triple
        elif triple[2] == var:
            source, role, target = model.invert(triple)
        else:
            # misplaced triple
            data.append(datum)
            break

        if push and push.variable == target:
            nodemap[push.variable] = (push.variable, [])
            target = _configure_node(
                push.variable, data, nodemap, model)
        elif target in nodemap and nodemap[target] is None:
            # site of potential node context
            nodemap[target] = node

        if role == CONCEPT_ROLE:
            role = '/'
            index = 0
        else:
            index = len(edges)

        edges.insert(index, (role, target, epidata))

    return node


def _find_next(data, nodemap):
    """
    Find the next node context; establish if necessary.
    """
    var = None
    for i in range(len(data) - 1, -1, -1):
        datum = data[i]
        if datum is POP:
            continue
        source, _, target = datum[0]
        if source in nodemap and _get_or_establish_site(source, nodemap):
            var = source
            break
        elif target in nodemap and _get_or_establish_site(target, nodemap):
            var = target
            break
    pivot = i + 1
    return data[pivot:], var, data[:pivot]


def _get_or_establish_site(var, nodemap):
    """
    Turn a variable target into a node context.
    """
    # first check if the var is available at all
    if nodemap[var] is not None:
        _var, edges = nodemap[var]
        # if the mapped node's var doesn't match it can be established
        if var != _var:
            node = (var, [])
            nodemap[var] = node
            for i in range(len(edges)):
                # replace the variable in the tree with the new node
                if edges[i][1] == var:
                    edge = list(edges[i])
                    edge[1] = node
                    edges[i] = tuple(edge)
        else:
            pass  # otherwise the node already exists so we're good
        return True
    # var is not yet available
    return False


def reconfigure(g: Graph,
                top: Variable = None,
                model: Model = None,
                strict: bool = False) -> Tree:
    """
    Create a tree from a graph after any discarding layout markers.
    """
    p = copy.deepcopy(g)
    for epilist in p.epidata.values():
        epilist[:] = [epi for epi in epilist
                      if not isinstance(epi, LayoutMarker)]
    return configure(p, top=top, model=model, strict=strict)


def rearrange(t: Tree,
              key: Callable[[Branch], Any] = None) -> None:
    """
    Sort the branches at each node in tree *t* according to *key*.

    Each node in a tree contains a list of branches. This function
    sorts those lists in-place using the *key* function, which accepts
    a branch and returns some sortable criterion. If the first branch
    is the node label it will stay in place after the sort.

    Example:

        >>> from penman import layout
        >>> from penman.model import Model
        >>> from penman.codec import PENMANCodec
        >>> c = PENMANCodec()
        >>> t = c.parse('(s / see :ARG0 (d / dog) :ARG1 (c / cat))')
        >>> layout.rearrange(t, key=Model().random_order)
        >>> print(c.format(t))
        (s / see
           :ARG1 (c / cat)
           :ARG0 (d / dog))

    """
    if key is None:
        key = _default_model.original_order
    _rearrange(t.node, key=key)


def _rearrange(node: Node, key: Callable[[Branch], Any]) -> None:
    _, branches = node
    if branches and branches[0][0] == '/':
        first = branches[0:1]
        rest = branches[1:]
    else:
        first = []
        rest = branches[:]
    for _, target, _ in rest:
        if not is_atomic(target):
            _rearrange(target, key=key)
    branches[:] = first + sorted(rest, key=key)


def has_valid_layout(g: Graph,
                     top: Variable = None,
                     model: Model = None,
                     strict: bool = False) -> bool:
    """
    Return ``True`` if *g* contains the information for a valid layout.

    Having a valid layout means that the graph data allows a
    depth-first traversal that reconstructs a spanning tree used for
    serialization.
    """
    if model is None:
        model = _default_model
    tree, data, nodemap, variables = _configure(g, top, model, strict)
    return len(data) == 0


def appears_inverted(g: Graph, triple: BasicTriple) -> bool:
    """
    Return ``True`` if *triple* appears inverted in serialization.

    More specifically, this function returns ``True`` if *triple* has
    a :class:`Push` epigraphical marker in graph *g* whose associated
    variable is the source variable of *triple*. This should be
    accurate when testing a triple in a graph interpreted using
    :func:`interpret` (including :meth:`PENMANCodec.decode
    <penman.codec.PENMANCodec.decode>`, etc.), but it does not
    guarantee that a new serialization of *g* will express *triple* as
    inverted as it can change if the graph or its epigraphical markers
    are modified, if a new top is chosen, etc.

    Args:
        g: a :class:`~penman.graph.Graph` containing *triple*
        triple: the triple that does or does not appear inverted
    Returns:
        ``True`` if *triple* appears inverted in graph *g*.
    """
    return any(isinstance(epi, Push) and epi.variable == triple[0]
               for epi in g.epidata[triple])

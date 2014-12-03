class Node(object):
    def __init__(self, value):
        self._value = int(value)
        self._connections = set()

    @property
    def value(self):
        return self._value

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def connect(self, *nodes):
        for node in nodes:
            self._connections.add(node)
            node._connections.add(self)

    @property
    def connections(self):
        return self._connections

    def __repr__(self):
        # This is for debug reason, to make assert errors looks better
        return u'node:{v}'.format(v=self.value)


def visit(node, visited=None):
    '''Generator to walk though all nodes related to the given node including
    itself'''
    if visited is None:
        visited = set()
    yield node
    visited.add(node)
    for not_visited in node.connections - visited:
        if not_visited in visited:
            # Skip the node if it was visited by any other way
            continue
        for nn in visit(not_visited, visited):
            yield nn


def avg(node):
    '''Calculates average value for the node and all nodes connected to it
    '''
    val = count = 0.
    for nn in visit(node):
        val += float(nn)
        count += 1
    return val / count

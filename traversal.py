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


def avg(node, visited=None):
    '''Calculates average value for the node and all nodes connected to it
    recursively.'''
    if visited is None:
        visited = set()
    not_visited = ({node} | node.connections) - visited
    visited.add(node)
    return sum(map(float, not_visited)) / float(len(visited))

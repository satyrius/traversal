#!/usr/bin/env python
import unittest
from decimal import Decimal
from traversal import Node, avg


def d(float_value):
    assert float_value is not None
    return Decimal(str(float_value))


class NodeTest(unittest.TestCase):
    def test_init_node(self):
        node = Node(43)
        self.assertEqual(node.value, 43)

    def test_connect(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.connect(n2, n3)
        self.assertEqual(n1.connections, {n2, n3})
        self.assertEqual(n2.connections, {n1})
        self.assertEqual(n3.connections, {n1})


class TestTraverse(unittest.TestCase):
    def test_avg(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)

        n1.connect(n2, n3)
        n3.connect(n4, n5)

        self.assertEqual(
            d(avg(n2)),
            d(n1.value + n2.value + n3.value + n4.value + n5.value) / 5)

        self.assertEqual(d(avg(n6)), d(n6.value))


if __name__ == '__main__':
    unittest.main()

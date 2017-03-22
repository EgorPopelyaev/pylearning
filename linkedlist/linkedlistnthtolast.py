from linkedlist.singlylinckedlist import Node


def nth_to_last_node(n, head):
    current = head

    i = 0;

    while i <= n:

        if not current.next_node:
            raise LookupError("We reached the end!")

        current = current.next_node

        i += 1

    return current


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e


####

class TestNLast(object):
    def test(self, sol):
        assert_equal(sol(2, a), d)
        print 'ALL TEST CASES PASSED'


# Run tests
t = TestNLast()
t.test(nth_to_last_node)

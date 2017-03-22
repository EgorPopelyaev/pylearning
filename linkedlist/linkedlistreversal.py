from linkedlist.singlylinckedlist import Node


def reverse(head):

    current = head
    next_node = None
    prev_node = None

    while current:

        next_node = current.next_node

        current.next_node = prev_node

        prev_node = current
        current = next_node

    return prev_node


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

print a.value
print a.next_node.value
print b.next_node.value
print c.next_node.value

reverse(a)

print d.next_node.value
print c.next_node.value
print b.next_node.value

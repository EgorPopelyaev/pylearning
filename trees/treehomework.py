def pre_order(tree):
    if tree:
        print "Tree root: %r" % tree.get_root_val()
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print "Tree root: %r" % tree.get_root_val()


def in_order(tree):
    if tree:
        in_order(tree.get_left_child())
        print "Tree root: %r" % tree.get_root_val()
        in_order(tree.get_right_child())


from treeasoop import BinaryTree

b_tree = BinaryTree('Book')

b_tree.insert_left('Chapter1')
b_tree.insert_left('Chapter2')

print b_tree.get_left_child().get_root_val()

b_tree.insert_right('Chapter3')
b_tree.insert_right('Chapter4')

pre_order(b_tree)
print '=================='
post_order(b_tree)
print '=================='
in_order(b_tree)
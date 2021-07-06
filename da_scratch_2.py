class NodeRB:
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)
    def __str__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)


def grandparent(node):
    if node.parent is None:
        return None
    return node.parent.parent


# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp is None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class RedBlackTree:
    def __init__(self, root_val):
        self.root = NodeRB(root_val, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, value):
        """
        using recursion to insert value in tree like BST. But we're returning the value that was inserted to examine it
        to determine if rebalancing rotations
        :param value:
        :return:
        """

        print(f'inserting {value}...')

        def insert_recursion(node):

            if node.value < value:
                if node.right:
                    return insert_recursion(node.right)
                else:
                    node.right = NodeRB(value, node, 'red')
                    return node.right
            else:
                if node.left:
                    return insert_recursion(node.left)
                else:
                    node.left = NodeRB(value, node, 'red')
                    return node.left

        new_node = insert_recursion(self.root)
        self.rebalance(new_node)

    def rebalance(self, node):

        # Case1: root -> do nothing
        if node.parent is None:
            return

        # Case2: parent is black -> do nothing
        if node.parent.color == 'black':
            return

        # Case3: parent & pibling are red -> turn them black
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        # if there is no grandparent, next cases won't apply
        gp = grandparent(node)
        if gp is None:
            return

        # Case4: parent red but pibling black, & generations are staggered
        # Inside case where parent & child on different sides than grandparent)
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        print(print_tree(self.root))

        # Case5: parent red but pibling black, & generations are aligned
        # Outside case where parent & child on same side as grandparent)
        p = node.parent
        gp = p.parent
        print(f'grandparent= {gp.value}')
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        # In cases 3, 4, and 5, the parent of new node is red. But we rotated a red node with a red child up. Since red
        # nodes must have two black children, we'll switch the colors of the (original) parent and grandparent nodes.
        p.color = 'black'
        gp.color = 'red'
        print(print_tree(self.root))

    def rotate_left(self, node):  # note that parent or grandparent node was passed in depending on case 4 or 5

        # Save off the parent (grandparent) of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p is not None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        else:
            self.root = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p is not None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        else:
            self.root = node_moving_up
        node_moving_up.parent = p

    def search(self, value):
        pass


def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)


'''
rb_tree = RedBlackTree(7)
rb_tree.insert(3)
rb_tree.insert(10)
rb_tree.insert(5)
#print(rb_tree)
# rb_tree.insert(1)
# rb_tree.insert(4)
#rb_tree.insert(6)
print(rb_tree)
'''
tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)
print_tree(tree.root)
tree.insert(13)
print_tree(tree.root)
tree.insert(16)
print_tree(tree.root)

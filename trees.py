from collections import deque

# ============== Binary Tree Node =================


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # overwrite native functions so that, when print is called on them, we can see the value inside the node
    def __repr__(self):
        return f"Node({self.get_value()})"
    def __str__(self):
        return f"Node({self.get_value()})"


# =========== Basic Tree ================

class Tree(object):
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# =========== Binary Search Tree ================

class BinarySearchTree(object):
    def __init__(self, value=None):
        if isinstance(value, Node):
            self.root = value
        else:
            self.root = Node(value)

    def get_root(self):
        return self.root

    def set_root(self, value):
        self.root = value

    def compare(self, node, new_node):
        """
        basic function to compare nodes in binary search tree. expand if node is comparing key,value pairs
        :param node:
        :param new_node:
        :return: integer representing comparison
            0: new_node == existing node
            -1: new node < existing node
            1: new node > existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, new_value):
        node = self.root
        if node is None:
            self.root = new_value
            return

        new_node = Node(new_value)

        while True:
            status = self.compare(node, new_node)
            if status == 0:
                node.set_value(new_node.get_value())
            if status == -1:
                if not node.has_left_child():
                    node.set_left_child(new_node)
                    break
                node = node.get_left_child()
            if status == 1:
                if not node.has_right_child():
                    node.set_right_child(new_node)
                    break
                node = node.get_right_child()

    def insert_with_recursion(self, value):

        def insert(node):

            if node is None:
                return Node(value)

            if value < node.value:
                node.left = insert(node.left)
            else:
                node.right = insert(node.right)

            return node

        if self.root is None:
            self.root = value
            return

        insert(self.root)

    def search(self, value):

        def search_node(node):

            print('recur search node: {}'.format(node.value))

            if node is None:
                return node

            if value < node.value:
                return search_node(node.left)
            elif value > node.value:
                return search_node(node.right)
            else:
                return node

        return search_node(self.root)

    def min_value_node(self, node):
        """
        Given a non-empty binary search tree, loop leftmost bottom leaf
        :return: node with minimum key value found in that tree.
        """
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def delete_untested(self, value):
        # case 1: leaf
        # case 2: single child
            # a. left only
            # b. right only
        # case 3: double child with children
            # 1. find either the next highest or next lowest node from the one you want to delete
                # for lowest: go to first element of left sub-tree & then bottom-most right child down the tree,
                # vice versa for next highest
            # 2. Remove the found node in preparation for replacing delete node
                # make a copy & point it's parent's right child to the found node's left child
            # 3. delete node & replace with the copied node
                # point copied node's left & right to delete node's left & right
                # point parent of delete node to copied node
        # case 4: delete node is root (TODO)
            # TODO
        # case 5: delete node doesn't exist

        parent = None
        node = self.root

        # find node to delete
        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.get_left_child()
            elif value > node.value:
                node = node.get_right_child()

        # node to delete doesn't exist case
        if node is None or node.value != value:
            return False

        # root node case

        # leaf node case (childless)
        if node.get_left_child() is None:
            if node.get_right_child() is None:
                parent.set_right_child(None)
                parent.set_left_child(None)
                return
            # right child only case
            else:
                if parent.value > node.value:
                    parent.set_left_child(node.get_right_child())
                else:
                    parent.set_right_child(node.get_right_child())
                return
        # left child only case
        if node.get_right_child() is None:
            if parent.value > node.value:
                parent.set_left_child(node.get_left_child())
            else:
                parent.set_right_child(node.get_left_child())
            return

        # double child case
        # find next highest by getting last left node in right sub-tree
        parent_replacement_node = node
        replacement_node = node.get_right_child()
        while replacement_node.get_left_child():
            parent_replacement_node = replacement_node
            replacement_node = get_left_child()
        print("Next highest: {}".format(replacement_node.value))
        # make copy of replacement node
        temp_node = replacement_node
        # point temp node children to delete node children
        temp_node.set_right_child(node.get_right_child())
        temp_node.set_left_child(node.get_left_child())
        # point deletion parent node to new temp node
        if parent.value > node.value:
            parent.set_left_child(temp_node)
        else:
            parent.set_right_child(temp_node)
        # delete replacement node
        if replacement_node.has_right_child():
            parent_replacement_node.set_left_child(replacement_node.get_right_child())

    def delete_node_recursion(self, value):
        """
        Use recursion to delete a node from a binary search tree
        Note: can further optimize by keeping track of parent instead of calling min_value_node function. That way
            the child can be set to empty rather than making that last recursive call
        :param value: value to search & delete
        :return: None
        """

        def delete_node(node, val):

            # Base Case
            if node is None:
                return node

            # If the value to be deleted is smaller than the node's value then it lies in left subtree
            if val < node.value:
                node.left = delete_node(node.left, val)
            # If the value to be deleted is greater than the node's value then it lies in right subtree
            elif val > node.value:
                node.right = delete_node(node.right, val)
            # If value is same as node's value, then this is the node to be deleted
            else:

                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children: Get the inorder successor (smallest in the right subtree)
                temp = self.min_value_node(node.right)
                # Copy the inorder successor's content to this node
                node.value = temp.value
                # Delete the inorder successor
                node.right = delete_node(node.right, temp.value)

            return node

        root = self.root
        print(delete_node(root, value))

    def __repr__(self):
        """
        overwrite py print functionality to print a tree in a visually appeasing way using BFS traversal
        :return: string of visual representation of a tree
        """
        level = 0
        q = deque()
        visit_order = list()
        node = self.get_root()
        q.appendleft((node, level))
        while q:
            node, level = q.pop()
            if node is None:
                visit_order.append(('<empty>', level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.appendleft((node.get_left_child(), level + 1))
            else:
                q.appendleft((None, level + 1))

            if node.has_right_child():
                q.appendleft((node.get_right_child(), level + 1))
            else:
                q.appendleft((None, level + 1))

            s = "Tree\n"
            previous_level = -1
            for i in range(len(visit_order)):
                node, level = visit_order[i]
                if level == previous_level:
                    s += " | " + str(node)
                else:
                    s += "\n" + str(node)
                    previous_level = level
        return s

# ======== Set up tree ==========


def convert_arr_to_binary_tree(arr):
    """
    Takes array input representing level order traversal of binary tree.
    Note that nodes with empty children are represented as None. If there aren't enought None type elements to
    represent empty children, an IndexError will be thrown
    :param arr: array of level order binary tree
    :return: root of binary tree
    """
    index = 0
    length = len(arr)
    if length <= 0 or arr[0] == -1:
        return None

    root = Node(arr[index])
    index += 1
    queue = deque()
    queue.appendleft(root)  # verify

    while queue:
        current_node = queue.pop()  # verify
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = Node(left_child)
            current_node.left = left_node
            queue.appendleft(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = Node(right_child)
            current_node.right = right_node
            queue.appendleft(right_node)
    return root



'''
node1 = Node('apple')
node2 = Node('banana')
node3 = Node('orange')
node1.set_left_child(node2)
node1.set_right_child(node3)
print(f"""
value: {node1.value}
left: {node1.left.value}
right: {node1.right.value}
""")
print(f"""Node 1 Has left node: {node1.has_left_child()}""")
print(f"""Node 2 has left node: {node2.has_left_child()}""")
print(node1) # now shows value inside node
'''

#binary_tree = Tree('apple')
#binary_tree.get_root().set_left_child(Node('banana'))
#binary_tree.get_root().set_right_child(Node('cherry'))
#binary_tree.get_root().get_left_child().set_left_child(Node('dates'))
#binary_tree.get_root().get_left_child().set_right_child(Node('grapes'))
#binary_tree.get_root().get_left_child().get_right_child().set_left_child(Node('pear'))
#binary_tree.get_root().get_left_child().get_right_child().set_right_child(Node('orange'))

# print(binary_tree)

r = convert_arr_to_binary_tree([8, 3, 10, 1, 6, None, 13, None, None, 4, 7, None, None, None, None, None, None])
binary_search_tree = BinarySearchTree(r)
# binary_search_tree.insert_with_recursion(5)
# print(binary_search_tree)
# binary_search_tree.delete_node_recursion(3)
# print(binary_search_tree)
# print(binary_search_tree.search(6))


# ============= Pre-Order Traversal Stack without State Object ============

# use stack to traverse tree
class StackLL:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.head is None:
            return None
        temp_val = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp_val

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def top_node(self):
        if self.head is None:
            return None
        return self.head

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def to_list(self):
        if self.head == None:
            return None
        out = []
        current = self.head
        while current:
            out.append(current.value)
            current = current.next
        return out


def pre_order_traversal(tree, target):

    """
    create visit order list
    create stack
    push root on stack
    append top of stack to visit order list
    loop
        check if stack empty, return
        check top of stack node for target value
            if val == target, return
        check top of stack node for left child
        if left child, put on stack & append to list
        else
            if right child, put on stack & append to list
            else, pop current node from stack

    """
    visit_order = list()
    stack = StackLL()
    stack.push(tree.get_root())

    while True:
        top_node = stack.top_node()
        if top_node is None:
            return None
        top_val = top_node.value.value
        print(f"""checking top of stack: {top_val}""")
        if top_val == target:
            return top_val

        tree_node = top_node.value
        if tree_node in visit_order:
            # if right node is in visit order or doesn't exist
            if not tree_node.has_right_child() or tree_node.get_right_child() in visit_order:
                stack.pop()
            else:
                stack.push(tree_node.get_right_child())
            continue

        if tree_node.has_left_child():
            stack.push(tree_node.get_left_child())
        elif tree_node.has_right_child():
            stack.push(tree_node.get_right_child())
        else:
            stack.pop()

        visit_order.append(tree_node)


# ============== Pre-Order Traversal w/ State Obj ===========

class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self, value=True):
        self.visited_left = value

    def set_visited_right(self, value=True):
        self.visited_right = value


def pre_order_traversal_state(tree, debug_mode=False):
    visit_order = list()
    stack = StackLL()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while node:
        if debug_mode:
            print(f"""
                loop count: {count}
                current node: {node}
                stack: {stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        elif node.has_right_child() and not state.get_visited_right():
            state.get_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""
            loop count: {count}
            current node: {node}
            stack: {stack}
        """)

    return visit_order


# ========= (DFS) Pre-Order, In-Order, Post-Order with Recursion =============

def pre_order_with_recursion_not_efficient_but_i_tried(tree):
    """
    creates a list of all the nodes that were touched and in what order
    (improved solution below)
    :param tree: binary tree
    :return: list of visit order nodes
    """

    visit_order = list()  # use set if don't want repeat values

    def check_node(node, visit_order):
        print("Current node value: {}".format(node.value))
        visit_order.append(node)
        if node.has_left_child() and node.get_left_child() not in visit_order:
            check_node(node.get_left_child(), visit_order)
        elif node.has_right_child() and node.get_right_child() not in visit_order:
            check_node(node.get_right_child(), visit_order)

        check_node(node, visit_order)

    check_node(tree.get_root(), visit_order)
    return visit_order


def pre_order_recursion_2(tree):
    """
    pre-order traversal using recursion
    notice the nodes are appended before the recursive calls
    :param tree:
    :return:
    """
    visit_order = list()

    def traverse(node):
        if node is not None:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())

    traverse(tree.get_root())
    return visit_order


def in_order_recursion(tree):
    """
    in-order traversal using recursion
    notice the nodes are appended after the left child recursive call
    :param tree:
    :return:
    """
    visit_order = list()

    def traverse(node):
        if node is not None:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())

    traverse(tree.get_root())
    return visit_order


def post_order_recursion(tree):
    """
    post-order traversal using recursion
    notice the nodes are appended after both recursive calls
    :param tree:
    :return:
    """
    visit_order = list()

    def traverse(node):
        if node is not None:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node.get_value())

    traverse(tree.get_root())
    return visit_order


# =================== (BFS) Breadth First Search =====================

def breadth_first_search_using_queue(tree):
    """
    BFS to mark off by levels
    Use queue to add children left to right first. As you dequeue it, add it's children
    :param tree:
    :return:
    """

    visit_order = list()
    q = deque()
    q.appendleft(tree.get_root())

    while q:
        node = q.pop()
        visit_order.append(node.value)
        if node.has_left_child():
            q.appendleft(node.get_left_child())
        if node.has_right_child():
            q.appendleft(node.get_right_child())

    return visit_order


# =========== Diameter of Binary Tree =============


def diameter_of_binary_tree(root):
    """
    Given the root, find the maximum distance between any two nodes
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root: root node of binary tree
    :return: [height, diameter]
    """
    if root is None:
        return 0, 0

    left_height, left_diameter = diameter_of_binary_tree(root.left)
    right_height, right_diameter = diameter_of_binary_tree(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter


print(diameter_of_binary_tree(r))


# ========== Path from Node ==========

def path_from_root_to_node(root, data):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    """
    output = path_from_node_to_root(root, data)
    return list(reversed(output))


def path_from_node_to_root(root, data):
    if root is None:
        return None

    elif root.data == data:
        return [data]

    left_answer = path_from_node_to_root(root.left, data)
    if left_answer is not None:
        left_answer.append(root.data)
        return left_answer

    right_answer = path_from_node_to_root(root.right, data)
    if right_answer is not None:
        right_answer.append(root.data)
        return right_answer
    return None

from collections import deque
import sys


class Node:

    def __init__(self, character, frequency):
        self.freq = frequency
        self.char = character
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __repr__(self):
        return f"Node({self.char}{self.freq})"

    def __str__(self):
        return f"Node({self.char}{self.freq})"


class MinHeap:

    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_idx = 0

    def up_heapify(self, child_idx):
        if child_idx == 0:
            return
        child_node = self.cbt[child_idx]
        parent_idx = (child_idx - 1) // 2
        parent_node = self.cbt[parent_idx]
        if child_node.freq >= parent_node.freq:
            return
        self.cbt[parent_idx] = child_node
        self.cbt[child_idx] = parent_node
        self.up_heapify(parent_idx)

    def down_heapify(self, parent_idx):
        left_idx = 2 * parent_idx + 1
        right_idx = 2 * parent_idx + 2
        right_node = None
        parent_node = self.cbt[parent_idx]
        minimum = parent_node.freq

        # check if children exist
        if left_idx >= self.next_idx:
            return  # if there's no left child, then there's no right

        left_node = self.cbt[left_idx]

        if right_idx < self.next_idx:
            right_node = self.cbt[right_idx]
            minimum = min(right_node.freq, minimum)

        minimum = min(left_node.freq, minimum)

        if minimum == parent_node.freq:
            return

        if minimum == left_node.freq:
            self.cbt[parent_idx] = left_node
            self.cbt[left_idx] = parent_node
            return self.down_heapify(left_idx)
        elif minimum == right_node.freq:
            self.cbt[parent_idx] = right_node
            self.cbt[right_idx] = parent_node
            return self.down_heapify(right_idx)

    def insert(self, data):

        # insert at self.next_index
        self.cbt[self.next_idx] = data
        child_index = self.next_idx
        self.next_idx += 1
        # heapify
        self.up_heapify(child_index)

        if self.next_idx >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for idx in range(self.next_idx):
                self.cbt[idx] = temp[idx]

    def remove(self):
        root = self.cbt[0]
        if root is None:
            return None
        # swap root with last index
        self.cbt[0] = self.cbt[self.next_idx - 1]
        # remove last index
        self.next_idx -= 1
        self.cbt[self.next_idx] = None
        if self.next_idx > 0:
            # down_heapify
            self.down_heapify(0)
        return root


def print_tree(root):
    """
    overwrite py print functionality to print a tree in a visually appeasing way using BFS traversal
    :return: string of visual representation of a tree
    """
    level = 0
    q = deque()
    visit_order = list()
    # node = self.get_root()
    q.appendleft((root, level))
    while q:
        node, level = q.pop()
        if node is None:
            visit_order.append(('<empty>', level))
            continue
        visit_order.append((node, level))
        if node.left:
            q.appendleft((node.left, level + 1))
        else:
            q.appendleft((None, level + 1))

        if node.right:
            q.appendleft((node.right, level + 1))
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


def huffman_encoding(data):
    '''
    1. Determine frequency of each char & put in node with char, freq, left child, right child
    2. Put nodes in sorted list that will be a priority queue
    3. Dequeue two (smallest) elements and add them together to make a new parent node where the smallest child node is
        the left child and the other is the right. Add the new node back into the priority queue
    4. Repeat #3 until there's a single node left in the queue, which will be the root
    5. Traverse the tree assigning all left nodes 0 and right nodes 1 so that the leaf nodes will be assigned a binary
        number based on the left/right paths
    :param data:
    :return:
    '''

    if not data:
        raise ValueError("No data to encode!")

    # traverse tree for binaries
    def traverse(node):
        if node is not None:
            bit_list.append('0')
            traverse(node.left)
            bit_list.pop()
            bit_list.append('1')
            traverse(node.right)
            bit_list.pop()
            if node.char is not None:
                bit_map[node.char] = ''.join(bit_list)

    # determine char frequency
    freq_map = dict()
    for char in data:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    # put in priority queue
    min_heap = MinHeap(10)
    for k, v in freq_map.items():
        node = Node(k, v)
        min_heap.insert(node)

    # sum mins & create tree
    while min_heap.next_idx > 0:
        left = min_heap.remove()
        right = min_heap.remove()
        right_freq = right.freq if right else 0
        new_val = left.freq + right_freq
        new_node = Node(None, new_val)
        new_node.set_left(left)
        new_node.set_right(right)
        min_heap.insert(new_node)
        if not right:
            break
    tree_root = min_heap.cbt[0]

    # print(print_tree(tree_root))
    bit_map = dict()
    bit_list = list()
    traverse(tree_root)

    code = ''
    for char in data:
        code += bit_map[char]

    return code, tree_root


def huffman_decoding(data, root):
    """
    1. Use the encoded data to traverse the tree bit by bit: 0 traverse left, 1 traverses right
    2. Append leaf node chars to a decode string
    :param data:
    :param tree:
    :return:
    """

    decoded = ''
    node = root
    for bit in data:
        if node.left is None:  # node.right will also be None; leaf node
            decoded += node.char
            node = root
        if bit == '0':
            node = node.left
        elif bit == '1':
            node = node.right
        else:
            raise ValueError("Encoded data contains a non-bit value.")
    # add last char
    decoded += node.char

    return decoded


# Test case 1
print('======== Test 1: Happy Path')
a_great_sentence = "The bird is the word"

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 2
print('======== Test 2: Single character')
sentence_2 = "T"

print("The size of the data is: {}\n".format(sys.getsizeof(sentence_2)))
print("The content of the data is: {}\n".format(sentence_2))

encoded_data, tree = huffman_encoding(sentence_2)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 3
print('======== Test 3: Repeated same character')
sentence_2 = "TTT"

print("The size of the data is: {}\n".format(sys.getsizeof(sentence_2)))
print("The content of the data is: {}\n".format(sentence_2))

encoded_data, tree = huffman_encoding(sentence_2)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The content of the encoded data is: {}\n".format(decoded_data))
print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

# Test case 4
print('======== Test 4: Large input')
sentence_2 = "TTTaAbbBCcdDeEFfGghhhhhHiJkLLLLmmmabcNonopoq  @ QQrsStUuvvvVoabcW x yYy y XzZZ@ abcdefg 12324i384939" \
             "58372738 anbdkslf111111111!! lkjadf Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " \
             "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud " \
             "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " \
             "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat " \
             "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print("The size of the data is: {}\n".format(sys.getsizeof(sentence_2)))
print("The content of the data is: {}\n".format(sentence_2))

encoded_data, tree = huffman_encoding(sentence_2)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 5
print('======== Test 5: Empty string input')
sentence_2 = ""

print("The size of the data is: {}\n".format(sys.getsizeof(sentence_2)))
print("The content of the data is: {}\n".format(sentence_2))

encoded_data, tree = huffman_encoding(sentence_2)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The content of the encoded data is: {}\n".format(decoded_data))
print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

import sys

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
    # determine char frequency
    freq_map = dict()
    for char in data:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1


    

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
import collections

# ================= Basic Tries ==============================

'''
-The Trie data structure is part of the family of Tree data structures.
-It shines when dealing with sequence data, whether it's characters, words, or network nodes. 
'''

basic_trie = {
        # a and add word
        'a': {
            'd': {
                'd': {
                    'word_end': True
                },
                'word_end': False
            },
            'word_end': True
        },
        # hi word
        'h': {
            'i': {
                'word_end': True
            },
            'word_end': False
        }
}
# print('Is "ad" a word: {}'.format(basic_trie['a']['d']['word_end']))


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie
    for char in word:
        if char not in current_node:
            return False
        current_node = current_node[char]
    return current_node['word_end']

# print(is_word('hi'))


class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def exists(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word


#trie = Trie()
#trie.add("bum")
#trie.add("add")
#print(trie.exists("addd"))


# ============== Trie using Defaultdict ==================

'''
-import collections is at top of file
-A cleaner way to build a trie is with a Python default dictionary. 
-The following `TrieNode2` class is using `collections.defaultdict` instead of a normal dictionary.
'''


class TrieNode2(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode2)
        self.is_word = False


class Trie2(object):
    def __init__(self):
        self.root = TrieNode2()

    def add(self, word):
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

            current_node.is_word = True

    def exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word

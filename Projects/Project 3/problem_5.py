import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        # Add a child node in this Trie
        # Don't think it's necessary since i'm using a defaultdict
        pass

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for all complete words below this point

        suffix_list = []

        if self.is_word and suffix != '':
            suffix_list.append(suffix)

        if self.children:
            for key, val in self.children.items():
                suffix += key
                suffix_list.extend(val.suffixes(suffix))
                suffix = suffix[:-1]

        return suffix_list


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        if type(word) is not str:
            raise TypeError("Invalid input for insert(): String expected.")

        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):

        if type(prefix) is not str:
            raise TypeError("Invalid input for find(): String expected.")

        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node


# ======== testing section =========

def create_trie(word_list):
    my_trie = Trie()
    for word in word_list:
        my_trie.insert(word)
    return my_trie


def test_prefix(prefix, trie):
    prefix_node = trie.find(prefix)
    if prefix_node:
        # print('\n'.join(prefix_node.suffixes()))
        print(prefix_node.suffixes())
    else:
        print(prefix + ' not found')


wordList_1 = [
    "a", "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
wordList_2 = []
wordList_3 = [
    "a", "ant", "anthology", "antagonist", "antonym",
    "fun", "function", False, "factory",
    "trie", "trigger", 3, "tripod"
]

my_trie_1 = create_trie(wordList_1)
test_prefix('a', my_trie_1)
# expected result: ['nt', 'nthology', 'ntagonist', 'ntonym']

test_prefix('ant', my_trie_1)
# expected result: ['hology', 'agonist', 'onym']

test_prefix('anth', my_trie_1)
# expected result: ['hology']

test_prefix('and', my_trie_1)
# expected result: and not found

test_prefix('tripod', my_trie_1)
# expected result: []

test_prefix('', my_trie_1)
# expected result: ['a', 'ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

try:
    test_prefix(False, my_trie_1)
except TypeError as e:
    print(e)
# expected result: TypeError

my_trie_2 = create_trie(wordList_2)
test_prefix('e', my_trie_2)
# expected result: a not found

try:
    my_trie_3 = create_trie(wordList_3)
except TypeError as e:
    print(e)
# expected result: TypeError




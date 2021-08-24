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


class TrieNode1(object):

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie1(object):

    def __init__(self):
        self.root = TrieNode1()

    def add(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode1()
            current_node = current_node.children[char]
        current_node.is_word = True

    def exists(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word


#trie = Trie1()
#trie.add("bum")
#trie.add("add")
#print(trie.exists("addd"))


# ============== Trie using Defaultdict ==================

'''
-import collections is at top of file
-A cleaner way to build a trie is with a Python default dictionary. 
-The following `TrieNode2` class is using `collections.defaultdict` instead of a normal dictionary.
-defaultdict automatically adds any key you put in instead of returning Key Not Found error
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


'''
trie = Trie2()
trie.add('addition')
trie.add('bum')
print(trie.exists("additio"))
print(trie.exists("additio"))
'''

# ============== Autocomplete Trie ==================


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
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node

'''
MyTrie = Trie()
wordList = [
    "a", "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefix_node = MyTrie.find('a')
if prefix_node:
    # print('\n'.join(prefix_node.suffixes()))
    print(prefix_node.suffixes())
else:
    print(prefix + ' not found')


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f,prefix='');
'''


# ============== HTTP Router ==================

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = None

    def insert(self, path):
        # Insert the node as before

        # *not necessary since using defaultdict as before

        pass


class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        if len(parts) == 0:
            return self.root

        part_head = parts[-1]
        parts_remaining = parts[:-1]

        node = self.insert(parts_remaining, None)

        node = node.children[part_head]
        if handler:
            node.handler = handler
        return node

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root

        for p in path:
            if p not in current_node.children:
                return None

            current_node = current_node.children[p]

        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie()
        self.add_handler('/', root_handler)
        self.add_handler('/404', not_found_handler)
        self.add_handler('/500', 'server error handler')

        self.not_found_config = self.split_path('/404')
        self.error_config = self.split_path('/500')

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # handle trailing '/'
        if path[-1] == '/':
            path = path[:-1]

        path_parts = self.split_path(path)
        self.router.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        try:

            # handle trailing '/'
            if path[-1] == '/':
                path = path[:-1]

            path_parts = self.split_path(path)
            handler = self.router.find(path_parts)

            # if page not found, return 'not found handler'
            if not handler:
                handler = self.router.find(self.not_found_config)

        except Exception as e:
            print(e)
            handler = self.router.find(self.error_config)

        finally:
            return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here

        import re  # todo move to top of file

        # regex to split path & put into list
        pattern = re.compile(r'/\w*')
        matches = pattern.findall(path)
        # add root handler to list
        if path != '/':
            matches.append('/')

        return matches


router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

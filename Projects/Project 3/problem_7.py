import collections

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

        try:

            if type(path) is not str:
                raise TypeError("Path in add_handler function must be a string.")

            # handle trailing '/'
            if path[-1] == '/':
                path = path[:-1]

            path_parts = self.split_path(path)
            self.router.insert(path_parts, handler)

        except Exception as e:
            print(e)
            handler = self.router.find(self.error_config)

        finally:
            return handler

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        try:

            if type(path) is not str:
                raise TypeError("Path in add_handler function must be a string.")

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


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

print(router.lookup("/"))
# expected result: 'root handler'

print(router.lookup("/home"))
# expected result: 'not found handler'

print(router.lookup("/home/about"))
# expected result: 'about handler'

print(router.lookup("/home/about/"))
# expected result: 'about handler'

print(router.lookup("/home/about/me"))
# expected result: 'not found handler'

router.add_handler("/home/about/me", "about me handler")  # add a route
print(router.lookup("/home/about/me"))
# expected result: 'about me handler'

router.add_handler(False, "test handler")  # add a route
# expected result: server error handler

print(router.lookup(False))
# expected result: server error handler

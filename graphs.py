
from collections import deque


class GraphNode(object):

    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)


class Graph(object):

    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            node_1.add_child(node_2)
            node_2.add_child(node_1)

    def remove_edge(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            node_1.remove_child(node_2)
            node_2.remove_child(node_1)


# =============== Depth-First Search =====================

def dfs_search_recursion(graph_node, search_value):
    """
    Depth-First Search for node in a graph with a certain value using recursion. If not found, return -1
    :param graph_node: starting node
    :param search_value: target value
    :return: node containing search value or -1 if None
    """

    def dfs_recur(node):

        if node.value == search_value:
            return node

        visited.add(node)
        found = -1
        for gn in node.children:
            if gn not in visited:
                found = dfs_recur(gn)
                if found != -1:
                    break
        return found

    visited = set()
    return dfs_recur(graph_node)


def dfs_search_stack(graph_node, search_value):
    """
    Depth-First Search for node in a graph with a certain value using a stack. If not found, return -1
    :param graph_node: starting node
    :param search_value: target value
    :return: node containing search value or -1 if None
    """

    visited = set()  # Sets are faster for lookups
    stack = deque()  # Start with a given root node
    stack.append(graph_node)

    while stack:  # Repeat until the stack is empty

        current_node = stack.pop()  # Pop out a node added recently
        visited.add(current_node)  # Mark it as visited

        if current_node.value == search_value:
            return current_node

        # Check all the neighbours
        for child in current_node.children:

            # If a node hasn't been visited before.
            if child not in visited:
                stack.append(child)

    return -1


# =============== Breadth-First Search =====================

def bfs_search(root_node, search_value):
    """
    Breadth-first search in graph for a node with a certain value using a queue. If not found, return -1
    :param root_node:
    :param search_value:
    :return:
    """

    visited = set()
    queue = deque()
    queue.append(root_node)

    while queue:

        current_node = queue.popleft()
        visited.add(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                queue.append(child)
    return -1


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
'''
for each in graph1.nodes:
    print('parent node = ',each.value,end='\nchildren\n')
    for each in each.children:
        print(each.value,end=' ')
    print('\n')
'''

print(dfs_search_stack(nodeS, 'A').value)
print(dfs_search_stack(nodeA, 'A').value)
print(dfs_search_stack(nodeP, 'S').value)
print(dfs_search_stack(nodeH, 'R').value)
print(dfs_search_stack(nodeH, 'Z'))

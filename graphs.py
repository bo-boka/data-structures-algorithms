
# from collections import deque
import collections
import sys
import heapq


# =============== Unweighted Graphs =====================

class GraphNodeU(object):

    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)


class GraphU(object):

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


# Test Graph
nodeG = GraphNodeU('G')
nodeR = GraphNodeU('R')
nodeA = GraphNodeU('A')
nodeP = GraphNodeU('P')
nodeH = GraphNodeU('H')
nodeS = GraphNodeU('S')

graph1 = GraphU([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )

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
    stack = collections.deque()  # Start with a given root node
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
    queue = collections.deque()
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


'''
print(dfs_search_stack(nodeS, 'A').value)
print(dfs_search_stack(nodeA, 'A').value)
print(dfs_search_stack(nodeP, 'S').value)
print(dfs_search_stack(nodeH, 'R').value)
print(dfs_search_stack(nodeH, 'Z'))
'''


# =============== Weighted Graphs =====================

class GraphEdge(object):
    def __init__(self, destination_node, distance):
        self.node = destination_node
        self.distance = distance


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


# Test Graphs:

# Test Graph 1
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')
graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)

# Test Graph 2
node_1 = GraphNode('1')
node_2 = GraphNode('2')
node_3 = GraphNode('3')
graph_2 = Graph([node_1, node_2, node_3])
graph_2.add_edge(node_1, node_2, 5)
graph_2.add_edge(node_2, node_3, 5)
graph_2.add_edge(node_1, node_3, 10)

# Test Graph 3
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')
node_D = GraphNode('D')
node_E = GraphNode('E')
graph_3 = Graph([node_A, node_B, node_C, node_D, node_E])
graph_3.add_edge(node_A, node_B, 3)
graph_3.add_edge(node_A, node_D, 2)
graph_3.add_edge(node_B, node_D, 4)
graph_3.add_edge(node_B, node_E, 6)
graph_3.add_edge(node_B, node_C, 1)
graph_3.add_edge(node_C, node_E, 2)
graph_3.add_edge(node_E, node_D, 1)


# =============== Dijkstra's Shortest Path Algorithm =====================

def dijkstra(graph, start_node, end_node):
    """
    Find the shortest path from the source node to the end node by creating a dictionary that stores the shortest
    distances to all nodes.

    Time Complexity: O(n log n) because it uses a priority queue data structure.

    :param graph: Graph object with GraphNode objects with GraphEdge objects
    :param start_node: GraphNode object representing source node
    :param end_node: GraphNode object representing ending node
    :return:
    """

    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value
    # Assume the initial distance to all nodes is infinity except start_node which is 0
    distance_dict = {node: sys.maxsize for node in graph.nodes}
    distance_dict[start_node] = 0

    # Build a dictionary that will store the "shortest" distance to all nodes, wrt the start_node
    shortest_distance = {}

    while distance_dict:

        # Sort the distance_dict by min val and turn it into list of node,dist tuples
        # and pick 1st element in the list which is the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]

        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)

        # Check for each neighbour of current_node, if the distance_to_neighbour is smaller than the already stored
        # distance, update the distance_dict
        for edge in current_node.edges:
            if edge.node in distance_dict:

                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour

    return shortest_distance[end_node]


# Tests

# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))

# Shortest Distance from 1 to 3 is 10
print('Shortest Distance from {} to {} is {}'.format(node_1.value, node_3.value, dijkstra(graph_2, node_1, node_3)))

# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph_3, node_A, node_C)))


# =============== Uniform Cost Search =====================

def uniform_cost_search(start, goal):
    """
    Uninformed algo guaranteed to find shortest path between 2 nodes, but can have multiple goal nodes.
    Returns tuple of minimum path cost, path. Returns tuple -1, -1 if goal node is not found.

    Todo: refactor to enable multiple goals via goal list

    Notes: differs from Dijkstra's in that it doesn't check adjacents; it checks frontier, which is all adjacent
    unvisited nodes and all the end paths of the visited nodes

    :param goal: Object GraphNode
    :param start: Object GraphNode
    :return: tuple (int: path cost, list: path of GraphNode objects)
    """

    P_COST = 0
    PATH = 1

    visited = set()  # set of visited nodes
    min_q = {start: (0, [start])}  # store nodes in dict(min pri queue via sorted) as tuples of cumulative cost & path

    while min_q:

        # min priority queue= use sorted() to convert dict to list & sort on path cost in tuple
        # then get node w cheapest path cost at top of list/queue ([0])
        current_node, node_data = sorted(min_q.items(), key=lambda x: x[1][P_COST])[0]
        p_cost = node_data[P_COST]
        path = node_data[PATH]

        # print('node:', current_node.value, 'current p_cost:', p_cost,
        #      'current path:', ', '.join(map(lambda x: x.value, path)))

        min_q.pop(current_node)     # remove node from dict/min queue
        visited.add(current_node)   # & mark node as visited

        if current_node is goal:    # if smallest path found, return cost & path
            return p_cost, path
        else:                       # else, for each adjacent node, record cheapest path cost in min queue
            for edge in current_node.edges:
                child = edge.node
                if child not in visited:
                    new_p_cost = p_cost + edge.distance
                    # print('check node:', child.value, 'new p_cost:', new_p_cost)
                    if child in min_q and min_q[child][0] < new_p_cost:  # if existing path is smaller, don't overwrite
                        # print(child.value, 'exceeds')
                        continue
                    min_q[child] = (new_p_cost, path + [child])  # enqueue/update w smallest path costs

    return -1, -1  # goal node doesn't exist in graph


# Tests

# Shortest Distance from U to Y is 14
print('14 expected from {} to {} is {}'.format(node_u.value, node_y.value, *uniform_cost_search(node_u, node_y)))

# Shortest Distance from 1 to 3 is 10
print('10 expected from {} to {} is {}'.format(node_1.value, node_3.value, *uniform_cost_search(node_1, node_3)))

# Shortest Distance from A to C is 4
print('4 expected from {} to {} is {}'.format(node_A.value, node_C.value, *uniform_cost_search(node_A, node_C)))

# Shortest Distance from A to Y is -1 (y doesn't exist in this graph)
print('-1 expected from {} to {} is {}'.format(node_A.value, node_y.value, *uniform_cost_search(node_A, node_y)))


# =============== A* Search Algorithm =====================

def a_star_search(map_data, start, goal):
    """
    Informed algo guaranteed to find the shortest path between 2 nodes, assuming the heuristic function is admissible.

    :param map_data:
    :param start:
    :param goal:
    :return:
    """

    # use distance formula: sqrt( (x2-x1)^2 + (y2-y1)^2 )
    # to calculate distance:
        # between current state and the next state
        # current state and the goal state

    # map.intersections = {} where key is the intersection number & the value is x,y location
    # map.roads = [[]] where the index is the intersection # & the element is a list of connected intersections
    pass

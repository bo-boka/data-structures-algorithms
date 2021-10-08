
# from collections import deque
import collections
import sys
import heapq
import traceback
import haversine as hs


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


'''
# Tests

# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))

# Shortest Distance from 1 to 3 is 10
print('Shortest Distance from {} to {} is {}'.format(node_1.value, node_3.value, dijkstra(graph_2, node_1, node_3)))

# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph_3, node_A, node_C)))
'''


# =============== Uniform Cost Search =====================

def uniform_cost_search(start, goal):
    """
    Uninformed algo guaranteed to find shortest path between 2 nodes, but can have multiple goal nodes.
    Returns tuple of minimum path cost, path. Returns tuple -1, -1 if goal node is not found.

    Todo: refactor to enable multiple goals via goal list
    Todo: complexity

    Notes: differs from Dijkstra's in that it doesn't check adjacents; it checks frontier, which is all adjacent
    unvisited nodes and all the end paths of the visited nodes

    :param goal: Object GraphNode
    :param start: Object GraphNode
    :return: tuple (int: path cost, list: path of GraphNode objects)
    """

    P_COST = 0
    PATH = 1

    visited = set()  # set of visited nodes
    min_q = {start: (0, [start])}  # store nodes in dict(min pri queue via sorted) as tuples of path cost & path

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

        # else, for each adjacent node, record cheapest path cost in min queue
        for edge in current_node.edges:
            child = edge.node
            if child not in visited:
                new_p_cost = p_cost + edge.distance
                # print('check node:', child.value, 'new p_cost:', new_p_cost)
                if child in min_q and min_q[child][P_COST] < new_p_cost:  # if existing path is less don't overwrite
                    # print(child.value, 'exceeds')
                    continue
                min_q[child] = (new_p_cost, path + [child])  # enqueue/update w smallest path costs

    return -1, -1  # goal node doesn't exist in graph


'''
# Tests

# Shortest Distance from U to Y is 14
print('14 expected from {} to {} is {}'.format(node_u.value, node_y.value, *uniform_cost_search(node_u, node_y)))

# Shortest Distance from 1 to 3 is 10
print('10 expected from {} to {} is {}'.format(node_1.value, node_3.value, *uniform_cost_search(node_1, node_3)))

# Shortest Distance from A to C is 4
print('4 expected from {} to {} is {}'.format(node_A.value, node_C.value, *uniform_cost_search(node_A, node_C)))

# Shortest Distance from A to Y is -1 (y doesn't exist in this graph)
print('-1 expected from {} to {} is {}'.format(node_A.value, node_y.value, *uniform_cost_search(node_A, node_y)))
'''


# =============== Maps =====================

class Map(object):

    def __init__(self, intersections={}, roads=[]):
        self.intersections = intersections
        self.roads = roads

    def add_intersection(self, i_id, x, y):
        self.intersections[i_id] = [x, y]

    def add_update_road(self, r_id, vertices):
        self.roads[r_id] = vertices


# Test Map

map_intersections = {
 0: [0.7801603911549438, 0.49474860768712914],
 1: [0.5249831588690298, 0.14953665513987202],
 2: [0.8085335344099086, 0.7696330846542071],
 3: [0.2599134798656856, 0.14485659826020547],
 4: [0.7353838928272886, 0.8089961609345658],
 5: ['0.09088671576431506', 0.7222846879290787],
 6: [0.313999018186756, 0.01876171413125327],
 7: [0.6824813442515916, 0.8016111783687677],
 8: [0.20128789391122526, 0.43196344222361227],
 9: [0.8551947714242674, 0.9011339078096633],
 10: [0.7581736589784409, 0.24026772497187532],
 11: [0.25311953895059136, 0.10321622277398101],
 12: [0.4813859169876731, 0.5006237737207431],
 13: [0.9112422509614865, 0.1839028760606296],
 14: [0.04580558670435442, 0.5886703168399895],
 15: [0.4582523173083307, 0.1735506267461867],
 16: [0.12939557977525573, 0.690016328140396],
 17: [0.607698913404794, 0.362322730884702],
 18: [0.719569201584275, 0.13985272363426526],
 19: [0.8860336256842246, 0.891868301175821],
 20: [0.4238357358399233, 0.026771817842421997],
 21: [0.8252497121120052, 0.9532681441921305],
 22: [0.47415009287034726, 0.7353428557575755],
 23: [0.26253385360950576, 0.9768234503830939],
 24: [0.9363713903322148, 0.13022993020357043],
 25: [0.6243437191127235, 0.21665962402659544],
 26: [0.5572917679006295, 0.2083567880838434],
 27: [0.7482655725962591, 0.12631654071213483],
 28: [0.6435799740880603, 0.5488515965193208],
 29: [0.34509802713919313, 0.8800306496459869],
 30: [0.021423673670808885, 0.4666482714834408],
 31: [0.640952694324525, 0.3232711412508066],
 32: [0.17440205342790494, 0.9528527425842739],
 33: [0.1332965908314021, 0.3996510641743197],
 34: [0.583993110207876, 0.42704536740474663],
 35: [0.3073865727705063, 0.09186645974288632],
 36: [0.740625863119245, 0.68128520136847],
 37: [0.3345284735051981, 0.6569436279895382],
 38: [0.17972981733780147, 0.999395685828547],
 39: [0.6315322816286787, 0.7311657634689946]
}

map_roads = [
 [36, 34, 31, 28, 17],
 [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
 [39, 36, 21, 19, 9, 7, 4],
 [35, 20, 15, 11, 6],
 [39, 36, 21, 19, 9, 7, 2],
 [32, 16, 14],
 [35, 20, 15, 11, 1, 3],
 [39, 36, 22, 21, 19, 9, 2, 4],
 [33, 30, 14],
 [36, 21, 19, 2, 4, 7],
 [31, 27, 26, 25, 24, 18, 17, 13],
 [35, 20, 15, 3, 6],
 [37, 34, 31, 28, 22, 17],
 [27, 24, 18, 10],
 [33, 30, 16, 5, 8],
 [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
 [37, 30, 5, 14],
 [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
 [31, 27, 26, 25, 24, 1, 10, 13, 17],
 [21, 2, 4, 7, 9],
 [35, 26, 1, 3, 6, 11, 15],
 [2, 4, 7, 9, 19],
 [39, 37, 29, 7, 12],
 [38, 32, 29],
 [27, 10, 13, 18],
 [34, 31, 27, 26, 1, 10, 15, 17, 18],
 [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
 [31, 1, 10, 13, 18, 24, 25, 26],
 [39, 36, 34, 31, 0, 12, 17],
 [38, 37, 32, 22, 23],
 [33, 8, 14, 16],
 [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
 [38, 5, 23, 29],
 [8, 14, 30],
 [0, 12, 17, 25, 26, 28, 31],
 [1, 3, 6, 11, 15, 20],
 [39, 0, 2, 4, 7, 9, 28],
 [12, 16, 22, 29],
 [23, 29, 32],
 [2, 4, 7, 22, 28, 36]
]

map_1 = Map(map_intersections, map_roads)


# =============== A* Search Algorithm =====================

def get_distance(s, e):
    """
    Compute distance between two points using Haversine Distance formula.
    :param s: list of x,y coordinates
    :param e: list of x,y coordinates
    :return: int of distance between coordinates
    """
    try:
        distance = hs.haversine(tuple(s), tuple(e))
    except Exception:
        raise Exception("Error computing distance. Invalid Coordinates: {} or {}".format(s, e))

    return distance


def a_star_search(map_data, start, goal):
    """
    Informed algo guaranteed to find the shortest path between 2 nodes with admissible heuristic function.

    :param map_data: object containing intersections (dict with x,y plots) & roads (unweighted adjacency list)
    :param start: int of start node id
    :param goal: int of goal node id
    :return: list of intersections representing smallest path
    """
    if type(start) is not int:
        raise TypeError("Start parameter is a non-integer value.")
    if type(goal) is not int:
        raise TypeError("Goal parameter is a non-integer value.")

    try:
        goal_location = map_data.intersections[goal]
    except KeyError:
        return "Goal intersection does not exist."

    F_COST = 1  # constant for readability
    visited = set()  # set of visited intersections
    min_q = {start: (0, 0, [start])}  # store nodes in dict(min pri queue via sorted) w true cost, estimated cost & path

    while min_q:

        # min priority queue= use sorted() to convert dict to list & sort on estimated path cost in tuple
        # then get node w cheapest estimated path cost at top of list/queue ([0])
        intersection, node_data = sorted(min_q.items(), key=lambda x: x[1][F_COST])[0]
        p_cost, f_cost, path = node_data

        # print('node:', intersection, 'current p_cost:', p_cost, 'f_cost', f_cost,
        #      'current path:', path)

        min_q.pop(intersection)     # remove node from dict/min queue
        visited.add(intersection)   # & mark node as visited

        if intersection is goal:    # if smallest path found, return path
            return path

        try:
            roads = map_data.roads[intersection]
        except IndexError:
            return "Intersection does not exist or cannot be reached by roads."

        # else, for each adjacent node, record cheapest path cost, estimated cost, & path in min queue
        for connection in roads:
            if connection not in visited:

                # data validation
                if type(intersection) is not int or type(connection) is not int:
                    raise TypeError("Road data contains non-integer value(s).")

                # get location coordinates from map
                try:
                    current_location = map_data.intersections[intersection]
                    state_destination = map_data.intersections[connection]
                except KeyError:
                    return "Road data is missing intersection(s)."

                # get distance between states & estimated goal distance
                edge_distance = get_distance(current_location, state_destination)
                h_estimated_distance = get_distance(state_destination, goal_location)

                # calculate costs
                g_true_cost = p_cost + edge_distance
                f_total_cost = g_true_cost + h_estimated_distance

                # if existing path is less don't overwrite in min queue
                if connection in min_q and min_q[connection][F_COST] < f_total_cost:
                    continue

                # enqueue/update w smallest path costs
                min_q[connection] = (g_true_cost, f_total_cost, path + [connection])

    raise Exception("Unexpected Error.")


print(a_star_search(map_1, 5, 34))  # expected: [5, 16, 37, 12, 34]
'''
print(a_star_search(map_1, 101, 34))  # expected: error message
print(a_star_search(map_1, False, 34))  # expected: error message
print(a_star_search(map_1, 5, 101))  # expected: error message
print(a_star_search(map_1, 5, "bear"))  # expected: error message
print(a_star_search(map_1, 5, -1))  # expected: error message
print(a_star_search(map_1, 5, False))  # expected: error message
'''


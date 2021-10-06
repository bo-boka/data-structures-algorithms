
import math
import collections
import sys
import heapq

# =============== Dijkstra's Shortest Path Algorithm =====================


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
    distance_dict = {node: math.inf for node in graph.nodes}
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
# Test Case 1:

# Create a graph
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

# add_edge() function will add an edge between node1 and node2 in both directions
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)

# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))

# Test Case 2
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')

graph = Graph([node_A, node_B, node_C])

graph.add_edge(node_A, node_B, 5)
graph.add_edge(node_B, node_C, 5)
graph.add_edge(node_A, node_C, 10)

# Shortest Distance from A to C is 10
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))


# Test Case 3
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')
node_D = GraphNode('D')
node_E = GraphNode('E')

graph = Graph([node_A, node_B, node_C, node_D, node_E])

graph.add_edge(node_A, node_B, 3)
graph.add_edge(node_A, node_D, 2)
graph.add_edge(node_B, node_D, 4)
graph.add_edge(node_B, node_E, 6)
graph.add_edge(node_B, node_C, 1)
graph.add_edge(node_C, node_E, 2)
graph.add_edge(node_E, node_D, 1)

# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))
'''


# =============== Dijkstra's - Inefficient Implementation =====================

class Graph2:
    def __init__(self):
        self.nodes = set()  # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # lets make the graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


def dijkstra_inefficient(graph, source):
    """
    Find the shortest path from the source node to every other node in the given graph.
    This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a O(n^2) time complexity.
    The alternate version above has O(n log n) time complexity because it uses a priority queue data structure.
    :param graph: graph object
    :param source: starting node
    :return: result dictionary of shortest paths to each node from starting node
    """

    # Declare and initialize result, unvisited, and path
    result = {source: 0}
    for node in graph.nodes:
        if node != source:
            result[node] = sys.maxsize
    unvisited = set(graph.nodes)
    path = {}

    # As long as unvisited is non-empty
    while unvisited:
        min_node = None

        # Find the unvisited node having smallest known distance from the source node.
        # When beginning, this will end up being A = 0
        for node in unvisited:
            if node in result:

                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        current_distance = result[min_node]

        # Calculate distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]

                # If new distance is smaller than already known distance, update results & path
                if neighbour not in result or distance < result[neighbour]:
                    result[neighbour] = distance
                    path[neighbour] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result

'''
# Test 1
testGraph = Graph2()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

print(dijkstra_greedy(testGraph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

print(dijkstra_greedy(graph, 'A'))  # {'A': 0, 'C': 10, 'B': 5}

# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

print(dijkstra_greedy(graph, 'A'))  # {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
'''


# =============== Minimum Train Platforms =====================

def min_platforms(arrival, departure):
    """
    Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number
    of platforms required so that no train has to wait for the other(s) to leave. In other words, when a train is
    about to arrive, at least one platform must be available to accommodate it.

    You will be given arrival and departure times both in the form of a list. The size of both the lists will
    be equal, with each common index representing the same train.
    Note: Time hh:mm would be written as integer hhmm for e.g. 13:45 would be written as 1345.

    Example:
    Input: A schedule of 6 trains:
        arrival = [900,  940, 950,  1100, 1500, 1800]
        departure = [910, 1200, 1120, 1130, 1900, 2000]
    Expected output: Minimum number of platforms required = 3

    The Greedy Approach:
        Sort the schedule, and make sure when a train arrives or departs, keep track of the required number of
        platforms. We will have iterator i and j traversing the arrival and departure lists respectively.
        At any moment, the difference (i - j) will provide us the required number of platforms.

        At the time of either arrival or departure of a train, if i^th arrival is scheduled before the j^th departure,
        increment the platform_required and i as well. Otherwise, decrement platform_required count, and increase j.
        Keep track of the max value of platform_required ever, as the expected result.

    :param: arrival - list of arrival time
    :param: departure - list of departure time
    :return: minimum number of platforms (int) required so that no train has to wait for other(s) to leave
    """
    if len(arrival) != len(departure):  # Mismatch in the length of the lists
        return -1

    # Sort both the lists.
    arrival.sort()
    departure.sort()

    platform_required = 1  # Count of platforms required at the moment when comparing i^th arrival and j^th departure
    max_platform_required = 1  # Keep track of the max value of platform_required

    # Iterate such that (i-j) will represent platform_required at that moment
    i = 1
    j = 0

    # Traverse the arrival list with iterator `i`, and departure with iterator `j`.
    while i < len(arrival) and j < len(arrival):

        # if i^th arrival is scheduled before than j^th departure,
        # increment platform_required and i as well.
        if arrival[i] < departure[j]:
            platform_required += 1
            i += 1

            # Update the max value of platform_required
            if platform_required > max_platform_required:
                max_platform_required = platform_required

        # Otherwise, decrement platform_required count, and increase j.
        else:
            platform_required -= 1
            j += 1

    return max_platform_required

'''
def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
'''


# =============== Minimum Operations =====================

def min_operations(target):
    """
    Starting from the number 0, find the minimum number of operations required to reach a given positive target number.
    You can only use the following two operations:

        1. Add 1
        2. Double the number

    Example:
        For Target = 18, output = 6, because it takes at least 6 steps shown below to reach the target

        start = 0
        step 1 ==> 0 + 1 = 1
        step 2 ==> 1 * 2 = 2 # or 1 + 1 = 2
        step 3 ==> 2 * 2 = 4
        step 4 ==> 4 * 2 = 8
        step 5 ==> 8 + 1 = 9
        step 6 ==> 9 * 2 = 18

    Approach:
        -start backwards from the target
        -if target is odd --> subtract 1
        -if target is even --> divide by 2

    input: target number (as an integer)
    output: number of steps (as an integer)
    """

    steps = 0

    while target != 0:
        if target % 2 == 0:
            target //= 2
        else:
            target -= 1
        steps += 1

    return steps

# print(min_operations(69))


# =============== Prim's Minimum Spanning Tree =====================

def create_graph_adjacency_list(vertices, edge_data):
    """
    Create a graph in the form of and adjacency list, which means each index is the id of the vertex and it's element is
    a list of tuples where the first element in the tuple is the connecting node id and the second element is the weight
    :param vertices: number of vertices
    :param edge_data: list of lists with 3 elements per nested list:
        1. id of starting island
        2. id of connecting island
        3. cost of connection
        Example: bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
    :return: two dimensional list that is a graph in adjacency list form
    """

    VERTEX_1 = 0
    VERTEX_2 = 1
    WEIGHT = 2

    graph = [[] for _ in range(vertices+1)]

    for edge in edge_data:
        graph[edge[VERTEX_1]].append((edge[VERTEX_2], edge[WEIGHT]))
        graph[edge[VERTEX_2]].append((edge[VERTEX_1], edge[WEIGHT]))

    return graph


def prims_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    In an ocean with n islands connected via bridges that each have a toll, find bridge path in such a way that all
    islands are connected with minimum cost of travelling, given a number of island and a list of bridge data.

    You can assume that there is at least one possible way in which all islands are connected with each other.

    This is one possible solution to the infamous Travelling Salesman Problem

    :param: num_islands - number of islands
    :param: bridge_config - list of lists with 3 elements per nested list:
        1. id of starting island
        2. id of connecting island
        3. cost of connection
        Example: bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
    :return: cost (int) minimum cost of connecting all islands
    """

    graph = create_graph_adjacency_list(num_islands, bridge_config)
    start_vertex = 1
    min_heap = [(0, start_vertex)]
    visited = [False for _ in range(num_islands+1)]
    total = 0

    while min_heap:

        cost, current_vertex = heapq.heappop(min_heap)

        if visited[current_vertex]:
            continue

        total += cost

        for neighbor, cost in graph[current_vertex]:
            heapq.heappush(min_heap, (cost, neighbor))

        visited[current_vertex] = True

    return total

# print(prims_minimum_cost_of_connecting(4, [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]))


# ===================== Knapsack Problem (Multiple Solutions) =============================

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


# ------- Naive Implementation ------------

def knapsack_naive(knapsack_max_weight, items):
    last_index = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, last_index)


def knapsack_recursive(capacity, items, lastIndex):
    """
    Time Complexity is O(2^n), exponential time. Very inefficient.
    This can be reduced to O(nM) by using dynamic programming to implement memoization with a lookup table.
    :param capacity: capacity remaining
    :param items: list of named tuples for item weights and values
    :param lastIndex: index of items list
    :return:
    """
    # Base case
    if (capacity <= 0) or (lastIndex < 0):
        return 0

    # Put the item in the knapsack
    valueA = 0
    if items[lastIndex].weight <= capacity:
        valueA = items[lastIndex].value + knapsack_recursive(capacity - items[lastIndex].weight, items, lastIndex - 1)

    # Do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)

    # Pick the maximum of the two results
    result = max(valueA, valueB)

    return result


# ------- Efficient Iterative Implementation ------------

def knapsack_max_value(knapsack_max_weight, items):
    """
    Time complexity is O(nM) where n is number of given items and M is the max capacity.
    :param knapsack_max_weight:
    :param items:
    :return:
    """
    # Initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:

        # The "capacity" represents amount of remaining capacity (kg) of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)):

            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]


# ------- Efficient Recursive Implementation ------------

def knapsack(weight_limit, items):
    """
    Given a knapsack that can only carry a certain amount of weight and a list of items with an associated weight and
    value for each, find the max value of items that the knapsack can carry without exceeding the weight limit.

    This is a greedy algorithm that uses dynamic programming to achieve optimal time complexity. We're using recursion
    to break the problem into smaller sub-problems and then using memoization to store the max value in a dictionary for
    a certain remaining capacity called with a certain index.

    Because we're only calling the function once for each capacity-index combination, and the capacity is an integer
    rather than a list size, the time complexity is O(nW) where n is the number of items and W is the weight limit. The
    complexity is pseudo-polynomial for those reasons. The data structure reduces the complexity from exponential.

    :param weight_limit: max capacity
    :param items: list of named tuples with weight and value
    :return: max value
    """

    def ks_recur(capacity, idx):
        """
        Use recursion to find and store the max value for each combination of indices with remaining capacity.

        :param capacity: remaining capacity left
        :param idx: current index of items list
        :return: max value
        """

        # if combo already exists in cache, return that
        if (capacity, idx) in cache.keys():
            return cache[(capacity, idx)]

        # base case where capacity has been met or sequence has been traversed
        if capacity <= 0 or idx < 0:
            return 0

        # if current item weight will exceed capacity, do not add it
        if items[idx].weight > capacity:
            result = ks_recur(capacity, idx-1)
        # find max value for item added vs not added
        else:
            val_a = items[idx].value + ks_recur(capacity-items[idx].weight, idx-1)
            val_b = ks_recur(capacity, idx-1)
            result = max(val_a, val_b)

        # add combo to cache before returning max result
        cache[(capacity, idx)] = result
        return result

    cache = dict()
    last_idx = len(items)-1
    max_value = ks_recur(weight_limit, last_idx)
    return max_value

'''
tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
'''

'''
items_2 = [Item(10, 7), Item(9, 8), Item(5, 6)]
print(knapsack(15, items_2))

items = [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]
print(knapsack(25, items))
'''


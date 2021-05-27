
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
        self.map = dict()
        self.data_removal_list = []

    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            out_string += str(node.value)
            if node.next:
                out_string += " -> "
            else:
                out_string += '\n'
            node = node.next
        return out_string

    def append(self, value):

        if value in self.map:
            return

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
        self.tail = self.map[value] = new_node
        self.size += 1

    def remove(self, value):
        node = self.map[value]

        if node is self.head:
            if node.next:
                self.head = node.next
                node.next.previous = None
            else:
                self.head = None
        elif node is self.tail:
            self.tail = node.previous
            node.previous.next = None
        else:
            node.previous = node.next

        self.data_removal_list.append(value)
        self.size -= 1

    def clean_map(self):
        for del_val in self.data_removal_list:
            del self.map[del_val]


def union(llist_1, llist_2):
    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1

    llist_1.tail.next = llist_2.head
    llist_2.head.previous = llist_1.tail
    llist_1.tail = llist_2.tail

    return llist_1


def intersection(llist_1, llist_2):

    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1

    # get smaller llist to iterate & transform to intersection
    intersected_llist = llist_1
    hash_llist = llist_2
    if llist_1.size > llist_2.size:
        intersected_llist = llist_2
        hash_llist = llist_1

    for item in intersected_llist.map.keys():
        # if hash_llist.map.has_key(item):
        if item not in hash_llist.map:
            intersected_llist.remove(item)

    intersected_llist.clean_map()

    return intersected_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(f'test1 union: {union(linked_list_1,linked_list_2)}')
print(f'test1 intersect: {intersection(linked_list_1,linked_list_2)}')

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(f'test2 union: {union(linked_list_3,linked_list_4)}')
print(f'test2 intersect: {intersection(linked_list_3,linked_list_4)}')
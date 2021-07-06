
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


def union(llist_1, llist_2):

    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1

    union_llist = LinkedList()
    for l1_item in llist_1.map.keys():
        union_llist.append(l1_item)
    for l2_item in llist_2.map.keys():
        union_llist.append(l2_item)

    return union_llist


def intersection(llist_1, llist_2):

    if llist_1.head is None:
        return ''
    if llist_2.head is None:
        return ''

    # get smaller llist to iterate & transform to intersection
    i_itr_llist = llist_1
    i_hash_llist = llist_2
    if llist_1.size > llist_2.size:
        i_itr_llist = llist_2
        i_hash_llist = llist_1

    intersected_llist = LinkedList()
    for item in i_itr_llist.map.keys():
        if item in i_hash_llist.map:
            intersected_llist.append(item)

    return intersected_llist


# Test case 1
print('======== Test 1: Happy Path')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(f'test1 union: {union(linked_list_1,linked_list_2)}')                 # LL string: 3,2,4,35,6,65,21,32,9,1,11
print(f'test1 intersection: {intersection(linked_list_1,linked_list_2)}')   # LL string: 4,6,21


# Test case 2
print('======== Test 2: empty intersection')

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(f'test2 union: {union(linked_list_3,linked_list_4)}')                 # LL string: 3,2,4,35,6,65,23,1,7,8,9,11,21
print(f'test2 intersection: {intersection(linked_list_3,linked_list_4)}')   # empty string


# Test case 3
print('======== Test 3: first list empty')

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(f'test3 union: {union(linked_list_5,linked_list_6)}')                 # LL string: 1,7,8,9,11,21
print(f'test3 intersection: {intersection(linked_list_5,linked_list_6)}')   # empty string


# Test case 4
print('======== Test 4: second list empty list')

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(f'test4 union: {union(linked_list_7,linked_list_8)}')                 # LL string: 3,2,4,35,6,65,23
print(f'test4 intersection: {intersection(linked_list_7,linked_list_8)}')   # empty string


# Test case 5
print('======== Test 5: both lists empty')

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(f'test4 union: {union(linked_list_7,linked_list_8)}')                 # empty string
print(f'test4 intersection: {intersection(linked_list_7,linked_list_8)}')   # empty string

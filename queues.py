
# ========Queue via Array======


# using array has a time complexity of O(n) because we have to traverse to increase capacity
class QueueList:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1  # since the front won't always be at 0, use -1 to denote no elements, whereas 0 would imply an item exists
        self.queue_size = 0

    def enqueue(self, value):
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        self.arr[self.next_index] = value
        self.next_index = (self.next_index + 1) % len(self.arr)  # wrap around array
        self.queue_size += 1
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            self.next_index = 0
            self.front_index = -1
            return None

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)  # wrap around array
        self.queue_size += 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size

    def front(self):
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr) *2)]

        index = 0

        # populate from wherever front index  is
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1
        # populate from start of array to front index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index


# =======Queue via Linked List======

# using Linked List  has O(1) capacity because we're not traversing;
#   just referencing the head & tail to dequeue & enqueue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return val

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


# =====Queue via Stack==========

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class QueueStack:
    def __init__(self):
        self.instorage = Stack()
        self.outstorage = Stack()

    def size(self):
        return self.outstorage.size() + self.instorage.size()

    def enqueue(self, item):
        self.instorage.push(item)

    def dequeue(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()


class QueuePy:

    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.pop(0)


def reverse_queue(queue):
    """
    Reverse the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """

    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())


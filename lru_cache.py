

class LRU_Cache(object):
    """
    Design a cache with a capacity that stores key value pairs and retrieves values from a given key.
    When the capacity is reached, remove the least recently used data before storing the new data.
    If an element doesn't exist (cache miss), return -1.
    All operations must take O(1) time.

    Notes: Maps take constant time but are not ordered to be able to check recently used elements.
        Can use a queue to keep track of element use but only the head and tail are O(1) time.
        Accessing a middle element will be O(n) time.
        Solution is to store queue data in the map.
    """

    PREV = 0
    NEXT = 1
    KEY = 2
    VALUE = 3

    def __init__(self, capacity=5):

        # throw error if capacity is set to 1 or below
        if capacity < 2:
            raise ValueError("Cache capacity must be larger than 1.")

        # Initialize class variables
        self.limit = capacity
        self.size = 0
        self.map = dict()
        self.head = [None, None, None, None]
        self.tail = self.head

    def get(self, key):

        # Return -1 if nonexistent.
        data = self.map.get(key)
        if data is None:
            return -1

        # Move item to top of queue before returning
        if data != self.tail:  # if tail, value is already top of queue

            if data == self.head:  # remove node from head
                self.head[self.NEXT][self.PREV] = None
                self.head = self.head[self.NEXT]
            else:  # remove node from chain
                data[self.NEXT][self.PREV] = data[self.PREV]
                data[self.PREV][self.NEXT] = data[self.NEXT]

            # add value to top of queue (tail)
            data[self.NEXT] = None
            data[self.PREV] = self.tail
            self.tail[self.NEXT] = data
            self.tail = data

        # Retrieve item from provided key.
        return data[self.VALUE]

    def set(self, key, value):

        # if key already in data set, get() moves it to top of queue
        val = self.get(key)
        if val != -1:  # key already in data set
            return

        # set first element in queue & map
        if self.head[self.KEY] is None:
            self.head = [None, None, key, value]
            self.tail = self.head
            self.map[key] = self.head
            self.size += 1
            return

        # If the cache is at capacity remove the oldest item from map & head of queue & adjust pointers
        if self.size >= self.limit:
            # remove oldest item from map
            rm_key = self.head[self.KEY]
            del self.map[rm_key]
            # remove oldest item from queue
            self.head[self.NEXT][self.PREV] = None
            self.head = self.head[self.NEXT]
            self.size -= 1

        # Add new key to map & tail of queue & adjust pointers
        new_data = [self.tail, None, key, value]
        self.tail[self.NEXT] = new_data
        self.tail = new_data
        self.map[key] = new_data
        self.size += 1

    def get_size(self):
        return self.size


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# print(our_cache.get(1))
# print(our_cache.get(2))
print(our_cache.get(4))
print(our_cache.get(5))
print(our_cache.get(6))
print(our_cache.get(4))
print(our_cache.get(1))
our_cache.set(9, 9)
print(our_cache.get(2))
print(our_cache.get(9))



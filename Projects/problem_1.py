

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

        # validate input
        if type(value) == str:
            try:
                value = int(value)
            except ValueError:
                pass
        if type(value) == int and value < 0:
            raise ValueError("Value must be a non-negative number.")

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


# Test case 1
print('======== Test 1: Happy Path')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(4))     # returns 4
print(our_cache.get(5))     # returns 5
print(our_cache.get(1))     # returns 1
our_cache.set(9, 9)
print(our_cache.get(2))     # returns -1 since 2 was least recently used
print(our_cache.get(9))     # returns 9


# Test case 2
print('======== Test 2: Invalid input')
try:
    cache_2 = LRU_Cache(0)  # raises a ValueError
except ValueError as e:
    print(e)

# Test case 3
print('======== Test 3: Invalid input')
try:
    cache_3 = LRU_Cache(1)  # raises a ValueError
except ValueError as e:
    print(e)

# Test case 4
print('======== Test 4: Large cache limit')
cache_4 = LRU_Cache(50)
cache_4.set(1, 1)
cache_4.set(2, 2)
cache_4.set(3, 3)
cache_4.set(4, 4)
cache_4.set(5, 5)
cache_4.set(6, 6)
cache_4.set(7, 7)
cache_4.set(8, 8)
cache_4.set(9, 9)

print(cache_4.get(1))       # returns 1
print(cache_4.get(2))       # returns 2
print(cache_4.get(9))       # returns 9


# Test case 5
print('======== Test 5: setting non-number values')
cache_5 = LRU_Cache(5)
print(cache_5.get(True))
cache_5.set("dolphin", "ocean")
print(cache_5.get("dolphin"))
cache_5.set(True, False)
print(cache_5.get(True))


# Test case 6
print('======== Test 6: setting negative/invalid integers & strings')
cache_6 = LRU_Cache(5)
try:
    cache_6.set(-1,"-1")    # raises a ValueError
except ValueError as e:
    print(e)
try:
    cache_6.set(-2,-2)      # raises a ValueError
except ValueError as ex:
    print(ex)
print(cache_6.get(-1))

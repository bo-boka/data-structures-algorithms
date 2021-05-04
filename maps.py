
# ======= Dictionaries are Python's built-in HashMaps

locations = {'North America': {'USA': ['Mountain View']}}

locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia']['China'] = ['Shanghai']
# print all Asian cities, formatted & alphabetically sorted
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))
sorted_asian_cities = sorted(asia_cities)
# [print(city) for city in sorted_asian_cities]


# ================ Hash Map ======================

# ---- Linked List used for Separate Chaining ----
class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31  # prime numbers, usually 37 or 31 (31 is the convention but not perfect for every case)
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        """
        In case of collision, the `put()` function uses the same bucket to store a linked list of key-value pairs.
        Every bucket will have it's own separate chain of linked list nodes.
        Because we have a sophisticated hashing function that spreads out data over buckets, the time complexity is
        O(1). But without that hashing function, worst case could be O(n)
        :param key: string
        :param value: integer
        :return:
        """
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]  # create a reference that points to the existing bucket

        # check if the key is already in the map, & UPDATE its value
        # key should always be unique
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        '''
            If the key is a new one, hence not found in the chain (LinkedList), then following two cases arise:
             1. The key has generated a new bucket_index,
             2. The key has generated an existing bucket_index. 
                This event is a Collision, i.e., two different keys have same bucket_index.
            In both the cases, we will prepend the new node (key, value) at the beginning (head) of the chain (LinkedList).
            Remember that each `bucket` at position `bucket_index` is actually a chain (LinkedList) with 1 or more nodes. 
        '''
        head = self.bucket_array[bucket_index]
        new_node.next = head   # prepend the new node in the beginning of the linked list
        self.bucket_array[bucket_index] = new_node  # make new node the bucket reference
        self.num_entries += 1

        # check load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)  # the returned hash code will be the bucket index

    def get_hash_code(self, key):
        """
        One of the most popular string hash functions is to use a prime number (because it provides good distribution,
        commonly 31 or 37) to the power of n ascending, each time multiplying it by each character's ASCII value.
        Compress numbers so that output used as array index won't create large array
        :param key: string
        :return: integer
        """
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1  # represents (self.p^0) which is 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code w/ modulus
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient as well
        return hash_code % num_buckets  # compress again, generated hash code will be the bucket index

    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)  # we can use put() to rehash
                head = head.next

    def delete(self, key):

        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]  # create a ref that points to the existing bucket, which is head node

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

    def __repr__(self):
        output = "\nLet's view the hash map:"
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
        return output



hash_map = HashMap()
#hash_map.put("one", 1)
#hash_map.put("two", 2)
#hash_map.put("three", 3)  # will generate the same bucket_index as four
#hash_map.put("four", 4)
#hash_map.put("neo", 11)
#hash_map.put("neyo", 12)
#hash_map.put("eight", 8)
#hash_map.put("five", 5)
#hash_map.put("six", 6)
#hash_map.put("seven", 7)
#hash_map.put("nine", 9)
#hash_map.put("ten", 10)
#hash_map.delete("neyo")
#print(hash_map)


# ============ Hash Table (implemented as Hash Set)======================

class HashTable:

    def __init__(self):
        self.table = [None] * 10000
        self.h_num = 100

    def store(self, string):
        """
        stores the string in an existing bucket or creates a new bucket
        :param string:
        :return: NONE
        """
        hash_v = self.calculate_hash_value(string)

        if self.lookup(string) != -1:
            return

        if self.table[hash_v]:  # array is not empty
            self.table[hash_v].append(string)
        else:
            self.table[hash_v] = [string]

    def lookup(self, string):
        """
        :param string: string to search
        :return: hash value of the string if it exists. Otherwise returns -1
        """
        hash_v = self.calculate_hash_value(string)

        if self.table[hash_v]:  # check if bucket is empty
            if string in self.table[hash_v]:  # check string in bucket
                return hash_v
        return -1

    def calculate_hash_value(self, string):
        """
        Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
        :param string:
        :return:
        """
        first_char = ord(string[0].upper())
        second_char = ord(string[1].upper())
        hash_v = first_char * self.h_num + second_char
        return hash_v


hash_table = HashTable()
#print('---hash table ----')
#print(hash_table.calculate_hash_value('Udacity'))
#print(hash_table.lookup('Udacity'))
#hash_table.store('Udacity')
#print(hash_table.lookup('Udacity'))

# ============ Caching to Optimize =============

# -------- Original recursive function before optimization ------------------
def staircase(n):
    """
    Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many
    possible ways can you climb the staircase if the staircase has n steps?
        Examples:
            n == 3 then answer = 4 The output is 4 because there are four ways we can climb the stair-case:
                1 step + 1 step + 1 step
                1 step + 2 steps
                2 steps + 1 step
                3 steps
            n == 5 then answer = 13
    param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    """
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Re
    # Recursive Step - Split the solution into base case if n > 3.

    if n <= 0:
        return 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4


# -------- After optimizing with Caching ------------

def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)


def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output = staircase_faster(n - 1, num_dict)

        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)

        output = first_output + second_output + third_output

    num_dict[n] = output
    return output


def pair_sum_to_target(input_list, target):
    """
    find the 2 indices that hold the values that sum the target
    :param input_list: list of values
    :param target: sum to find
    :return: list of indices that equal the sum
    """

    my_dict = dict()
    for i, val in enumerate(input_list):
        if target - val in my_dict:
            return [my_dict[target-val], i]
        my_dict[val] = i
    return [-1]


def longest_consecutive_subsequence(input_list):
    """
    find the longest list of consecutive numbers and return them in an ordered list
    :param input_list: list of random natural numbers
    :return: list of consecutive numbers in order
    """
    # Create a dictionary of input_list where element is key & index is val
    element_dict = dict()
    # Time complexity = O(n)
    for index, element in enumerate(input_list):
        element_dict[element] = index

    # Represents the length of longest subsequence
    max_length = -1
    # Represents the index of smallest element in the longest subsequence
    starts_at = -1

    # Traverse again: Time complexity = O(n)
    for index, element in enumerate(input_list):

        current_starts = index
        element_dict[element] = -1  # Mark as visited
        current_count = 1  # length of the current subsequence

        '''CHECK ONE ELEMENT FORWARD'''
        current = element + 1  # `current` is the expected number

        # check if the expected number is available (as a key) in the dictionary,
        # and it has not been visited yet (i.e., value > 0)
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        while current in element_dict and element_dict[current] > 0:
            current_count += 1  # increment the length of subsequence
            element_dict[current] = -1  # Mark as visited
            current = current + 1

        '''CHECK ONE ELEMENT BACKWARD'''
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        current = element - 1  # `current` is the expected number

        while current in element_dict and element_dict[current] > 0:
            current_starts = element_dict[current]  # index of smallest element in the current subsequence
            current_count += 1  # increment the length of subsequence
            element_dict[current] = -1
            current = current - 1

        '''If length of current subsequence >= max length of previously visited subsequence'''
        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts  # index of smallest element in the current (longest so far) subsequence
            max_length = current_count  # store the length of current (longest so far) subsequence

    start_element = input_list[starts_at]  # smallest element in the longest subsequence

    # return a NEW list starting from `start_element` to `(start_element + max_length)`
    return [element for element in range(start_element, start_element + max_length)]

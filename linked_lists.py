#=========SINGLEY LINKED LISTS===========

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    # LinkedList.append() has O(N) complexity since looping through all values to find tail
    def append(self, value):
        """Append a value to the end of the linked list."""
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)

    # LinkedList.prepend() has O(1) complexity
    def prepend(self, value):
        """Prepend a value to the beginning of the LinkedList."""
        if self.head is None:
            self.head = Node(value)
            return

        node = Node(value)
        node.next = self.head
        self.head = node

    def to_list(self):
        """Converts a linked list to a Python list."""
        node = self.head
        out_list = []
        while node:
            is_ll = isinstance(node.value, LinkedList)
            if (is_ll):
                str_list = node.value.to_list()
                out_list.append((str_list))
            else:
                out_list.append(node.value)
            #out_list.append(int(str(node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        return out_list

    def search(self, value):
        """Search linked list for value and return Node. Raise error otherwise."""
        current = self.head
        if current is None:
            raise ValueError("There are no values in the list.")
        while current:
            if current.value == value:
               return current
            current = current.next
        raise ValueError("Value not found in the list.")

    def remove(self, value):
        """Removes first occurrence of value."""
        current = self.head
        if current is None:
            raise ValueError("There are no values in the list.")
        if current.value == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def pop(self, value):
        """returns the first Node's value and removes it from the list"""
        if self.head is None:
            return
        node = self.head
        self.head = self.head.next
        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        current = self.head
        if current is None:
            return
        if pos == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        idx = 1
        while current.next:
            if idx == pos:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            idx += 1
            current = current.next
        new_node = Node(value)
        current.next = new_node

    def size(self):
        """ Return the size or length of the linked list. """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


#defining a function outside class & adding it

# LinkedList.prepend() has O(1) complexity
def prepend(self, value):
    """Prepend a value to the beginning of the LinkedList."""
    if self.head is None:
        self.head = Node(value)
        return

    node = Node(value)
    node.next = self.head
    self.head = node
#this adds the function to the class
LinkedList.prepend = prepend


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


#=========DOUBLY LINKED LISTS===========

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # DoublyLinkedList.append() has O(1) complexity
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


#=========CIRCULARLY LINKED LISTS===========

#(after creating ll class and node class)
list_with_loop = LinkedList(Node(2))
list_with_loop.append(-1)
list_with_loop.append(3)
list_with_loop.append(0)
list_with_loop.append(5)

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next
node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not
    The idea is to have one index moving slowly and another moving fast so that
    the fast one will circle around and eventually equal the slow one

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    if linked_list.head is None:
        return
    node = linked_list.head
    fast = linked_list.head.next
    while node and fast:
        if node == fast:
            return True
        node = node.next
        fast = fast.next.next
        if node.value == -4:
            return
    return False

#========= Algos ==========

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """

    new_ll = LinkedList()
    prev_node = None

    #each new node points to the previous and the last one is made the head
    for i in linked_list:
        new_node = Node(i)
        new_node.next = prev_node
        prev_node = new_node
    new_ll.head = prev_node
    return new_ll


# Flattening sorted nested linked list (linked list with other sorted linked lists as the elements)
# ================================================================================================


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two sorted linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList and those linked lists must be sorted.
    The merge() function must return an instance of LinkedList.
    '''

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    node1 = list1.head
    node2 = list2.head
    new_ll = None
    if node1.value < node2.value:
        new_ll = LinkedList(node1)
        node1 = node1.next
    else:
        new_ll = LinkedList(node2)
        node2 = node2.next
    new_node = new_ll.head
    while node1:
        if node2 is None: #add the rest of node1s to new_ll
            new_node.next = node1
            return new_ll
        if node1.value < node2.value:
            new_node.next = node1
            new_node = new_node.next
            node1 = node1.next
        else:
            new_node.next = node2
            new_node = new_node.next
            node2 = node2.next
        print('current new_ll: {}'.format(new_ll.to_list()))
    if node2: #add the rest of node2s to new_ll
        print('add rest of list2 to {}'.format(new_ll.to_list()))
        new_node.next = node2
    return new_ll


class NestedLinkedList(LinkedList):
    def flatten(self):
        '''
        Args: nested linked list
        Returns: linked list in ascending sorted order.
        '''

        if self.head is None:
            return

        current = self.head
        merged_ll = current.value
        while current.next:
            merged_ll = merge(merged_ll, current.next.value)
            current = current.next

        return merged_ll

    # Recursive implementation of flatten function
    def flatten_recursive(self):
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    def _flatten_recursive(self, node):
        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))  # <-- Both arguments are a simple LinkedList each

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)
''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
#print(merge(linked_list, second_linked_list).to_list())
''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here
#print(nested_linked_list.flatten().to_list())



def even_after_odd(head):
    """
    desc - put even nodes after odd nods without creating new nodes or using any data structures
    param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    """
    parameter: - head of the given linked list
    return: - head of the updated list with all even elements placed after odd elements
    """
    # --------------------------------------------------#
    '''
    The Idea: Traverse the given LinkedList, and build two sub-lists: EVEN and ODD. 
    For this purpose, we will use four helper references, that denotes starting and 
    current ending of EVEN and ODD sub-list respectively. 

    1. For each Node in the LinkedList, check if its data is even/odd. 
    Change the "next" reference (pointer) of each Node, based on the following rules:
     - First even valued Node will be referenced by head of EVEN sub-list
     - Subsequent even valued Node will be appended to the tail of EVEN sub-list

     - First odd valued Node will be referenced by head of ODD sub-list
     - Subsequent odd valued Node will be appended to the tail of ODD sub-list

    2. After the loop, append the EVEN sub-list to the tail of ODD sub-list.
    '''

    if head is None:
        return head

    # Helper references
    ''' `even_head` and `even_tail` represents the starting and current ending of the "EVEN" sub-list '''
    even_head = None
    even_tail = None

    ''' `odd_head` and `odd_tail` represents the starting and current ending of the "ODD" sub-list '''
    odd_head = None
    odd_tail = None

    current = head  # <-- "current" represents the current Node.

    # Loop untill there are Nodes available in the LinkedList
    while current:  # <-- "current" will be updated at the end of each iteration

        next_node = current.next  # <-- "next_node" represents the next Node w.r.t. the current Node

        if current.data % 2 == 0:  # <-- current Node is even

            # Below
            if even_head is None:  # <-- Make the current Node as the starting Node of EVEN sub-list
                even_head = current  # `even_head` will now point where `current` is already pointing
                even_tail = even_head
            else:  # <-- Append the current even node to the tail of EVEN sub-list
                even_tail.next = current
                even_tail = even_tail.next
        else:
            if odd_head is None:  # <-- Make the current Node as the starting Node of ODD sub-list
                odd_head = current
                odd_tail = odd_head
            else:  # <-- Append the current odd node to the tail of ODD sub-list
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node  # <-- Update "head" Node, for next iteration

    if odd_head is None:  # <-- Special case, when there are no odd Nodes
        return even_head

    odd_tail.next = even_head  # <-- Append the EVEN sub-list to the tail of ODD sub-list

    return odd_head


def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """'''
    The Idea: 
    Traverse the Linkedist. Make use of two references - `current` and `previous`.
     - Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
     - Delete next `j` nodes. Keep incrementing the `current`.
     - Connect the `previous.next` to the `current`
    '''

    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None

    # Edge case - Delete 0 nodes
    if j == 0:
        return head

    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    current = head
    previous = None

    # Traverse - Loop untill there are Nodes available in the LinkedList
    while current:

        '''skip (i - 1) nodes'''
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        '''delete next j nodes'''
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node

        '''Connect the `previous.next` to the `current`'''
        previous.next = current

    # Loop ends

    return head


def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: `position_one` - indicates position (index) ONE
    :param: `position_two` - indicates position (index) TWO
    return: head of updated linked list with nodes swapped

    TODO: complete this function and swap nodes present at position_one and position_two
    Do not create a new linked list
    """

    # If both the indices are same
    if position_one == position_two:
        return head

    # Helper references
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head
    new_head = None

    # LOOP - find out previous and current node at both the positions (indices)
    while current_node is not None:

        # Position_one cannot be equal to position_two,
        # so either one of them might be equal to the current_index
        if current_index == position_one:
            one_current = current_node

        elif current_index == position_two:
            two_current = current_node
            break

        # update previous as you go
        if one_current is None:
            one_previous = current_node

        two_previous = current_node

        # increment both the current_index and current_node
        current_node = current_node.next
        current_index += 1

    # Loop ends
    '''SWAPPING LOGIC'''
    # We have identified the two nodes: one_current & two_current to be swapped,
    # Make use of a temporary reference to swap the references
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp

    # if the node at first index is head of the original linked list
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head
    # Swapping logic ends

    return new_head

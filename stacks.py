

# =========Stack via Array=========

# using array has a time complexity of O(n) because we have to traverse to increase capacity
class StackArray:
    def __init__(self, initial_arr=10):
        self.arr = [0 for _ in range(initial_arr)]
        self.next_idx = 0
        self.num_elements = 0

    def push(self, data):
        if len(self.arr) == self.num_elements:
            print('Out of space! Increasing array capacity...')
            self._handle_stack_capacity_full()
        self.arr[self.next_idx] = data
        self.next_idx += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            self.next_idx = 0
            return None
        self.next_idx -= 1
        self.num_elements -= 1
        return self.arr[self.next_idx]

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr)*2)]

        for idx, val in enumerate(old_arr):
            self.arr[idx] = val

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


# =========Stack via Linked List===============

# using Linked List as a stack has O(1) capacity because we're not traversing; just push & pop from the front
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLL:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.head is None:
            return None
        temp_val = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp_val

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def to_list(self):
        if self.head == None:
            return None
        out = []
        current = self.head
        while current:
            out.append(current.value)
            current = current.next
        return out


# ========Stack via List=======

class StackList:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.size == 0:
            return None
        self.list.pop()

    def size(self):
        return len(self.list)


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """

    # TODO: Initiate stack object
    # TODO: Iterate through equation checking parentheses
    # TODO: Return True if balanced and False if not

    stack = StackList()
    bracks_dict = {'[': ']', '{':'}', '(':')'}

    for i in equation:
        if i in bracks_dict.keys():
            stack.push(i)
            continue
        if i in bracks_dict.values():
            if stack.size() == 0:
                return False
            b_key = stack.list.pop()
            if i != bracks_dict[b_key]:
                return False
    return stack.size() == 0

# print (equation_checker('((3^2 + 8)*(5/2))/(2+6)'))
# print (equation_checker('((3^2 + 8)*(5/2))/(2+6))'))


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer
    Note: Postfix notation is a notation for writing arithmetic expressions
        in which the operands appear before their operators.

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    # TODO: Iterate over elements
    # TODO: Use stacks to control the element positions
    # test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]

    stack = StackLL()
    for i in input_list:
        print('stack is: {} and operator is: {}'.format(stack.to_list(), i))
        if i == '+':
            b = stack.pop()
            a = stack.pop()
            stack.push(a + b)
        elif i == '-':
            b = stack.pop()
            a = stack.pop()
            stack.push(a - b)
        elif i == '/':
            b = stack.pop()
            a = stack.pop()
            stack.push(int(a / b))
        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            stack.push(a * b)
        else:
            stack.push(int(i))
    return stack.pop()


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stacks): Input stack to be reversed
    Returns:
       stacks: Reversed Stack
    """

    # TODO: Write the reverse stack function
    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack, holder_stack)


# used in the function above?
def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.is_empty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack, holder_stack)
    stack.push(popped_element)


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """

    # count { and count }
    # find the smaller count & subtract it from the other
    # if sum == 0 return -1

    # note: the solution given was using a stack

    opens = 0
    closes = 0
    for i in input_string:
        if i == '{':
            opens += 1
        if i == '}':
            closes += 1
    if opens > closes:
        return opens - closes
    elif closes > opens:
        return closes - opens
    else:
        return -1

Problem 1: LRU Cache
---------------------
Time Complexity: O(1)
Maps take constant time but are not ordered, which is needed to check recently used elements. 
A queue can be used to keep track of when elements are used, but only the head and tail are O(1) time.
Accessing a middle element from a queue will be O(n) time.
Solution is to store queue position data (previous & next nodes) in a map so that data can be 
accessed in constant time and then the previous & next info can be used to update the queue
in constant time.

Space Complexity: O(n)
Solution uses dictionaries, arrays, and class objects which are linear complexity.


Problem 2: File Recursion
-------------------------
Time Complexity: O(n)

We're iterating through all of the contents in in the input using recursion. So the complexity is linear.

Space Complexity: O(n)

The function is called recursively n times and is popped of the stack before continuing.


Problem 3: Huffman Coding 
-------------------------
Time Complexity: O(n)

The loops and recursion makes this the complexity linear.

Space Complexity: O(n)

Solution uses dictionaries, arrays, and class objects which are linear complexity.


Problem 4: Active Directory 
---------------------------
Time Complexity: O(n)

We're iterating through all of the contents in in the input using recursion. So the complexity is linear.

Space Complexity: O(n)

The function is called recursively n times and is popped of the stack before continuing.


Problem 5: Blockchain 
---------------------
Time Complexity: O(1)

Adding to the blockchain accesses the tail only which is constant time. The conversion function is only
there to facilitate testing but would otherwise decrease the efficiency to O(n).

Space Complexity: O(n)
Class objects have a complexity of O(n)


Problem 6: Union & Intersection 
-------------------------------
Time Complexity: O(n)

Union requires iterating both lists adding them to a 3rd list to remove duplicates, rather than 
just pointing head to tail. Intersection requires using a map to check one list while iterating
the other to avoid a nested loop. Maps are O(1) to index but looping the list makes it linear.

Space Complexity: O(n)
Dictionary and classes are used which are O(n) complexity.
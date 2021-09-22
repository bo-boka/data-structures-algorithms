Problem_1
==========
Time complexity: O(log n)
To meet the requirement of O(log n) time, I needed to use an algorithm that would cut the input in half with each step. 
I chose a binary search that cuts the input in half and compares the middle element to determine if the target value is
in the right or left portion and dicards the side that's out of range.

Space complexity: O(log n)
If I were implementing the binary search using an iterative solution, the space complexity would be O(1). But since I'm 
using recursion, I'm increasing the call stack space with each recursive call. The total number of recursive calls made 
is proportional to the input being cut in half with each step. This is O(log n).

Problem_2
==========
Time complexity: O(log n)
To meet the requirement of O(log n) time, I needed to use an algorithm that would cut the input in half with each step. 
I chose a binary search that cuts the input in half and compares the the target value with the sorted half of the array.

Space complexity: O(log n)
If I were implementing the binary search using an iterative solution, the space complexity would be O(1). But since I'm 
using recursion, I'm increasing the call stack space with each recursive call. The total number of recursive calls made 
is proportional to the input being cut in half with each step. This is O(log n).

Problem_3
==========
Time complexity: O(n log n)
I chose to sort the array from max to min using heap sort with a time complexity of O(n log n) and then put the values 
into two strings by alternating for the next largest elements. I was told I could do this without sorting but I have no 
idea how.  

Space complexity: O(n)
I chose the heapsort with O(1) auxiliary space rather than mergesort with O(n) auxiliary space. However, heapsort is 
not stable because it may invert duplicates, whereas mergesort will preserve the relative order. Since there were no 
duplicates in the test case examples, I went with heapsort. Then factoring in that heapify is called for all of the
input, space complexity is O(n). 

Problem_4
==========
Time complexity: O(n)
I used multiple indexes and swapping to keep the array partitioned without doing multiple iterations. Since we are
looping the size of the input in the worst case scenario, the rate of increase is proportional to the input, n.

Space complexity: O(1)
We're swapping values in place.

Problem_5
==========
Time complexity: O(n)
I used recursion to build the suffix list and pass it back when a leaf node is hit. There are also loops that iterate 
the size of the input, n. 

Space complexity: O(n)
The suffix function is called recursively on each child node, which is the size of the input. This means a call is added
to the stack proportional to the input size, n.

Problem_6
==========
Time complexity: O(n)
I used variables to keep track of the max and min while iterating once through the input. 

Space complexity: O(1)
We are not increasing memory proportional to the input size. It is constant.

Problem_7
==========
Time complexity: O(n)
I used the router class to organize calls to the RouteTrie and initialized the nodes using the defaultdict class because
it automatically adds key/value pairs when called rather than returning a key not found error. Loops, regex, and 
recursion are all proportional to the input size, n.

Space complexity: O(n)
Insert function is called recursively for each child node, which means calls are added to the stack proportional to the 
input size.


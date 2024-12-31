# Strings/Characters
# ord(char) returns the ASCII value of the character
count = [0]*26
s = "Apple"
for c in s:
    count[ord(c) - ord('a')] += 1

# Slicing
print(s[0:2]) # Ap

# Strings are immutable

# Sets
seen = set()
# add(element) adds an element to the set
# remove(element) removes an element from the set
# value in set returns True if the value is in the set, False otherwise
# len(set) returns the number of elements in the set
print(set[1, 2, 3]) # {1, 2, 3} Convert list to set

# Set comprehension
mySet = {i for i in range(5)} # mySet = {0, 1, 2, 3, 4}

# Dicts/HashMap
# d = defaultdict(list) creates a dict where the default value is an empty list
# d = defaultdict(int) creates a dict where the default value is 0
# d = defaultdict(str) creates a dict where the default value is an empty string
# d = {} and d = dict() are equivalent
# len(d) returns the number of key-value pairs in the dict
d = {"one": 1, "two": 2, "three": 3, "four": 4}

# Get all keys in dict
for x in d:
    print(x)

# Another way to get keys in dict
for k in d.keys():
    print(x)

# Get all values in dict
for v in d.values():
    print(v)

# Get all key-value pairs in dict
for k, v in d.items():
    print(k, v)
# d[key] returns the value associated with the key
# d[key] = value sets the value associated with the key
# key in d returns True if the key is in the dict, False otherwise
# del d[key] removes the key from the dict
# d.keys() returns a list of all keys in the dict
# d.values() returns a list of all values in the dict
# d.items() returns a list of tuples of all key-value pairs in the dict
# d.clear() removes all key-value pairs
# d.pop(key) removes the key-value pair and returns the value

# Dict comprehension
myMap = {i: 2*i for i in range(5)} # myMap = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Tuple is an immutable list and hashable unlike list
count = [0] * 26
for c in s:
    key = ord(c) - ord('a')
    count[key] += 1
d[tuple(count)].append(s) # Convert list to tuple to use as key
# Tuple will look something like this: (1, 0, 0, 0, 1...........goes to 26)


# List comprehension
# 1D List
arr = [i for i in range(5)] # arr = [0, 1, 2, 3, 4]
arr = [i+i for i in range(5)] # arr = [0, 2, 4, 6, 8]

# 2D List
arr_2d = [[0] * 4 for i in range(4)] # arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Queue (Queues in python are Double ended queue by default)
from collections import deque
queue = deque()
queue.append(1) # Add element to the end(right side) of the queue
queue.appendleft(2) # Add element to the beginning (left side) of the queue
queue.pop() # Remove element from the end(right side) of the queue
queue.popleft() # Remove element from the beginning (left side) of the queue

# Heap - under the hood, it is implemented as array/list in python
# By default, Heaps in python are min heaps
import heapq
minHeap = []
heapq.heappush(minHeap, 1) # Add element to the heap
heapq.heappush(minHeap, 2)

print(minHeap[0]) # Min is always at index 0

while len(minHeap):
    print(heapq.heappop(minHeap)) # Prints smallest to largest

# To create a max heap, multiply the element by -1 and then push it to the heap
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap)) # Prints largest to smallest


# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr) # Use heapify to convert a list to heap
while arr:
    print(heapq.heappop(arr)) # Prints smallest to largest

# Sorting in python
# Sorting is ascending by default in python
arr = [2, 1, 8, 4, 5]
arr.sort() # Sorts in place
print(arr) # [1, 2, 4, 5, 8]

arr.sort(reverse=True) # Sorts in descending order

# Sorting strings
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr) # ['alice', 'bob', 'doe', 'jane']

# Custom sorting
arr.sort(key=lambda x: len(x)) # Sorts based on length of the string
print(arr) # ['bob', 'doe', 'jane', 'alice']

# Stacks and Lists
# Stacks in python are implemented using lists/arrays

arr = [1, 2, 3]
arr.append(4) # Push element to the stack
arr.append(5)
print(arr)  # [1, 2, 3, 4, 5]
arr.pop() # Pop element from the stack
print(arr) # [1, 2, 3, 4] - 5 is removed

arr[-1] # Peek the top of the stack

arr.insert(1, 7) # since technically it is a list, you can insert at any index
print(arr) # [1, 7, 2, 3, 4]

# Sublist
arr = [1, 2, 3, 4, 5]
print(arr[1:3]) # [2, 3]

# Unpacking
a, b, c, = [1, 2, 3]
print(a, b, c) # 1 2 3

# Looping through list
# Using index
for i in range(len(arr)):
    print(arr[i])

# Using value
for x in arr:
    print(x)

# Using enumerate
for i, x in enumerate(arr):
    print(i, x)

# Loop through multiple arrays simultaneously
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2) # 1 2, 3 4, 5 6

# Reverse a list
arr = [1, 2, 3, 4, 5]
arr.reverse() # [5, 4, 3, 2, 1]

# Time complexity Information
# Stack: O(1) for append, pop() and peek(stack[-1]), O(n) for insert
# Queue: Always use collections.deque instead of queue.Queue O(1) for append, appendleft(), popleft() and pop(), O(n) for insert, queue[i] is O(n)
# Heap: O(log n) for push and pop, O(n) for heapify aka building heap
# List: sort() - O(n log n) # Uses timsort, reverse() - O(n), append() - O(1), pop() - O(1), insert() - O(n), del - O(n)

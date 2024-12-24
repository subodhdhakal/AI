# Strings/Characters
# ord(char) returns the ASCII value of the character
count = [0]*26
s = "Apple"
for c in s:
    count[ord(c) - ord('a')] += 1

# Sets
seen = set()
# add(element) adds an element to the set
# remove(element) removes an element from the set
# value in set returns True if the value is in the set, False otherwise

# Dicts/Hashmaps
# d = defaultdict(list) creates a dict where the default value is an empty list
# d = defaultdict(int) creates a dict where the default value is 0
# d = defaultdict(str) creates a dict where the default value is an empty string
# d = {} and d = dict() are equivalent
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

# Tuple is an immutable list and hashable unlike list
count = [0] * 26
for c in s:
    key = ord(c) - ord('a')
    count[key] += 1
d[tuple(count)].append(s) # Convert list to tuple to use as key
# Tuple will look something like this: (1, 0, 0, 0, 1...........goes to 26)


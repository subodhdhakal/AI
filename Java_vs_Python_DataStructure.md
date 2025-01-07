# Java vs Python Data Structure Methods

### String

| **Operation**                               | **Java**                                      | **Python**                  |
| ------------------------------------------- | --------------------------------------------- | --------------------------- |
| **Get ASCII value of a character**          | `c - 'a'`                                     | `ord(c) - ord('a')`         |
| **Check if character is a letter or digit** | `Character.isLetterOrDigit(c)`                | `c.isalnum()`               |
| **Convert to lowercase**                    | `Character.toLowerCase(c)`                    | `c.lower()`                 |
| **Convert to uppercase**                    | `Character.toUpperCase(c)`                    | `c.upper()`                 |
| **Check if string starts with a prefix**    | `str.startsWith(prefix)`                      | `str.startswith(prefix)`    |
| **Check if string ends with a suffix**      | `str.endsWith(suffix)`                        | `str.endswith(suffix)`      |
| **Find character at an index**              | `str.charAt(index)`                           | `str[index]`                |
| **Concatenate strings**                     | `str1 + str2` or `str1.concat(str2)`          | `str1 + str2`               |
| **Substring**                               | `str.substring(start, end)`                   | `str[start:end]`            |
| **Check if string contains a substring**    | `str.contains(substring)`                     | `substring in str`          |
| **Trim whitespace from both ends**          | `str.trim()`                                  | `str.strip()`               |
| **Split string by delimiter**               | `str.split(delimiter)`                        | `str.split(delimiter)`      |
| **Replace substring**                       | `str.replace(old, new)`                       | `str.replace(old, new)`     |
| **Convert string to integer**               | `Integer.parseInt(str)`                       | `int(str)`                  |
| **Convert integer to string**               | `Integer.toString(num)`                       | `str(num)`                  |
| **Check string length**                     | `str.length()`                                | `len(str)`                  |
| **Check equality of two strings**           | `str1.equals(str2)`                           | `str1 == str2`              |
| **Find index of a character or substring**  | `str.indexOf(charOrSubstring)`                | `str.find(charOrSubstring)` |
| **Reverse a string**                        | `new StringBuilder(str).reverse().toString()` | `str[::-1]`                 |

### List/Array

| **Operation**                                      | **Java**                                           | **Python**               |
| -------------------------------------------------- | -------------------------------------------------- | ------------------------ |
| **Create a list/array**                            | `new ArrayList<>()` or `new int[]{1, 2, 3}`        | `[1, 2, 3]`              |
| **Get element at index**                          | `list.get(index)` or `array[index]`               | `list[index]`            |
| **Set element at index**                          | `list.set(index, value)` or `array[index] = value` | `list[index] = value`    |
| **Add element to end**                            | `list.add(value)`                                  | `list.append(value)`     |
| **Insert element at index**                       | `list.add(index, value)`                           | `list.insert(index, value)` |
| **Remove element by value**                       | `list.remove(value)`                               | `list.remove(value)`     |
| **Remove element by index**                       | `list.remove(index)`                               | `list.pop(index)`        |
| **Check if element exists**                       | `list.contains(value)`                             | `value in list`          |
| **Get size/length of list**                       | `list.size()`                                      | `len(list)`              |
| **Sort list**                                     | `Collections.sort(list)` or `Arrays.sort(array, Comparator)`   | `list.sort()` or `sorted(list, key=lambda x: ...)` |
| **Reverse list**                                  | `Collections.reverse(list)`                        | `list.reverse()`         |
| **Iterate over list**                             | `for (int item : list)` or `for (int i = 0...)`    | `for item in list`       |
| **Convert list to array**                         | `list.toArray(new Type[0])`                        | `list` (no conversion needed) |
| **Find index of element**                         | `list.indexOf(value)`                              | `list.index(value)`      |
| **Clear all elements**                            | `list.clear()`                                     | `list.clear()`           |

### Map

| **Operation**                                  | **Java**                                             | **Python**                 |
| ---------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| **Create a map**                               | `new HashMap<>()`                                    | `{}`                       |
| **Insert key-value pair**                      | `map.put(key, value)`                                | `dict[key] = value`        |
| **Get value by key**                           | `map.get(key)`                                       | `dict.get(key)`            |
| **Remove key-value pair by key**               | `map.remove(key)`                                    | `dict.pop(key)`            |
| **Check if key exists**                        | `map.containsKey(key)`                               | `key in dict`              |
| **Check if value exists**                      | `map.containsValue(value)`                           | `value in dict.values()`   |
| **Get all keys**                               | `map.keySet()`                                       | `dict.keys()`              |
| **Get all values**                             | `map.values()`                                       | `dict.values()`            |
| **Iterate over key-value pairs**               | `for (Map.Entry<Key, Value> entry : map.entrySet())` | `for key, value in dict.items()` |
| **Get size of map**                            | `map.size()`                                         | `len(dict)`                |
| **Clear all entries**                          | `map.clear()`                                        | `dict.clear()`             |

### Set

| **Operation**                                  | **Java**                                             | **Python**                 |
| ---------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| **Create a set**                               | `new HashSet<>()`                                    | `set()`                    |
| **Add element**                                | `set.add(value)`                                     | `set.add(value)`           |
| **Remove element**                             | `set.remove(value)`                                  | `set.remove(value)`        |
| **Check if element exists**                    | `set.contains(value)`                                | `value in set`             |
| **Get size of set**                            | `set.size()`                                         | `len(set)`                 |
| **Iterate over elements**                      | `for (Value value : set)`                            | `for value in set`         |
| **Union of two sets**                          | `set1.addAll(set2)`                                  | `set1.union(set2)`         |
| **Intersection of two sets**                   | `set1.retainAll(set2)`                               | `set1 & set2`              |
| **Difference of two sets**                     | `set1.removeAll(set2)`                               | `set1 - set2`              |
| **Clear all elements**                         | `set.clear()`                                        | `set.clear()`              |

### Stack

| **Operation**                                  | **Java**                                             | **Python**                 |
| ---------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| **Create a stack**                             | `new Stack<>()`                                      | `[]` or `collections.deque()` |
| **Push element onto stack**                    | `stack.push(value)`                                  | `stack.append(value)`      |
| **Pop element from stack**                     | `stack.pop()`                                        | `stack.pop()`              |
| **Peek top element**                           | `stack.peek()`                                       | `stack[-1]`                |
| **Check if stack is empty**                    | `stack.isEmpty()`                                    | `len(stack) == 0`          |

### Queue

| **Operation**                                  | **Java**                                             | **Python**                 |
| ---------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| **Create a queue**                             | `new LinkedList<>()` or `new ArrayDeque<>()`         | `collections.deque()`      |
| **Enqueue element**                            | `queue.add(value)` or `queue.offer(value)`           | `queue.append(value)`      |
| **Dequeue element**                            | `queue.poll()` or `queue.remove()`                   | `queue.popleft()`          |
| **Peek front element**                         | `queue.peek()`                                       | `queue[0]`                 |
| **Check if queue is empty**                    | `queue.isEmpty()`                                    | `len(queue) == 0`          |

### Heap

| **Operation**                                  | **Java**                                             | **Python**                 |
| ---------------------------------------------- | ---------------------------------------------------- | -------------------------- |
| **Create a heap**                              | `new PriorityQueue<>()`                              | `heapq` library (`[]`)     |
| **Add element to heap**                        | `heap.add(value)`                                    | `heapq.heappush            |

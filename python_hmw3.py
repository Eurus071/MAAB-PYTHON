# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 19:45:00 2026

@author: user
"""

### List Tasks

#1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
lst = [1, 2, 3, 2, 2]
x = 2
print(lst.count(x))

#2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
print(sum(lst))

#3. **Max Element**: From a given list, determine the largest element.
print(max(lst))

#4. **Min Element**: From a given list, determine the smallest element.
print(min(lst))

#5. **Check Element**: Given a list and an element, check if the element is present in the list.
x = 2
print(x in lst)
#6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
print(lst[0] if lst else None)

#7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
print(lst[-1] if lst else None)

#8. **Slice List**: Create a new list that contains only the first three elements of the original list.
print(lst[:3])
#9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
print(lst[::-1])

#10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
print(sorted(lst))

#11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
print(list(set(lst)))

#12. **Insert Element**: Given a list and an element, insert the element at a specified index.
lst.insert(1, 2)
print(lst)

#13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
x = 2
print(lst.index(x) if x in lst else -1)

#14. **Check for Empty List**: Determine if a list is empty and return a boolean.
lst1 = []
print(len(lst1) == 0)
#15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
print(sum(1 for x in lst if x % 2 == 0))

#16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
print(sum(1 for x in lst if x % 2 != 0))

#17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
a = [1, 2]
b = [3, 4]
print(a + b)
#18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
sub = [2, 3]
found = any(lst[i:i+len(sub)] == sub for i in range(len(lst)))
print(found)

#19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
old, new = 2, 9
if old in lst:
    lst[lst.index(old)] = new
print(lst)

#20. **Find Second Largest**: From a given list, find the second largest element.
unique = sorted(set(lst))
print(unique[-2])
#21. **Find Second Smallest**: From a given list, find the second smallest element.
unique = sorted(set(lst))
print(unique[1])

#22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
print([x for x in lst if x % 2 == 0])

#23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
print([x for x in lst if x % 2 != 0])

#24. **List Length**: Determine the number of elements in the list.
print(len(lst))

#25. **Create a Copy**: Create a new list that is a copy of the original list.
copy_lst = lst.copy()
print(copy_lst)
#26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
mid = len(lst) // 2
print(lst[mid-1:mid+1] if len(lst) % 2 == 0 else lst[mid])

#27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
print(max(lst[1:4]))

#28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
print(min(lst[1:4]))

#29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
idx = 1
if 0 <= idx < len(lst):
    lst.pop(idx)
print(lst)

#30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
print(lst == sorted(lst))
#31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
n = 3
print([x for x in lst for _ in range(n)])

#32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
a = [3, 1]
b = [4, 2]
print(sorted(a + b))
#33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
x = 2
print([i for i, v in enumerate(lst) if v == x])

#34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
k = 1
print(lst[-k:] + lst[:-k])

#35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
print(list(range(1, 11)))

#36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
print(sum(x for x in lst if x > 0))

#37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
print(sum(x for x in lst if x < 0))

#38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
print(lst == lst[::-1])

#39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
n = 2
print([lst[i:i+n] for i in range(0, len(lst), n)])

#40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print(unique)

### Tuple Tasks

#1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
t = (1, 2, 3, 2, 2)
x = 2
print(t.count(x))

#2. **Max Element**: From a given tuple, determine the largest element.
print(max(t))

#3. **Min Element**: From a given tuple, determine the smallest element.
print(min(t))

#4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
x = 2
print(x in t)

#5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
print(t[0] if t else None)

#6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
print(t[-1] if t else None)

#7. **Tuple Length**: Determine the number of elements in the tuple.
print(len(t))

#8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
print(t[:3])

#9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
a = (1, 2)
b = (3, 4)
print(a + b)
#10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
t = ()
print(len(t) == 0)
#11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.
x=2
print([i for i, v in enumerate(t) if v == x])

#12. **Find Second Largest**: From a given tuple, find the second largest element.
unique = sorted(set(t))
print(unique[-2])

#13. **Find Second Smallest**: From a given tuple, find the second smallest element.
unique = sorted(set(t))
print(unique[1])

#14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
t = (x,)
print(t)

#15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
print(tuple(lst))
#16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
print(t == tuple(sorted(t)))

#17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
print(max(t[1:4]))

#18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
print(min(t[1:4]))

#19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
x = 2

lst = list(t)
if x in lst:
    lst.remove(x)

print(tuple(lst))
#20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
t = (1, 2, 3, 4, 5, 6)
n = 2
print(tuple(t[i:i+n] for i in range(0, len(t), n)))

#21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
n = 3
print(tuple(x for x in t for _ in range(n)))

#22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
print(tuple(range(1, 11)))

#23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
print(t[::-1])
#24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
print(t == t[::-1])

#25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
unique = []

for x in t:
    if x not in unique:
        unique.append(x)

print(tuple(unique))

### Set Tasks

#1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
#2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
print(a & b)
#3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
print(a - b)
#4. **Check Subset**: Given two sets, check if one set is a subset of the other.
print(a.issubset(b))
#5. **Check Element**: Given a set and an element, check if the element exists in the set.
s = {1, 2, 3}
x = 2
print(x in s)

#6. **Set Length**: Determine the number of unique elements in a set.
print(len(s))
#7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
lst = [1, 2, 2, 3]
print(set(lst))
#8. **Remove Element**: Given a set and an element, remove the element if it exists.
x = 2
s.discard(x)
print(s)
#9. **Clear Set**: Create a new empty set from an existing set.
new_set = set()
print(new_set)
#10. **Check if Set is Empty**: Determine if a set has any elements.
s = set()
print(len(s) == 0)
#11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)
#12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
s = {1, 2}
x = 3
s.add(x)
print(s)
#13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
print(s.pop())
#14. **Find Maximum**: From a given set of numbers, find the maximum element.
print(max(s))
#15. **Find Minimum**: From a given set of numbers, find the minimum element.
print(min(s))
#16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
print({x for x in s if x % 2 == 0})
#17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
print({x for x in s if x % 2 != 0})
#18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
print(set(range(1, 11)))
#19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
print(set(a + b))
#20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
print(a.isdisjoint(b))

#21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
print(list(set(lst)))
#22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
print(len(set(lst)))
#23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.

import random

random_set = set(random.randint(1, 20) for _ in range(5))
print(random_set)

### Dictionary Tasks

#1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
d = {"a": 1, "b": 2}
key = "c"
print(d.get(key, None))

#2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
key = "a"
print(key in d)
#3. **Count Keys**: Determine the number of keys in the dictionary.
print(len(d))
#4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
print(list(d.keys()))
#5. **Get All Values**: Create a list that contains all the values in the dictionary.
print(list(d.values()))
#6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2
print(merged)
#7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
key = "c"
d.pop(key, None)
print(d)
#8. **Clear Dictionary**: Create a new empty dictionary.
d = {}
print(d)
#9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
d = {}
print(len(d) == 0)
#10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
key = "a"
print((key, d[key]) if key in d else None)
#11. **Update Value**: Given a dictionary, update the value for a specified key.
d["a"] = 5
print(d)
#12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
value = 1
print(list(d.values()).count(value))
#13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
inverted = {v: k for k, v in d.items()}
print(inverted)
#14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
value = 1
print([k for k, v in d.items() if v == value])
#15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
keys = ["a", "b"]
values = [1, 2]
print(dict(zip(keys, values)))
#16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
d = {"a": 1, "b": {"x": 2}}
print(any(isinstance(v, dict) for v in d.values()))
#17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
d = {"a": {"x": 10}}
print(d["a"]["x"])
#18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
from collections import defaultdict

d = defaultdict(int)
print(d["missing"])
#19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
d = {"a": 1, "b": 2, "c": 1}
print(len(set(d.values())))
#20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
print(dict(sorted(d.items())))
#21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
print(dict(sorted(d.items(), key=lambda x: x[1])))
#22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
print({k: v for k, v in d.items() if v > 1})
#23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(bool(set(d1) & set(d2)))
#24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
t = (("a", 1), ("b", 2))
print(dict(t))
#25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
print(next(iter(d.items())))

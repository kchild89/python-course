# my_set = {1, 2, 3, 4, 4}  # duplicates values will be exterminated

# use methods
# my_set.add(5)
# my_set.remove(2)
# print(len(my_set))
# print(my_set)

# indexing and slicing does NOT work
# print(my_set[0])
# print(my_set.pop())

# exercise
# use type conversion to get one item from the set by index
# print(list(my_set)[0])

# comparison operators
set1 = {1, 2, 3, 4, 4}
set2 = {4, 5, 6, 7}

print(set1.union(set2))  # does the same as below
print(set1 | set2)

print(set1.intersection(set2))  # does the same as below
print(set1 & set2)

print(set1.difference(set2))  # does the same as below
print(set1 - set2)

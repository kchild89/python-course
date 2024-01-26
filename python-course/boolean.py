# boleans and numbers
print(1 == 1)  # is equal
print(1 != 10)  # is not equal
print(10 > 10)

# booleans and lists and strings
print(1 in [1, 2, 3])
print("e" in "hello")
print(4 not in [1, 2, 3])

# date conversion exercise
e_dict = {1: "one", 2: "two", 3: "three"}
# check if the key 1 exists in the dict
print(1 in e_dict)

# check if the value 'four' exists in the dict
print("four" not in e_dict.values())

# booleans by themselves
print(True)
print(not True)

# bool function
# if it has content its truthy
# if it doesnt have content its falsy
print(bool(34123))  # truthy
print(bool())  # falsy
print(bool("string"))  # truthy
print(bool(""))  # falsy
print(bool([1, 2, 3]))  # truthy
print(bool([]))  # falsy
print(bool(None))  # falsy

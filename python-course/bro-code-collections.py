# Collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
#


fruits = ["apple", "orange", "banana", "coconut"]  # list
fruits = {"apple", "orange", "banana", "coconut"}  # set
fruits = ("apple", "orange", "banana", "coconut")  # tuple

# Some Function

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)  # returns True
print("pineapple" in fruits)  # returns False

# Some Methods

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))


for fruit in fruits:
    print(fruit)

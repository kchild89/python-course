# basics x = {key : value}
test_dict = {"A": 123, "B": [1, 2, 3], 1: True}
print(test_dict.values())
print(type(test_dict.values()))
print(test_dict.keys())
print(test_dict.items())
print(len(test_dict))

# converting a dict
print(list(test_dict))

# indexing with dict.
print(test_dict["A"])  # does crash when it doesnt find a key
print(test_dict.get("X"))  # doesn't crash when it cannot find a key

# Exercise
# do research and use the update method to add another key value pair

dict_1 = {"A": 23, "B": 34, "C": 45, "E": 65}
dict_2 = {"B": 23, "D": 34, "C": 55}
dict_1.update(dict_2)
print(dict_1)


car = {"brand": "Ford", "model": "Mustang", "year": "1964"}
car.update({"color": "White"})
car.update({"color": "Black"})
print(car)
print(car["brand"])
print(car["color"])

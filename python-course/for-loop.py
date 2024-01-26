basic_list1 = [1, 2, 3]
basic_tuple1 = (1, 2, 3)
basic_dict1 = {1: "one", 2: "two", 3: "three"}
basic_set1 = {1, 2, 3}
basic_string1 = "One two three"
basic_num1 = 3

for y in range(10, 20, 2):
    print(y)

# test to see how each print
basic_list = [1, 2, 3]
basic_tuple = (1, 2, 3)
basic_dict = {1: "one", 2: "two", 3: "three"}
basic_set = {1, 2, 3}
basic_string = "One two three"
basic_num = 3

for x in basic_dict.items():
    print(x)

# exercise
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100
practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]
for nested_list in practice_list:
    for value in nested_list:
        if value > 100:
            break
        if value < 50:
            if value < 10:
                continue
            print(value)
# should print
# 10
# 40
# 20
# 42
# 10

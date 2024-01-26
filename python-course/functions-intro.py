# Define
# Exercise 1
def test_function():
    print("Hello")
    test = 1 + 2
    print(test)


test_function()


# Exercise 2
def calculator(num1, num2):
    result = num1 + num2
    print(result)


calculator(2, 3)
calculator(20, 30)


# Exercise 3
def better_calculator(num3, num4, operation):
    if operation == "plus":
        result2 = num3 + num4
        print(f"{num3} + {num4} = {result2}")
    elif operation == "minus":
        result2 = num3 - num4
        print(f"{num3} - {num4} = {result2}")
    elif operation == "multiply":
        result2 = num3 * num4
        print(f"{num3} * {num4} = {result2}")
    elif operation == "divide":
        result2 = num3 / num4
        print(f"{num3} / {num4} = {result2}")


better_calculator(10, 2, "plus")
better_calculator(10, 2, "minus")
better_calculator(10, 2, "multiply")
better_calculator(10, 2, "divide")

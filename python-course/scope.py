# global and local scopes
# every function has its own local scope and every local scope is separate
# variables inside functions only exist inside that function
# global variables can be accessed in the local scope but they cannot be changed (or created) if created thats when it becomes local to that function
# you can move between scopes with parameters, global and return but only use it when needed
# generaly you want to use return

g = 10  # global


def test_func():  #
    L = 2  # local scope
    print(L)  #


test_func()


def test_func2():
    L = 200
    print(L)


test_func2()


def test_func3(g):
    g += 2
    print(g)


test_func3(g)


# same function as above but not as good.
def test_func4():
    global g
    g += 2
    print(g)


test_func4()


# similar to func3
def test_func5(g):
    g += 2
    return g


print(test_func5(g))


# best way
def test_func6(g):
    g += 2
    return g


g = test_func6(g)
print(g)


# exercise
# create 2 global variables called 'multiplier' and has_calculated
# multiplier should have any integer and has_calculated should be set to the booleann false
# then create a function called multiply_calculator that takes one argument and     calculates the multiplication of that number
# inside of the function multiply the parameter with the global variable mutiplier
# Once the calculation is done set has_calculated to True
# store that new number a variiable called result and return it
# print the return value of the function (after it was called with the number)

multiplier = 5
has_calculated = False


def multiply_calculator(number):
    global has_calculated
    has_calculated = True
    result = number * multiplier
    return result


result = multiply_calculator(5)
print(result)
print(has_calculated)

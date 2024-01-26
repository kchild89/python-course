# using positioning arguments
def test_function(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


test_function(1, "hello", True, [1, 2, "test"])


# using keyword arguments
def test_function1(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


test_function1(arg4=1, arg2="hello", arg3=True, arg1=[1, 2, "test"])


# combining positional and keyword arguments
# positonal have to come before keyword arguments
def test_function1(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


test_function1(1, arg2="hello", arg3=True, arg4=[1, 2, "test"])


# default arguments
# exercise 1
def test_function1(arg1, arg2, arg3, arg4="Argument 4"):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


test_function1(1, arg2="hello", arg3=True)


# exercise 2
def test_function1(
    arg1="Argument 1", arg2="Argument 2", arg3="Argument 3", arg4="Argument 4"
):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


test_function1()

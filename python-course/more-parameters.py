# # list unpacking
# def print_all(first, *arguments, extra):
#     print(first)
#     print(arguments)
#     print(extra)
#     # print all arguments
#     for argument in arguments:
#         print(argument)


# # keyword unpacking
# def print_more(**arguments):
#     print(arguments)


# # combining keyword and arguments
# # args = short for argumensta
# # kwargs = short for keyword arguments
# def print_even_more(*args, **kwargs):
#     print(args)
#     print(kwargs)


# # print_all(1, 2, 3, 4, 5, "hello", 1, 3, 213, 321, 3, 123, extra=12)
# # print_more(arg="1", arg2="test", arg3=[1, 2, 3])
# print_even_more(1, 2, 3, 54, 21, 3412, 31, "hello", True, test=1, test2=5)

# # exercise
# # create a calculator function that prints the sum of an unlimited amount of numbers


def sum_number(*args):
    result = sum(args)
    # print(sum(args))
    print(result)


sum_number(1, 22, 3, 4, 54, 6, 57, 8, 49, 230, 78)

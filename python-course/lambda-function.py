# Lambda simple single line functions
# lambda parameter: expression
# some functions want other functions as argument
# sort([1,4,3,2,5],func)
# graphical user interfaces = each button gets a lambda

a = lambda x: x + 1
simple_calc = lambda a, b: a + b
print(a(10))
print(simple_calc(2, 3))

# exercise
# create a lambda function that accepts 1 integer argument
# if the integer is > 5 return hello
# otherwise return bye

x = lambda x: "hello" if x > 5 else "bye"
print(x(4))

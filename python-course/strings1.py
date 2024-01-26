# quotes for strings
test_var1 = "Test 1"
test_var2 = "Test 2"
print(test_var1)
print(test_var2)

# quotes inside of strings
test_var3 = '   He said  "This was great"    '
test_var4 = "\"'"  # simple escape character
print(test_var3)
print(test_var4)

# escape characters
test_var5 = "Line 1: some text \nLine 2: Some more text"
print(test_var5)

# multiple lines
test_var6 = """A comment
write some more text
write on another line"""
print(test_var6)
test_var7 = """    x
   xxx
  xxxxx
    x
    x"""
print(test_var7)
test_var8 = "copy" * 10
print(test_var8)

# how to get values into strings
name = "Kevin"
age = 34
greeting_string = "Hello {}, you are {} years old".format(name, age)
greeting_string = f"Hello {name}, you are {age} years old"  # most common way
print(greeting_string)

name = "Kevin"
hobby = "Hacking"
greeting_string = f"Hello, My name is {name}\nand my hobby is {hobby}"  # most common
greeting_string2 = f"""Hello, My name is {name}
and my hobby is {hobby}"""
print(greeting_string)
print(greeting_string2)

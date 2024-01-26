# quotes for strings
test_var = "Test 1"
test_var2 = "Test 2"
print(test_var)
print(test_var2)

# quotes inside of strings ' "text" ' or " 'text' "
test_var3 = '    He said "This was great"     '
# test_var4 = '\"\''  # simple escape character
print(test_var3)


# escape characters \n=line break \t \r
test_var5 = "Line 1: some text\n Line 2: some more text"
print(test_var5)

test_var8 = "copy" * 10
print(test_var8)

# how to get values into strings
name = "Bob"
age = 40
greeting_string = "Hello {one}, you are {two} years old".format(one=name, two=age)
greeting_string = f"Hello {name}, you are {age + 10} years old"
print(greeting_string)

name1 = "Kevin"
hobby = "Hacking"

greeting_string1 = f"Hello, my name is {name1}\n and my hobby is {hobby}"
print(greeting_string1)

greeting_string1 = f"""Hello, my name is {name1}
 and my hobby is {hobby}"""
print(greeting_string1)

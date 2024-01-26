# function = A block of reusable code place () after the function name to invoke it
# alot of developers mix up the parameters and arguments


# Example 1
def happy_birthday(name, age):  # In the () are parameters
    print(
        f"happy birthday to {name} happy bithday to {name} happy birthday dear {name} you are {age} years old"
    )


happy_birthday("Kevin", "34")  # In the () are arguments
happy_birthday("Sage", "4")
happy_birthday("Emery", "4")


# Example 2
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old")
    print("Happy birthday to you!")
    print()


happy_birthday("Kevin", "34")
happy_birthday("Sage", "4")
happy_birthday("Emery", "4")


# Example 3
def happy_birthday(x, y):
    print(f"Happy birthday to {x}!")
    print(f"You are {y} years old")
    print("Happy birthday to you!")
    print()


happy_birthday("Kevin", "34")
happy_birthday("Sage", "4")
happy_birthday("Emery", "4")


# Example 4
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("Kevin", 345.50, "03/21/1989")


# return = statement used to end a function and send a result back to the caller


# Example 5
def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multipy(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(add(50, 50))
print(subtract(200, 100))
print(multipy(5, 20))
print(divide(1000, 10))


# # Example 6
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("kevin", "child")

print(full_name)

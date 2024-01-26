# if
# elif
# else

x = 15
if x > 10:
    print("the if statment was true")
    print("anotherline")
    y = 10
    print(y)

elif x != 0:
    print("the elif statement was correct")

else:
    print("the code that was run if the statment was false")

print("some other code")
# there can only be one if and else in a block
# there can be infinite elif statements

# exercise
money_available = 100

if money_available >= 80:
    print("eat something fancy")
elif money_available > 45:
    print("eat something nice")
elif money_available > 15:
    print("eat something okay")
else:
    print("eat something cheap")

# practice
grade = 6

if grade == 1:
    print("Very Good")
elif grade == 2:
    print("Good")
elif grade == 3:
    print("Okay")
elif grade == 4:
    print("Bad")
elif grade == 5:
    print("Very Bad")
else:
    print("NA")

mood = "hungry"

match mood:
    case "hungry":
        print("get some food")
    case "thirst":
        print("get some water")
    case "tired":
        print("get some sleep")
    case _:
        print("any other mood")

# exercise
# create a variable with an integer between 1 and 5, call it grade
# create a match case statement that writes 'very good' when the grade is 1
# and very bad when the grade is 5 (and all other cases in between)
# there should also be some default behaviour if you get an unexpected value

grade = 2

match grade:
    case 1:
        print("Very Good")
    case 2:
        print("Good")
    case 3:
        print("Okay")
    case 4:
        print("Needs Improvement")
    case 5:
        print("Very Bad")
    case _:
        print("NA")

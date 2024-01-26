# Infinte Loops. two examples
# while True:
#   print("infinite loop")

# x = 0
# while x < 10:
#    print(x)

# while loop with a break
x = 0
while x < 10:
    print(x)
    x += 1

    if x == 5:
        break

# while loop with a continue

y = 0
while y < 10:
    y += 1

    if y == 5:
        continue  # if y == 5 continue on and dont print 5

    print(y)

# exercise
# use a while loop to create a list with only even values from 0 to 100
# Do not add the value 58!


# k = 0
# while k <= 100:
#     if k % 2 == 0:
#         print(k)
#     k += 1

my_list = []
counter = 0

while counter <= 100:
    if counter % 2 == 0 and counter != 58:
        my_list.append(counter)
    counter += 1

print(my_list)

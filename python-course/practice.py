list = [[12, 32, 56, 45], [73, 5, 32, 5], [43, 56, 111, 34]]
for lists in list:
    for value in lists:
        if value > 100:
            break
        if value < 50:
            if value < 10:
                continue
            print(value)

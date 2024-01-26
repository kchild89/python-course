practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]
for nested_list in practice_list:
    for value in nested_list:
        if value > 100:
            break  # Stop
        if value < 50:
            if value < 10:
                continue  # Skip
            print(value)


# Simplified
practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]
for nested_list in practice_list:
    for value in nested_list:
        if value > 100:
            break  # Stop
        if value < 50:
            if value >= 10:
                print(value)


# Most simplified
practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]
for nested_list in practice_list:
    for value in nested_list:
        if value > 100:
            break  # Stop
        if value >= 50:
            continue  # Skip
        if value >= 10:
            print(value)

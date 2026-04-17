my_list = [23,34,23,34,65,56,12,13,19,45]

target = 13

found_index = -1 # if not found

currentindex = 0 #Use when found

for i in my_list:

    if i == target:
        found_index = currentindex

        break
    currentindex+=1

print(f"Found at index : {currentindex}")

    
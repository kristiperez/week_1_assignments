

names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]


new_list = []

for item in names:
    if item not in new_list:
        new_list.append(item)
    
print(new_list)




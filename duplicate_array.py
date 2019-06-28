
my_array = [1,2,3,4,5]
#by definint a funtion
def my_newarray(my_array):
    return my_array + my_array

print(my_newarray(my_array))
#by using a loop

new_array = []
for item in my_array:
    if item in my_array:
        new_array.append(item)
for item in my_array:
    if item in my_array:
        new_array.append(item)
        
print(new_array)

#crazy easy way
print(my_array + my_array)

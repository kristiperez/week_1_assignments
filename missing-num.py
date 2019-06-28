
my_array = [0,1,2,3,5,6,7,8,9]



correct_total = 45

def missing_number():
    sum = 0
    for item in my_array:
        sum = sum + item
    return sum

missing = correct_total - missing_number()
print(missing)
        


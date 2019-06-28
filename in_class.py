

def calculate_factorial(number):
    result = 1
    for index in range(1,number+1):
        result *= index
    return result

try:
        number = int(input("Enter number: "))
        result = calculate_factorial(number)
        print(result)
except ValueError:
    print("please enter only numbers!:")
except:
    print("something went wrong")


result = calculate_factorical(number)
print(result)


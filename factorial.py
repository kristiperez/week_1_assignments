#get number input and print the factorial of that number

def factorial():
    number_input = int(input("Enter a number: "))
    counter = 1
    while number_input > 0:
        counter *= number_input
        number_input -= 1
    print(counter)    
       

factorial()

#could also do
#number = int(input("Enter number: "))
#factorial = 1
#for number in range(1, number+1):
#    factorial = factorial*number
#print(factorial)

#or

#for index in range(number, 0, -1):
#    result *= index
#result = result * index same as above line 23


    

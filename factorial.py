#get number input and print the factorial of that number

def factorial():
    number_input = int(input("Enter a number: "))
    counter = 1
    while number_input > 0:
        counter *= number_input
        number_input -= 1
    print(counter)    
       

factorial()





    

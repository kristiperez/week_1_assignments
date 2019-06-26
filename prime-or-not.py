#get input value
#use boolean and set initial value to true
number_input = int(input("Enter a number: "))
isPrime = True
#for each number in the range, take the number input and divide by the value in the range, if the remainder = 0 then true
for index in range(2, number_input):
    if number_input % index == 0:
        isPrime = False
        break
    
print(isPrime)



#FIZZ BUZZ

#if the number is divisible by 3 then you print "FIZZ"
#if the number is divisible by 5 then you print "BUZZ"
#if the number is divisible by 3 and 5 the you print "FIZZ BUZZ"

number = int(input("Enter number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FIZZ BUZZ")

elif number % 3 == 0:
    print("FIZZ")

elif number % 5 == 0:
    print("BUZZ")









#ask user for amount and tip percentage
amount = input("Enter the amount: ")
tip_percent = input("Enter tip percentage: ")

#divide tip amount by 100 and multiply by amount, print result
def multiply(x,y):
    result = int(x) * int(y)/100
    print (result)

multiply(amount, tip_percent)
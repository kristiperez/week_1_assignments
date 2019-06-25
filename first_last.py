
#print a greeting
def greet(first_name, last_name):
  print(f"Hello, my name is {first_name} {last_name}.")

#ask user for their first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

greet(first_name, last_name)
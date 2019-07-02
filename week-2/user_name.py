
name = input("Enter your name: ")

with open("guests.txt","w") as file_object:
    file_object.write(name)

    
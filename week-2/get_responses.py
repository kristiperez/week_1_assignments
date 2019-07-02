
reason = ""

while reason != "q":

    reason = input("Why do you like programming: ")
    
    if reason != "q":

        with open("responses.txt","a") as file_object:
            file_object.write(reason + "\n")

    

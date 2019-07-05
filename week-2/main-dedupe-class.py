
file_name = "emails.txt"
new_file_name = "duplicate-free-emails.txt"

duplicate_free_emails = []

with open(file_name) as file_object:
    #print(file_object.read) -----> do this to check it's printing
    contents = file_object.read()
    contents = contents.replace("\n","")
emails = contents.split(', ')

#print(contents)
#fake_emails = "johndoe@gmail.com, marydoe@gmail.com"
#print(fake_emails.split(", "))

for email in emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

#email_with_new_line = "\njohndoe@gmail.com"
#print(email_with_new_line)
#print(email_with_new_line.replace("\n", ""))
#for item in duplicate_free_emails:
#    print(item.replace("\n", ""))   

with open(new_file_name,"w") as file_object:
    for item in duplicate_free_emails:
        file_object.write(item + "\n")





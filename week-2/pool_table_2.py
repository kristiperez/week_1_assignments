

file_name = "06-05-2019.txt"
number_of_tables = 12
tables = []
import datetime
user_input = ""
#will need to use __dict__ to save to json.  convert pooltable object to dictionary

class PoolTable:
    def __init__(self,number):
        self.number = number
        self.start = datetime.datetime.now().replace(microsecond=0)
        self.end = datetime.datetime.now().replace(microsecond=0)
        self.total_time = 0.0
        self.occupied = "NOT OCCUPIED"

def create_tables():
    for index in range(number_of_tables):
        table_number = index + 1
        p = PoolTable(table_number)
        tables.append(p)        
    
create_tables()

#def menu():
#    return input("1) Open a table \n2) View all tables\n3) Close a table\n")
#user_input = menu()

#def menu():
#    user_input = input("1) View all tables \n2) Open a table \n3) Close a table\n4) Quit\n")
#    return user_input   
#user input = what is returned from the calling the menu
#user_input = menu()

def menu():
    print("1) View all tables \n2) Open a table \n3) Close a table\n4) Quit\n")

menu()

while user_input != "4":
    user_input = input("Enter your selection: ")
   
    if user_input =="1":
        for item in tables:
            print(f"{item.number} - {item.start} - {item.occupied}")

    elif user_input =="2":
        table_number = int(input("Enter table number: "))
        table_number = table_number - 1
        if tables[table_number].occupied == "OCCUPIED":
            print(f"Table {tables[table_number].number} is occupied.")
        else:
            tables[table_number].start = datetime.datetime.now().replace(microsecond=0)
            tables[table_number].occupied = "OCCUPIED"
            for item in tables:
                print(f"{item.number} - {item.start} - {item.occupied}")


    elif user_input =="3":
        table_number = int(input("Enter table number: "))
        table_number = table_number -1
        tables[table_number].end = datetime.datetime.now().replace(microsecond=0)
        tables[table_number].occupied = "NOT OCCUPIED"
        tables[table_number].total_time = tables[table_number].end - tables[table_number].start

        with open(file_name,"a") as file_object:
            file_object.write(f"{tables[table_number].number} - {tables[table_number].start} - {tables[table_number].end} - {tables[table_number].total_time} \n")
        
        for item in tables:
            print(f"{item.number} - {item.start} - {item.end} - {item.total_time} - {item.occupied}")


    

number_of_tables = 12
tables = []
import datetime
user_input = ""

#will need to use __dict__ to save to json.  convert pooltable object to dictionary

class PoolTable:
    def __init__(self,number):
        self.number = number
        self.start = datetime.datetime.now()
        self.end = datetime.datetime.now()
        self.total_time = 0.0
    
    @staticmethod
    def create_tables():
        for index in range(number_of_tables):
            table_number = index + 1
            p = PoolTable(table_number)
            tables.append(p)

PoolTable.create_tables()

#def menu():
#    return input("1) Open a table \n2) View all tables\n3) Close a table\n")

#user_input = menu()

def menu():
    user_input = input("1) Open a table \n2) View all tables\n3) Close a table\n")
    return user_input   

menu()

if user_input == "1":
    table_number = input("Enter table number: ")
    table_number = table_number - 1
    tables[table_number].start_time = str(datetime.datetime.now)

elif user_input =="2":
    for index in range(0,len(tables)):
        print(f"hello")




       



















    
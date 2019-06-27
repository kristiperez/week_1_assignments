


tasks = [] #empty array

user_input = ""

while user_input != "q":
     
    if user_input == "1":
        title = input("Enter title: ")
        priority = input("Enter priority (high, medium, low): ")

        task = {
            "title": title,
            "priority": priority
        }

        tasks.append(task)
    elif user_input == "2":   

        for index in range(0,len(tasks)):
            result = tasks[index]
            print(f"{index+1} - {result['title']} - {result['priority']}")

        deleted_input = int(input("Enter task number to be delted: "))

        def delete_task():
            del tasks[deleted_input - 1]

        delete_task()

    elif user_input == "3":
        for index in range(0,len(tasks)):
            result = tasks[index]
            print(f"{index+1} - {result['title']} - {result['priority']}")

    user_input = input("Press 1 to add task, press 2 to delete task, press 3 to view all tasks and q to quit: ")

            

    

   

   
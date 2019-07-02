
tasks = []

class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority


user_input = ""

while user_input != "q":

    if user_input == "1":

        title = input("Enter a title for your task: ")
        priority = input("Enter a priority for this task: ")

        user_task = Task(title,priority)

        tasks.append(user_task)
        #accesses index number
        with open("task.txt") as file_object:
            lines = file_object.readlines()
      
        with open("task.txt", "a") as file_object:
            file_object.write(f"{str(len(lines))} - {title} - {priority} \n")
            

    elif user_input == "2":

        for index in range(0,len(tasks)):
            print(f"{index + 1} - {tasks[index].title} - {tasks[index].priority}")

        delted_input = int(input("Enter the number of the task you want to delete: "))

        def delete_task():
            del tasks[delted_input - 1]
        
        delete_task()

    elif user_input == "3":
        for index in range(0,len(tasks)):
            print(f"{index + 1} - {tasks[index].title} - {tasks[index].priority}")     
                

    user_input = input("Press 1 to add taks \nPress 2 to delete task \nPress 3 to view all tasks \nPress 'q' to quit: ")


# To do list

# A list to store the tasks
tasks = []


# Function to display the menu
def show_menu():
    print("--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2.Add Task")
    print("3.Remove Task")
    print("4.Exit")


# Function for viewing the task
def view_tasks():
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        print("Your tasks: ") 
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}") 



# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added")


# Function to remove the task
def remove_task():
    view_tasks()
    if len(tasks)>0:
        print("Your To_Do list is empty ")
        try:
            task_num = int(input("/n Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' is removed.")
            else:
                print("Ivalid task number")
        except ValueError:
            print("Enter a valid number.")



# Main Program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()  
    elif choice == '3':
        remove_task()  
    elif choice == '4':
        print("Exiting the To-Do list, Goodbye!")
        break  
    else:
        print("Invalid choice, Please try again. ")

    




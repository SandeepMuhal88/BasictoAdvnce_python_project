# Today make basic project of To Do List
# Using the Dictionary make the To Do List

task = {}
def menu():
    print("\n--- **********************************Welcome to To Do List Project************************************ ---")
    print("Press the number between 1 to 7:-")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Mark done Task")
    print("5. View Mark done Task")
    print("6. Delete Task")
    print("7. Exit")


def add_task():
    task_number = input("Enter your task_number(For example:-task-01,task-02 in format):-")
    task_name = input("Enter your task:-")
    task[task_number] = task_name

def view_task():
    if not task:
        print("No task to display!")
    else:
        print("\n--- To-Do List ---")
        for key, value in task.items():
            print(f"- {key}: {value}")
    return task

def delete_task():
    task_number=input("Enter task Number to delete:-")
    if task_number in task:
        del task[task_number]
        print(f"Task '{task_number}' deleted successfully!")
    else:
        print(f"Task '{task_number}' not found!")

def update_task():
    task_number=input("Enter task Number to update:-")
    if task_number in task:
        task[task_number]=input("Enter new task:-")
        print(f"Task '{task_number}' updated successfully!")
    else:
        print(f"Task '{task_number}' not found!")

def mark_done():
    task_number=input("Enter task Number to mark done:-")
    if task_number in task:
        print(f"Task '{task_number}' marked done successfully!")
    else:
        print(f"Task '{task_number}' not found!")

while True:
    menu()
    choice = int(input("Enter your choice:-"))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        view_done()
    elif choice == 5:
        update_task()
    elif choice == 6:
        delete_task()
    elif choice == 7:
        break
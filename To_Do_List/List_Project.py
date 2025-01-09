# Lists to store tasks
tasks = []
completed_tasks = []

# Function to display the menu
def menu():
    print("\n--- ********************************** Welcome to To-Do List Project ************************************ ---")
    print("Press the number between 1 to 7:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. View Completed Tasks")
    print("6. Delete Task")
    print("7. Exit")

# Add a new task
def add_task():
    task_name = input("Enter the task: ")
    task = {"task_id": len(tasks) + 1, "task_name": task_name}
    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display!")
    else:
        print("\n--- Pending Tasks ---")
        for task in tasks:
            print(f"Task ID: {task['task_id']}, Task: {task['task_name']}")

# Update an existing task
def update_task():
    if not tasks:
        print("No tasks available to update!")
        return
    
    task_id = int(input("Enter the task ID to update: "))
    for task in tasks:
        if task["task_id"] == task_id:
            new_task_name = input("Enter the new task: ")
            task["task_name"] = new_task_name
            print(f"Task ID {task_id} updated successfully!")
            return
    
    print(f"Task ID {task_id} not found!")

# Mark a task as done
def mark_done():
    if not tasks:
        print("No tasks available to mark as done!")
        return
    
    task_id = int(input("Enter the task ID to mark as done: "))
    for task in tasks:
        if task["task_id"] == task_id:
            completed_tasks.append(task)
            tasks.remove(task)
            print(f"Task ID {task_id} marked as done successfully!")
            return
    
    print(f"Task ID {task_id} not found!")

# View completed tasks
def view_completed_tasks():
    if not completed_tasks:
        print("No completed tasks to display!")
    else:
        print("\n--- Completed Tasks ---")
        for task in completed_tasks:
            print(f"Task ID: {task['task_id']}, Task: {task['task_name']}")

# Delete a task
def delete_task():
    if not tasks and not completed_tasks:
        print("No tasks available to delete!")
        return

    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task["task_id"] == task_id:
            tasks.remove(task)
            print(f"Task ID {task_id} deleted successfully from pending tasks!")
            return
    
    for task in completed_tasks:
        if task["task_id"] == task_id:
            completed_tasks.remove(task)
            print(f"Task ID {task_id} deleted successfully from completed tasks!")
            return
    
    print(f"Task ID {task_id} not found!")

# Main program loop
while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            update_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            view_completed_tasks()
        elif choice == 6:
            delete_task()
        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a number.")

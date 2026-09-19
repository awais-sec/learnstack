import sys

# Initialize an empty list to store tasks
tasks = []

def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append({"task": task, "status": "Pending"})
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")

def view_tasks():
    """View all tasks in the to-do list."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} - {task['status']}")

def update_task():
    """Update a task's status or content."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            print("1. Mark as Completed")
            print("2. Update Task Content")
            choice = input("Choose an option (1/2): ").strip()
            if choice == "1":
                tasks[task_number - 1]["status"] = "Completed"
                print("Task marked as completed.")
            elif choice == "2":
                new_task = input("Enter the updated task: ").strip()
                if new_task:
                    tasks[task_number - 1]["task"] = new_task
                    print("Task updated.")
                else:
                    print("Updated task cannot be empty.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to display the menu and handle user input."""
    while True:
        print("\nSimple To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            print("Exiting the to-do list. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

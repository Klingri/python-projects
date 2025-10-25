# simple_todo_app.py

def run_todo_app():
    """
    Runs a simple command-line To-Do List application.
    Users can add tasks, view tasks, and mark tasks as complete.
    Tasks are stored in memory and are lost when the app closes.
    """

    tasks = [] # List to store tasks. Each task will be a dictionary.
               # Example: {'description': 'Buy groceries', 'completed': False}

    print("Welcome to your Simple To-Do List App!")
    print("--------------------------------------")

    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add a new task
            task_description = input("Enter the task description: ")
            tasks.append({'description': task_description, 'completed': False})
            print(f"Task '{task_description}' added!")

        elif choice == '2':
            # View all tasks
            if not tasks:
                print("Your To-Do list is empty!")
            else:
                print("\nYour Current Tasks:")
                print("--------------------")
                for i, task in enumerate(tasks):
                    status = "✓" if task['completed'] else " "
                    print(f"{i + 1}. [{status}] {task['description']}")
                print("--------------------")

        elif choice == '3':
            # Mark a task as complete
            if not tasks:
                print("No tasks to mark complete. Your To-Do list is empty.")
                continue # Go back to the menu

            try:
                task_number = int(input("Enter the number of the task to mark as complete: "))
                if 1 <= task_number <= len(tasks):
                    task_index = task_number - 1
                    if tasks[task_index]['completed']:
                        print(f"Task '{tasks[task_index]['description']}' is already complete.")
                    else:
                        tasks[task_index]['completed'] = True
                        print(f"Task '{tasks[task_index]['description']}' marked as complete!")
                else:
                    print("Invalid task number. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            # Exit the application
            print("Exiting To-Do List App. Goodbye!")
            break # Exit the while loop

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures that run_todo_app() is called only when the script is executed directly.
if __name__ == "__main__":
    run_todo_app()


import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_complete(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to mark complete: "))
    tasks[choice-1]["completed"] = True
    save_tasks(tasks)
    print("Task marked as complete!")

def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to delete: "))
    tasks.pop(choice-1)
    save_tasks(tasks)
    print("Task deleted successfully!")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks\n2. Add Task\n3. Mark Complete\n4. Delete Task\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("📋 No tasks found.")
    else:
        print("\n✅ To-Do List:")
        for idx, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{idx + 1}. [{status}] {task['title']}")
        print()

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            deleted = tasks.pop(idx)
            print(f"Deleted: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n🛠 Menu: add | done | delete | show | quit")
        choice = input("Choose: ").strip().lower()
        if choice == "add":
            add_task(tasks)
        elif choice == "done":
            mark_done(tasks)
        elif choice == "delete":
            delete_task(tasks)
        elif choice == "show":
            show_tasks(tasks)
        elif choice == "quit":
            save_tasks(tasks)
            print("Bye! 👋")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    menu()

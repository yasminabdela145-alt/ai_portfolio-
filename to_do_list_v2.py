# to_do_list_v2.py

# To-Do List App with File Saving
# Tasks are saved in 'tasks.txt' so they stay after closing the program.

tasks = []

# Load tasks from file if it exists
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

def show_menu():
    print("\n📋 To-Do List Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Quit")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        save_tasks()
        print(f"✅ '{task}' added to the list!")

    elif choice == "2":
        if not tasks:
            print("⚠️ No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("⚠️ No tasks to remove.")
        else:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks()
                print(f"🗑️ '{removed}' removed from the list.")
            else:
                print("⚠️ Invalid task number.")

    elif choice == "4":
        save_tasks()
        print("👋 Goodbye! Your tasks are saved in tasks.txt")
        break

    else:
        print("⚠️ Invalid choice. Please select 1-4.")
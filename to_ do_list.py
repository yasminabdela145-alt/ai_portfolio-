# to_do_list.py

# A simple To-Do List app in Python
# You can add tasks, view them, and remove them.

tasks = []

def show_menu():
    print("\n📋 To-Do List Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
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
                print(f"🗑️ '{removed}' removed from the list.")
            else:
                print("⚠️ Invalid task number.")

    elif choice == "4":
        print("👋 Goodbye! Thanks for using To-Do List App.")
        break

    else:
        print("⚠️ Invalid choice. Please select 1-4.")
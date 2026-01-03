# Basic To-Do List

tasks = []

task = input("Enter a new task: ")

tasks.append(task)

print("Task added successfully.")

print("\nCurrent task list:")
for t in tasks:
    print("- " + t)


Menu System with Conditionals

tasks = []

print("--- To-Do Menu ---")
print("1. Add a task")
print("2. View tasks")
print("3. Delete a task")
print("4. Quit")

choice = input("Enter your choice: ")

if choice == "1":
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

elif choice == "2":
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Task list:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

elif choice == "3":
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        num = input("Enter the task number to delete: ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(tasks):
                removed_task = tasks.pop(num - 1)
                print(f"Deleted task: {removed_task}")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")

elif choice == "4":
    print("Goodbye!")

else:
    print("Invalid choice. Please try again.")



#Full To-Do Application Loop


tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("Task list:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            num = input("Enter the task number to delete: ")
            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(tasks):
                    removed_task = tasks.pop(num - 1)
                    print(f"Deleted task: {removed_task}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting the To-Do App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

#salah-eddine houmadi

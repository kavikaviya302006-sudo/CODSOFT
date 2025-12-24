tasks = []

while True:
    print("\n------ TO-DO LIST MENU ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == '3':
        if not tasks:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            num = int(input("Enter task number to update: "))
            new_task = input("Enter updated task: ")
            tasks[num - 1] = new_task
            print("Task updated successfully!")

    elif choice == '4':
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            print("Deleted task:", removed)

    elif choice == '5':
        tasks.clear()
        print("All tasks cleared!")

    elif choice == '6':
        print("Thank you! Exiting To-Do List.")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")

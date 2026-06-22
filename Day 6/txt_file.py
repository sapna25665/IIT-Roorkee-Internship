file_name = "tasks.txt"

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        with open(file_name, "a") as file:
            file.write(task + "\n")
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        try:
            with open(file_name, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No tasks found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

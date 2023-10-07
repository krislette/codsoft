import sys


todo_list = []


def display_design(count = 50):
    """Prints a line of dashes for design purposes."""
    for i in range(count):
        print("-", end="", flush=True)
    print("-")


def display_menu():
    """Displays the menu of the program."""
    display_design()
    print("-------------------- TO-DO LIST -------------------")
    display_design()
    
    print("[1] Add a task")
    print("[2] Delete a task")
    print("[3] View list")
    print("[4] Exit")


def print_list():
    """Prints the current to-do list."""
    for task_number, task in todo_list:
        print(f"({task_number}) {task}")


def is_valid(input, min, max):
    """Returns True if the input is within the range of min and max."""
    if not min <= input <= max: return False
    else: return True


def get_input(min, max):
    """Returns a valid integer after checking if it is within the range of min and max."""
    try:
        user_input = int(input("Choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_input(min, max)

    valid_input = is_valid(user_input, min, max)

    if not valid_input:
        print(f"Invalid input. Enter numbers from {min}-{max} only.")
        return get_input(min, max)

    return user_input


def add_task():
    """Adds a task to the to-do list."""
    display_design()
    print("--------------------- Add task --------------------")
    display_design()

    task_number = len(todo_list)

    new_task = input("Enter task name: ")
    print("Task added successfully.")
    task_number += 1

    todo_list.append((task_number, new_task))

    try_again = get_answer("Add another task")
    if try_again == 1: add_task()
    else: return


def delete_task():
    """Deletes a task from the to-do list."""
    display_design()
    print("------------------- Delete task -------------------")
    display_design()
    print_list()

    task_number = len(todo_list)

    if not todo_list:
        print("There are no current tasks...")
    else:
        task_to_delete = int(input("Enter task number to remove: "))

        all_task_numbers = [sub_list[0] for sub_list in todo_list]

        if task_to_delete in all_task_numbers:
            index_to_delete = all_task_numbers.index(task_to_delete)
            todo_list.pop(index_to_delete)
            print(f"Task {task_to_delete} successfully removed.")

            for i in range(index_to_delete, len(todo_list)):
                todo_list[i] = (todo_list[i][0] - 1, todo_list[i][1])

            task_number -= 1
        else:
            print(f"Task not found.")

    try_again = get_answer("Delete another task")
    if try_again == 1: delete_task()
    else: return


def view_list():
    """Displays the current to-do list."""
    display_design()
    print("-------------------- To-do List -------------------")
    display_design()

    if not todo_list:
        print("There are no current tasks...")
    else:
        print_list()

    try_again = get_answer("View the list again")
    if try_again == 1: view_list()
    else: return


def confirm_exit():
    """Asks the user if they want to exit the program."""
    display_design()
    print("----------------------- Exit ----------------------")
    display_design()

    print("Are you sure you want to exit the program?\n[1] Yes\n[2] No")
    display_design()
    user_answer = get_input(1, 2)

    if user_answer == 1:
        display_design()
        print("Thank you for using my program!")
        display_design()
        sys.exit()
    elif user_answer == 2:
        display_design()
        print("|||||||||||| Restarting the program... ||||||||||||")
        main()


def get_answer(message):
    """Asks the user if they want to do the same transaction again"""
    display_design()

    print(f"[1] {message}")
    print("[2] Go back to main menu")

    return get_input(1, 2)


def main():
    """Main function of the program."""
    while True:
        display_menu()
        user_input = get_input(1, 4)

        if user_input == 1:
            add_task()
        elif user_input == 2:
            delete_task()
        elif user_input == 3:
            view_list()
        else:
            confirm_exit()


main()
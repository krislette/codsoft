import sys


def display_design(count = 50):
    """Prints a line of dashes for design purposes."""
    for i in range(count):
        print("-", end="", flush=True)
    print("-")


def check_valid_input(message):
    """Returns a valid integer from the user."""
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("[ERROR]. Enter a valid integer.")


def print_operations():
    """Prints the operations that the user can choose from."""
    print("Enter an operation [1 to 4]:")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")


def get_operation():
    """Returns the valid operation that the user wants to perform."""
    print_operations()
    display_design()

    while True:
        try:
            math_operation = int(input("Choice: "))
            assert 1 <= math_operation <= 4 
        except ValueError:
            print("[ERROR]. Enter a valid integer.")
        except AssertionError:
            print("[ERROR] Enter numbers from 1 to 4 only.")
        else:
            return math_operation


def evaluate_solution(input_one, input_two, math_operation):
    """Returns the calculated answer of the two inputs."""
    if math_operation == 1:
        return f"{input_one} + {input_two} = {input_one + input_two}"
    elif math_operation == 2:
        return f"{input_one} - {input_two} = {input_one - input_two}"
    elif math_operation == 3:
        return f"{input_one} * {input_two} = {input_one * input_two}"
    elif math_operation == 4:
        if input_two == 0:
            return f"{input_one} / {input_two} = undefined"
        else:
            return f"{input_one} / {input_two} = {input_one / input_two}"


def try_again():
    """Asks the user if they want to try the program again."""
    print("------ Do you want to try the program again? ------")
    print("------- Enter 1 if yes, enter any key if no -------")

    display_design()
    user_answer = input("Choice: ")

    if user_answer == "1":
        display_design()
        print("|||||||||||| Restarting the program... ||||||||||||")
        main()
    else:
        display_design()
        print("Thank you for using my program!")
        display_design()
        sys.exit()


def main():
    """Main function of the program."""
    display_design()
    print("\t\tCALCULATOR PROGRAM")
    display_design()

    print("---------------- Enter two numbers ----------------")
    display_design()

    input_one = check_valid_input("First number: ")
    input_two = check_valid_input("Second number: ")

    display_design()

    math_operation = get_operation()
    final_answer = evaluate_solution(input_one, input_two, math_operation)  

    display_design()
    print(f"Final Answer: {final_answer}")
    display_design()

    try_again()


main()
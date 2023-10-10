import sys
import random


def display_design(count = 50):
    """Prints a line of dashes for design purposes."""
    for i in range(count):
        print("-", end="", flush=True)
    print("-")


def generate_password():
    """Generates a password and passes it to the assess_password_strength function."""
    possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
    generated_password = ""
    is_valid_password = False

    while not is_valid_password:
        try:
            password_length = int(input("Enter desired password length: "))
            assert password_length > 0

            for i in range(password_length):
                generated_password += random.choice(possible_characters)
        except ValueError:
            print("[ERROR] Enter integer values only.")
        except AssertionError:
            print("[ERROR] Enter a value greater than zero.")
        else:
            assess_password_strength(generated_password, password_length)


def assess_password_strength(password, length):
    """Assesses the strength of the generated password and passes it to the print_password function."""
    if 1 <= length <= 7:
        print_password(password, "Very weak")
    elif 8 <= length <= 10:
        print_password(password, "Weak")
    elif 11 <= length <= 13:
        print_password(password, "Good")
    elif 14 <= length <= 16:
        print_password(password, "Strong")
    else:
        print_password(password, "Very Strong")


def print_password(password, password_strength):
    """"Prints the generated password and its strength."""
    display_design()
    print("Generated password: ")
    print(password)
    print(f"Status: {password_strength}")

    ask_user()


def ask_user():
    """Asks the user if they want to try the program again."""
    display_design()
    print("---- Do you want to generate another password? ----")
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
    print("---------------- PASSWORD GENERATOR ---------------")
    display_design()
    generate_password()


main()
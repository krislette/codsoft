import sys


MAX_CONTACTS = 100
contact_book = []


class Contact:

    number_of_contacts = 0
    
    def __init__(self):
        self.full_name = ""
        self.phone_number = ""
        self.email_address = ""
        self.house_address = ""

    def add_contact(self):
        self.full_name = input("Enter full name: ").title()
        self.phone_number = input("Enter phone number: ")
        self.email_address = input("Enter email address: ")
        self.house_address = input("Enter house address: ").title()
        Contact.number_of_contacts += 1

    def display_contact(self):
        print(f"Name: {self.full_name}")
        print(f"Phone Number: {self.phone_number}")


def display_design(count = 50):
    """Prints a line of dashes for design purposes."""
    for i in range(count):
        print("-", end="", flush=True)
    print("-")


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


def is_empty():
    """Returns True if the contact book is empty."""
    if len(contact_book) == 0:
        display_design()
        print("-> No contacts found. Please add a contact first <-")
        return True


def display_menu():
    """Displays the main menu."""
    display_design()
    print("------------------- CONTACT BOOK ------------------")
    display_design()
    print("[1] Add Contact")
    print("[2] View Contact List")
    print("[3] Search Contact")
    print("[4] Update Contact")
    print("[5] Delete Contact")
    print("[6] Exit")


def get_answer(message):
    """Asks the user if they want to do the same transaction again"""
    print(f"[1] {message}")
    print("[2] Go back to main menu")
    return get_input(1, 2)


def add_contact():
    """Adds a contact to the contact book."""
    if Contact.number_of_contacts == MAX_CONTACTS:
        display_design()
        print("\t  -> Contact list already full <-") 
        return
    
    for empty_slot in range(MAX_CONTACTS):
        display_design()
        print("------------------- Add Contact -------------------")
        display_design()
        entry = Contact()
        entry.add_contact()
        contact_book.append(entry)
        display_design()
        print("\t -> Contact successfully added <-")
        display_design()
        
        try_again = get_answer("Add another contact")
        if Contact.number_of_contacts == MAX_CONTACTS:
            display_design()
            print("\t  -> Contact list already full <-") 
            break
        else:
            if try_again == 1: continue
            else: break


def display_contacts():
    """Displays all the contacts in the contact book."""
    if is_empty(): return

    display_design()
    print("------------------- Contact List ------------------")
    display_design()

    for i in range(len(contact_book)):
        print(f"[Contact {i + 1}]")
        contact_book[i].display_contact()
        display_design()

    try_again = get_answer("View contact list again")
    if try_again == 1: display_contacts()
    else: return


def search_contact():
    """Searches for a contact in the contact book."""
    if is_empty(): return

    display_design()
    print("------------------ Search Contact -----------------")
    display_design()
    user_choice = print_choices("Search")
    matching_contacts = match_contacts(user_choice)
    display_design()

    if matching_contacts:
        for contact in matching_contacts:
            print_contact_found()
            contact.display_contact()
            print(f"Email Address: {contact.email_address}")
            print(f"House Address: {contact.house_address}")
    else:
        print("\t\t\b-> Contact not found <-")

    display_design()

    try_again = get_answer("Search another contact")
    if try_again == 1: search_contact()
    else: return


def update_contact():
    """Updates a contact in the contact book."""
    if is_empty(): return

    display_design()
    print("------------------ Update Contact -----------------")
    display_design()
    user_choice = print_choices("Update")
    matching_contacts = match_contacts(user_choice)
    display_design()

    if matching_contacts:
        print_contact_found()
        for contact in matching_contacts:
            contact.full_name = input("Enter full name: ").title()
            contact.phone_number = input("Enter new phone number: ")
            contact.email_address = input("Enter new email address: ")
            contact.house_address = input("Enter new house address: ").title()
            display_design()
            print("\t-> Contact successfully updated <-")
    else:
        print("\t\t\b-> Contact not found <-")

    display_design()

    try_again = get_answer("Update another contact")
    if try_again == 1: update_contact()
    else: return


def delete_contact():
    """Deletes a contact in the contact book."""
    if is_empty(): return
    
    display_design()
    print("------------------ Delete Contact -----------------")
    display_design()
    user_choice = print_choices("Delete")
    matching_contacts = match_contacts(user_choice)

    display_design()
    if matching_contacts:
        print_contact_found()
        print("Are you sure you want to delete this contact?\n[1] Yes\n[2] No")
        display_design()
        user_answer = get_input(1, 2)
        if user_answer == 1:
            for contact in matching_contacts:
                contact_book.remove(contact)
                display_design()
                print("\t-> Contact successfully deleted <-")
        else :
            display_design()
            print("\t\t\b\b\b-> Contact not deleted <-")
    else:
        print("\t\t\b-> Contact not found <-")

    display_design()

    try_again = get_answer("Delete another contact")
    if try_again == 1: delete_contact()
    else: return


def print_choices(message):
    """Prints the choices for searching, updating, and deleting a contact and returns the user's choice."""
    print(f"[1] {message} contact by name")
    print(f"[2] {message} contact by phone number")
    return get_input(1, 2)


def print_contact_found():
    """Prints a message if a contact is found."""
    print("\t\t-> Contact found <-")
    display_design()

    
def match_contacts(choice):
    """Takes the user's choice and returns a list of matching contacts."""
    display_design()
    if choice == 1:
        full_name = input("Enter full name: ").title()
        return search_contact_by_name(full_name)
    else:
        phone_number = input("Enter phone number: ")
        return search_contact_by_phone(phone_number)
    

def search_contact_by_name(full_name):
    """Returns a list of matching contacts based on the last name."""
    matching_contacts = [contact for contact in contact_book if contact.full_name == full_name]
    return matching_contacts


def search_contact_by_phone(phone_number):
    """Returns a list of matching contacts based on the phone number."""
    matching_contacts = [contact for contact in contact_book if contact.phone_number == phone_number]
    return matching_contacts


def exit_program():
    """Asks the user if they want to exit the program."""
    display_design()
    print("----------------------- Exit ----------------------")
    display_design()
    print("Are you sure you want to exit the program?\n[1] Yes\n[2] No")
    display_design()
    user_answer = get_input(1, 2)

    display_design()
    if user_answer == 1:
        print("Thank you for using my program!")
        display_design()
        sys.exit()
    elif user_answer == 2:
        print("|||||||||||| Restarting the program... ||||||||||||")
        main()


def main():
    """Main function of the program."""
    while True:
        display_menu()
        user_input = get_input(1, 6)

        if user_input == 1:
            add_contact()
        elif user_input == 2:
            display_contacts()
        elif user_input == 3:
            search_contact()
        elif user_input == 4:
            update_contact()
        elif user_input == 5:
            delete_contact()
        else:
            exit_program()


main()
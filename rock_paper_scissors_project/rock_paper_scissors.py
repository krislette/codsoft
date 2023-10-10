import sys
import random
from tabulate import tabulate


# The round number is used to keep track of the number of rounds played.
round_number = 1

# The scoreboard is a list of lists. Each list contains the name of the score and the score itself.
scoreboard = [
    ["Wins", 0],
    ["Losses", 0],
    ["Ties", 0]
]


def display_design(count = 50):
    """Prints a line of dashes for design purposes."""
    for i in range(count):
        print("-", end="", flush=True)
    print("-")


def get_computer_move():
    """Returns a random move for the computer."""
    possible_moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(possible_moves)
    
    return computer_move


def get_game_result(player_move, computer_move):
    """Takes the player's move and the computer's move and returns the result of the game."""
    if player_move == "rock":
        if computer_move == "rock": return "It's a tie!"
        elif computer_move == "paper": return "You lose!"
        elif computer_move == "scissors": return "You win!"
    elif player_move == "paper":
        if computer_move == "rock": return "You win!"
        elif computer_move == "paper": return "It's a tie!"
        elif computer_move == "scissors": return "You lose!"
    elif player_move == "scissors":
        if computer_move == "rock": return "You lose!"
        elif computer_move == "paper": return "You win!"
        elif computer_move == "scissors": return "It's a tie!"


def track_score(result):
    """Takes the result of the game and updates the scoreboard."""
    if result == "You win!": scoreboard[0][1] += 1
    elif result == "You lose!": scoreboard[1][1] += 1
    elif result == "It's a tie!": scoreboard[2][1] += 1


def print_game_result(user, computer, result):
    """Takes the user's move, the computer's move, and the result of the game and prints them."""
    global round_number
    display_design()
    print("--------------------- Results ---------------------")
    display_design()
    print(f"Your move |---------> {user}\nComputer's move |---> {computer}\nResult |------------> {result}")
    display_design()

    print("-------------------- Scoreboard -------------------")
    print(f"\t\t\t\b\bROUND {round_number}")
    display_design()
    column_names = ["Result", "Points"]
    print(tabulate(scoreboard, headers=column_names, tablefmt="github", stralign="left", numalign="center"))

    play_again()


def play_again():
    """Asks the user if they want to play another round."""
    global round_number
    display_design()
    print("-------- Do you want to play another round? -------")
    print("------- Enter 1 if yes, enter any key if no -------")

    display_design()
    user_answer = input("Choice: ")

    if user_answer == "1":
        display_design()
        print("|||||||||||| Restarting the program... ||||||||||||")
        round_number += 1
        main()
    else:
        display_design()
        print("Thank you for using my program!")
        display_design()
        sys.exit()


def main():
    """Main function of the program."""
    display_design()
    print("------------- ROCK-PAPER-SCISSORS GAME ------------")   
    print("------ Type and enter the name of your move. ------")
    display_design()
    
    print("[] Rock")
    print("[] Paper")
    print("[] Scissors")
    user_input = input("Your move: ")
    user_input = user_input.lower()

    if user_input not in ["rock", "paper", "scissors"]:
        print('[ERROR] Enter "rock", "paper", or "scissors" only')
        return main()

    # Gets the computer's move.
    computer_move = get_computer_move()

    # Gets the result of the game.
    game_result = get_game_result(user_input, computer_move)

    # Updates the scoreboard.
    track_score(game_result)

    # Prints the result of the game.
    print_game_result(user_input, computer_move, game_result)


main()
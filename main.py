# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 06MAY2024 @ 11:59 PM PST. Using grace days, new due date is 08MAY2024 @ 11:59 PM PST.
# Description: One Rep Max Calculator and Projected Training Percentages program.

import time


def main() -> None:
    """
    Main function
    """

    user_max = None
    training_percentages = {}
    training_reps = {}

    while True:
        print_title_desc_commands()
        user_input = input(f"Enter your command: ")

        if user_input.lower() == "max":
            new_max = int(input("Please enter your max as an integer: "))
            user_new_correct = input("Are you sure this is your one rep max? Please enter 'Y'/'Yes', N'/'No', or press Enter to reset your one rep max back to 'None': ")
            if user_new_correct.lower() == "y" or user_new_correct.lower() == "yes":
                user_max = new_max
                print(f"Your one rep max is {user_max} lbs.")
            elif user_new_correct.lower() == "n" or user_new_correct.lower() == "no":
                print(f"Your one rep max has not changed. It is currently {user_max} lbs.")
                pass
            elif user_new_correct.lower() == "" or user_new_correct == " ":
                user_max = None
                print(f"Your one rep max is not set. One rep max currently is {user_max}.")
        elif user_input.lower() == "tp" and user_max is not None:
            for i in range(0, 101, 5):
                training_percent = str(i) + "%"
                training_percentages[training_percent] = user_max * (i / 100)
            print(f"Your training percentage weights (by divisibles of 5) are:")

            for j in training_percentages:
                print(f"Training percent: {j} | training weight: {training_percentages[j]}")
        elif user_input.lower() == "reps" and user_max is not None:
            for idx in range(0, 66, 5):
                training_rep = str(idx) + "%"
                training_reps[training_rep] = "12+ REPS"
            for idx2 in range(70, 81, 5):
                training_rep2 = str(idx2) + "%"
                training_reps[training_rep2] = "8-10 REPS"
            for idx3 in range(85, 91, 5):
                training_rep3 = str(idx3) + "%"
                training_reps[training_rep3] = "5-6 REPS"
            for idx4 in range(95, 101, 5):
                training_rep4 = str(idx4) + "%"
                training_reps[training_rep4] = "1-2 REPS"

            print(f"The suggested reps for your training percentages are:")

            for counter in training_reps:
                print(f"Training percent: {counter} | Suggested reps: {training_reps[counter]}")

        elif user_input.lower() == "help":
            print_help()
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            user_wants_to_exit = input("Are you sure you want to exit? Please enter 'Y' or 'Yes' to exit or 'N' or 'No to stay in the program. ")
            try:
                if user_wants_to_exit.lower() == "y" or user_wants_to_exit.lower() == "yes":
                    break
                elif user_wants_to_exit.lower() == "n" or user_wants_to_exit.lower() == "no":
                    pass
            except TypeError:
                print(f"Your input was not a valid input!")

        print_command_complete()

def print_title() -> None:
    """
    Prints the title of the program.
    """

    print(f"   ____                    _____                      _____       ______                             ")
    print(f"  / __ \\  _ ___  _____    |  __ |  _____   _______   |   _  \\    /  _   |  ___   __    __           ")
    print(f" | /  \\ || |__ || ___ \\   | |__|| | ___ \\ |  ___  |  |  | \\  \\  /  / |  | / _ \\ |  \\  /  |     ")
    print(f" | |  | || | | || |_|_|   | |\\ \\  | |_|_| | |___|_|  |  |  \\  \\/  /  |  || / \\ | \\  \\/  /      ")
    print(f" | \\__/ || | | || |___    | | \\ \\ | |____ | |        |  |   \\ ___/   |  || \\_/ | /  /\\  \\      ")
    print(f"  \\____/ | | |_||_____|   |_|  \\_\\|______||_|        |__|            |__| \\__/\\||__/  \\__|      \n")

def print_program_description() -> None:
    """
    Prints the program's description.
    """

    print(f"One Rep Max to determine Training Percentage Calculator. Improve your lifts using the training percentages determined from your One Rep Max.")
    print(f"WARNING: This program is specifically for beginners who are embarking on their fitness journey. This program will not be very helpful for intermediate and pro lifters.\n")

def print_commands() -> None:
    """
    Prints the main prompt's commands.
    """
    print(f"COMMANDS:")
    print(f"Type 'Max' to enter your one rep max.")
    print(f"Type 'TP' to get your training percentages. This option may only be accessed when your one rep max has been inputted.")
    print(f"Type 'Reps' to get the recommended repetition range for each of your training percentages.")
    print(f"Type 'Help' to get a more detailed descriptions.")
    print(f"Type 'Q' or 'Quit' to exit the program.")

def print_title_desc_commands() -> None:
    """
    Function to call the title, program description & warning, and the main prompt commands. Leveraged from Professor Letaw's
    example video https://canvas.oregonstate.edu/courses/1958534/assignments/9583963?module_item_id=24164834
    """
    print_title()
    print_program_description()
    print_commands()

def print_command_complete() -> None:
    """
    Print message for when a command is finished processing. Leveraged from Professor Letaw's
    example video https://canvas.oregonstate.edu/courses/1958534/assignments/9583963?module_item_id=24164834
    """
    print(f"\nPlease wait about one (1) second for your current command to finish. Only one command at a time. ")
    waiting = ""

    for i in range(3):
        time.sleep(0.33)
        waiting += "."
        print(f"{waiting}")

    print(f"\n")

def print_help() -> None:
    """
    Print function for the "Help" command.
    """

    print(f"The 'Max' command will allow the user to enter their one rep max in lbs. The user's initial max is set to 'None'. Once the user inputs a one rep max, the command prompt will confirm if this is the user's one rep max.")
    print(f"\tIf the user types 'Y' or 'Yes', then their new max will be set.")
    print(f"\tIf the user types 'N' or 'No', their one rep max will remain unchanged.")
    print(f"\tIf the user presses the Enter key, their one rep max will be cleared back to 'None'.\n")

    print(f"The 'TP' command will determine what the training weights for each respective training percentage from 0% to 100% in intervals of 5%. This command will print out each training percentage and associated training weight.")
    print(f"\tThis command will only work if there is a one rep max inputted from the user.\n")

    print(f"The 'Reps' command will determine what the suggested repetition range for each respective training percentage from 0% to 100% in intervals of 5%. This command will print out each training percentage and suggested repetition range.")
    print(f"\tThis command will only work if there is a one rep max inputted from the user.\n")

    print(f"The 'Help' command provides detailed descriptions of each command listed from the main prompt. Please read each description carefully.\n")

    print(f"The 'Q' or 'Quit' command allows the user to exit the program. It will provide a subsequent prompt asking if the user is sure they want to exit the program.")

if __name__ == "__main__":
    main()
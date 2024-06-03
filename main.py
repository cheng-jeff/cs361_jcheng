# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 06MAY2024 @ 11:59 PM PST. Using grace days, new due date is 08MAY2024 @ 11:59 PM PST.
# Description: One Rep Max Calculator and Projected Training Percentages program.

import time
import zmq
import json

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
    print(f"Type 'Convert' to convert your current one rep max from imperial units to metric units or vice-versa.")
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

def print_waiting() -> None:
    """
    Waiting print function.
    """
    waiting = ""

    for i in range(3):
        time.sleep(0.33)
        waiting += "."
        print(f"{waiting}")

def main() -> None:
    """
    Main function
    """

    # Establish connection with Microservice A socket.
    context = zmq.Context()

    print(f"Establishing connections to microservices...")
    socket_a = context.socket(zmq.REQ)
    socket_b = context.socket(zmq.REQ)
    socket_c = context.socket(zmq.REQ)
    socket_d = context.socket(zmq.REQ)

    print_waiting()

    socket_a.connect("tcp://localhost:7777")
    print(f"Connection with Microservice A established.")
    socket_b.connect("tcp://localhost:5555")
    print(f"Connection with Microservice B established.")
    socket_c.connect("tcp://localhost:8888")
    print(f"Connection with Microservice C established.")
    socket_d.connect("tcp://localhost:9999")
    print(f"Connection with Microservice D established.")



    user_max = None
    training_percentages = {}
    training_reps = {}

    user_units = None
    user_message = None

    while True:
        print_title_desc_commands()
        user_input = input(f"Enter your command: ")

        if user_input.lower() == "max":

            try:
                new_max = int(input("Please enter your max as an integer: "))
            except ValueError:
                print(f"\nYou did not enter an integer. Please enter an integer.\n")
                continue

            new_units = input("Please enter the units for your one rep max: (lbs/kgs) ")
            new_units_valid = None

            if new_units.lower() == "lbs" or new_units.lower() == "kgs":
                new_units_valid = True
            else:
                new_units_valid = False

            while not new_units_valid:
                new_units = input("You did not enter lbs or kgs. Please enter lbs or kgs: ")

                if new_units.lower() == "lbs" or new_units.lower() == "kgs":
                    new_units_valid = True
                else:
                    new_units_valid = False

            user_new_correct = input("Are you sure this is your one rep max? Please enter 'Y'/'Yes', N'/'No', or press Enter to reset your one rep max back to 'None': ")

            if user_new_correct.lower() == "y" or user_new_correct.lower() == "yes":
                user_max = new_max

                client_max_json = {
                    "user_max" : user_max,
                    "unit" : new_units
                }

                socket_b.send_json(client_max_json)
                print(f"\nClient sending to Microservice B: {client_max_json}")

                microservice_b_max = socket_b.recv_json()
                print(f"Client receiving from Microservice B: {microservice_b_max}\n")

                user_max_print = microservice_b_max["user_max"]
                user_units = microservice_b_max["units"]
                user_message = microservice_b_max["message"]

                print(f"{user_max_print}")
                print(f"The units of your one rep max is {user_units}.")
                print(f"{user_message}")
            elif user_new_correct.lower() == "n" or user_new_correct.lower() == "no":
                if user_max is None:
                    print(f"You do not currently have a one rep max entered. Please enter a one rep max.")
                else:
                    print(f"Your one rep max has not changed. It is currently {user_max} lbs.")
                pass
            elif user_new_correct.lower() == "" or user_new_correct == " ":
                user_max = None
                print(f"Your one rep max is not set. One rep max currently is {user_max}.")
        elif user_input.lower() == "tp":
            if user_max is None:
                print(f"\nYou have not entered a one rep max. Please enter a one rep max.\n")
                continue

            client_msc_tp_json = {
                "command" : "tp",
                "user_max" : user_max
            }

            socket_c.send_json(client_msc_tp_json)
            print(f"\nClient sending to Microservice C: {client_msc_tp_json}")

            msc_tp_json = socket_c.recv_json()
            print(f"Client receiving from Microservice C: {msc_tp_json}")


            for i in msc_tp_json["tp"]:
                print(f"Training percent: {i} | training weight: {msc_tp_json['tp'][i]}")

        elif user_input.lower() == "reps":
            if user_max is None:
                print(f"\nYou have not entered a one rep max. Please enter a one rep max.\n")
                continue

            client_msc_reps_json = {
                "command" : "reps",
                "user_max" : user_max
            }

            socket_c.send_json(client_msc_reps_json)
            print(f"Client sending to Microservice C: {client_msc_reps_json}")

            # for idx in range(0, 66, 5):
            #     training_rep = str(idx) + "%"
            #     training_reps[training_rep] = "12+ REPS"
            # for idx2 in range(70, 81, 5):
            #     training_rep2 = str(idx2) + "%"
            #     training_reps[training_rep2] = "8-10 REPS"
            # for idx3 in range(85, 91, 5):
            #     training_rep3 = str(idx3) + "%"
            #     training_reps[training_rep3] = "5-6 REPS"
            # for idx4 in range(95, 101, 5):
            #     training_rep4 = str(idx4) + "%"
            #     training_reps[training_rep4] = "1-2 REPS"

            msc_reps_json = socket_c.recv_json()
            print(f"Client receiving from Microservice C: {msc_reps_json}")

            print(f"\nThe suggested reps for your training percentages are:")

            for counter in msc_reps_json["reps"]:
                print(f"Training percent: {counter} | Suggested reps: {msc_reps_json['reps'][counter]}")

        elif user_input.lower() == "convert":
            if user_max is None:
                print(f"\nYou have not entered a one rep max. Please enter a one rep max.\n")
                continue

            try:
                if user_units.lower() == "lbs":
                    convert_unit = "kgs"
                elif user_units.lower() == "kgs":
                    convert_unit = "lbs"

                pack_json = {
                    "convert_type" : convert_unit,
                    "values" : user_max
                }
            except AttributeError:
                print(f"\nIt does not seem you have entered a one rep max. Please enter a one rep max.\n")
                continue
            else:
                socket_a.send_json(pack_json)
                print(f"\nClient sending to Microservice A: {pack_json}")

                convert_json = socket_a.recv_json()
                print(f"Client received from Microservice A: {convert_json}\n")

                converted_max = convert_json["converted_values"]
                converted_unit = convert_json["converted_type"]

                print(f"Your converted one rep max is {converted_max}!")
                print(f"The units of your converted one rep max is {converted_unit}!\n")

        elif user_input.lower() == "help":

            help_msg_valid = True

            help_json = {
                "help_msg_valid" : help_msg_valid,
            }

            socket_d.send_json(help_json)
            print(f"\nClient sending to Microservice D: {help_json}")

            microservice_d_help = socket_d.recv_json()
            print(f"Client receiving from Microservice D: {microservice_d_help}\n")

            print(f"{microservice_d_help['help_max']}")
            print(f"{microservice_d_help['help_tp']}")
            print(f"{microservice_d_help['help_reps']}")
            print(f"{microservice_d_help['help_convert']}")
            print(f"{microservice_d_help['help_help']}")
            print(f"{microservice_d_help['help_quit']}")

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

if __name__ == "__main__":
    main()
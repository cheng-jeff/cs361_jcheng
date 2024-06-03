# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 03June2024 @ 11:59 PM PST.
# Description: Microservice C.

import zmq
import json
import time

def get_help_max() -> str:
    """
    Function to return description for the 'Max' command.
    """

    return f"The 'Max' command will allow the user to enter their one rep max in lbs. The user's initial max is set to 'None'. Once the user inputs a one rep max, the command prompt will confirm if this is the user's one rep max.\n\tIf the user types 'Y' or 'Yes', then their new max will be set.\n\tIf the user types 'N' or 'No', their one rep max will remain unchanged.\n\tIf the user presses the Enter key, their one rep max will be cleared back to 'None'.\n"
    # print(f"\n\tIf the user types 'Y' or 'Yes', then their new max will be set.")
    # print(f"\n\tIf the user types 'N' or 'No', their one rep max will remain unchanged.")
    # print(f"\n\tIf the user presses the Enter key, their one rep max will be cleared back to 'None'.\n")

def get_help_tp() -> str:
    """
    Function to return description for the 'TP' command.
    """


    return f"The 'TP' command will determine what the training weights for each respective training percentage from 0% to 100% in intervals of 5%. This command will print out each training percentage and associated training weight.\n\tThis command will only work if there is a one rep max inputted from the user.\n"

def get_help_reps() -> str:
    """
    Function to return description for the 'Reps' command.
    """

    return f"The 'Reps' command will determine what the suggested repetition range for each respective training percentage from 0% to 100% in intervals of 5%. This command will print out each training percentage and suggested repetition range.\n\tThis command will only work if there is a one rep max inputted from the user.\n"

def get_help_convert() -> str:
    """
    Function to return description for the 'Reps' command.
    """

    return f"The 'Convert' command will convert your current one rep max between imperial and metric units. For example, if your current one rep max is in lbs the 'Convert' command will convert from lbs to kgs.\n\tThis command will only work if there is a one rep max inputted from the user.\n"

def get_help_help() -> str:
    """
    Function to return description for the 'Help' command.
    """

    return f"The 'Help' command provides detailed descriptions of each command listed from the main prompt. Please read each description carefully.\n"

def get_help_quit() -> str:
    """
    Function to return description for the 'Help' command.
    """

    return f"The 'Q' or 'Quit' command allows the user to exit the program. It will provide a subsequent prompt asking if the user is sure they want to exit the program.\n"

def check_help_msg_valid(client_json: object) -> bool:
    """Check the client JSON object to see if the 'correct' attribute exists."""
    if "help_msg_valid" in client_json:
        if client_json["help_msg_valid"] == True:
            return True
        else:
            return False
    else:
        return False

def help_main() -> None:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:9999")

    while True:
        client_json = socket.recv_json()
        print(f"Microservice D receiving from client: {client_json}.")
        client_json_valid = check_help_msg_valid(client_json)

        server_json = {}


        if client_json_valid:
            server_json["help_max"] = get_help_max()
            server_json["help_tp"] = get_help_tp()
            server_json["help_reps"] = get_help_reps()
            server_json["help_convert"] = get_help_convert()
            server_json["help_help"] = get_help_help()
            server_json["help_quit"] = get_help_quit()

        socket.send_json(server_json)
        print(f"Microservice D sending to client: {server_json}")

if __name__ == "__main__":
    help_main()
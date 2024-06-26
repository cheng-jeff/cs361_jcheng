# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 20MAY2024 @ 11:59 PM PST. Using grace days, new due date is 22MAY2024 @ 11:59 PM PST.
# Description: Congratulations message microservice program.

# Sources:
# 1. https://zeromq.org/get-started/
# 2. https://pyzmq.readthedocs.io/en/latest/api/zmq.html
# 3. https://canvas.oregonstate.edu/courses/1806257/pages/exploration-file-handling-pickling-json?module_item_id=19702215

import time
import zmq
import json
import random

def congrats_trivia():
    """Function to output congratulatory messages for a Trivia client type."""

    # Get a random number and create dictionaries to hold five (5) different congratulatory messages for correct
    # answers for a trivia game.
    num = str(random.randint(0,4))
    congrats_trivia_msg = {"0" : "Good job! You got the right answer!",
                       "1" : "Congratulations on getting the right answer!",
                       "2" : "You are correct! Keep it up!",
                       "3" : "Nice job! You got the correct answer!",
                       "4" : "Congrats! You got it right!"
                       }

    # Return random congratulatory message.
    return congrats_trivia_msg[num]

def congrats_general():
    """Function to output a congratulatory message for general (workouts/expense) client types."""

    # Get a random number and create dictionaries to hold five (5) different congratulatory messages/affirmations.
    num = str(random.randint(0,4))
    congrats_general_msg = {"0" : "Keep up the good work!",
                       "1" : "Nice job! Keep working hard!",
                       "2" : "You're doing a great job!",
                       "3" : "You're crushing it! Keep it up!",
                       "4" : "Good job! You'll get to where you want to be soon enough!"
                       }

    # Return congratulatory message/affirmation.
    return congrats_general_msg[num]

def check_client_type(client_json: object) -> str:
    """Check to see if the 'client_type' attribute is apart of the client JSON object."""
    if "client_type" in client_json:
        return client_json["client_type"]
    elif "client_type" not in client_json:
        return None

def check_trivia_correct(client_json: object) -> bool:
    """Check the client JSON object to see if the 'correct' attribute exists."""
    if "correct" in client_json:
        if client_json["correct"] == True:
            return True
        else:
            return False
    else:
        return False

def print_command_complete() -> None:
    """
    Print message for when a command is finished processing. Leveraged from Professor Letaw's
    example video https://canvas.oregonstate.edu/courses/1958534/assignments/9583963?module_item_id=24164834
    """
    print(f"\nPlease wait about one (1) second for the communication to complete.")
    waiting = ""

    for i in range(3):
        time.sleep(0.33)
        waiting += "."
        print(f"{waiting}")

    print(f"\n")

def congrats_main():
    """
    Main function
    """

    # Create a socket on the server side and bind to "tcp://*:5555"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Loop while true
    while True:

        # Receive client JSON object.
        client_json = socket.recv_json()
        print(f"Server receiving from client: {client_json}")

        # Try-Except-Else to see if the client_type attribute is not None. If it is None, send back a JSON object
        # with an error message. Otherwise, check to see which client type the user is running and then send back
        # a JSON object with the correct congratulatory message.
        try:
            client_type = check_client_type(client_json)
        except AttributeError:
            error_json = {"Error Message" : "Client type was not defined. Please define client type."
                          }
            print(f"Sending {error_json}")
            socket.send_json(error_json)
        else:
            if client_type.lower() == "trivia":
                trivia_correct = check_trivia_correct(client_json)
                if trivia_correct == True:
                    congrats_msg = congrats_trivia()
                else:
                    congrats_msg = "You did not get the question correct. You do not get a congratulatory message."
            elif client_type.lower() == "workout" or client_type.lower() == "expenses":
                congrats_msg = congrats_general()
            server_json = {
                "client_type" : client_type,
                "message" : congrats_msg
        }
            print(f"Server sending to client: {server_json}")
            socket.send_json(server_json)

            print_command_complete()

if __name__ == "__main__":
    congrats_main()
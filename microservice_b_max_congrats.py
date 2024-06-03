# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 03June2024 @ 11:59 PM PST.
# Description: Microservice B.

# Sources:
# 1. https://zeromq.org/get-started/
# 2. https://pyzmq.readthedocs.io/en/latest/api/zmq.html
# 3. https://canvas.oregonstate.edu/courses/1806257/pages/exploration-file-handling-pickling-json?module_item_id=19702215

import time
import zmq
import json
import random

def check_valid_max(client_json: object) -> bool:
    """Check to see if the one rep max passed in is valid."""
    if "user_max" in client_json:
        return True
    else:
        return False

def check_unit_type(client_json: object) -> str:
    """Check to see if the 'client_type' attribute is apart of the client JSON object."""
    if "unit" in client_json:
        return client_json["unit"]
    elif "client_type" not in client_json:
        return None

def congrats_max():
    """Function to output a congratulatory message for general (workouts/expense) client types."""

    # Get a random number and create dictionaries to hold five (5) different congratulatory messages/affirmations.
    num = str(random.randint(0,4))
    congrats_max_msg = {"0" : "Keep up the good work!",
                       "1" : "Nice job! Keep working hard!",
                       "2" : "You're doing a great job!",
                       "3" : "You're crushing it! Keep it up!",
                       "4" : "Good job! You'll get to where you want to be soon enough!"
                       }

    # Return congratulatory message/affirmation.
    return congrats_max_msg[num]

def print_max(user_max: int, units: str) -> None:
    if isinstance(user_max, int) and isinstance(units, str):
        return f"Your one rep max is {user_max}!"
    else:
        return f""

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

def max_congrats_main():
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
        server_json = {}

        try:
            unit = check_unit_type(client_json)

            if unit.lower() == "lbs":
                user_unit = "lbs"
            elif unit.lower() == "kgs":
                user_unit = "kgs"
        except AttributeError:
            error_json = {"Error Message" : "Unit was not defined. Please define what unit you will be using."
                          }
            print(f"Sending {error_json}")
            socket.send_json(error_json)
        else:
            server_json["units"] = user_unit

        try:
            one_rep_max_valid = check_valid_max(client_json)

            if one_rep_max_valid:
                user_max = client_json["user_max"]
            else:
                user_max = "Your one rep max has not been defined. Please define your one rep max. "
        except AttributeError:
            error_json = {"Error Message" : "Unit was not defined. Please define what unit you will be using."
                          }
            socket.send_json(error_json)
            print(f"Sending {error_json}")
        except TypeError:
            error_json = {"Error Message" : "Unit was not defined. Please define what unit you will be using."
                          }
            socket.send_json(error_json)
            print(f"Sending {error_json}")
        else:
            server_json["user_max"] = print_max(user_max, user_unit)


        congrats_msg = congrats_max()

        server_json["message"] = congrats_msg



        socket.send_json(server_json)
        print(f"Microservice B sending to client: {server_json}.")

        print_command_complete()

if __name__ == "__main__":
    max_congrats_main()
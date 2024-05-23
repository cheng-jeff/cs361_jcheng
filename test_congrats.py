# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 06MAY2024 @ 11:59 PM PST. Using grace days, new due date is 08MAY2024 @ 11:59 PM PST.
# Description: Congratulations message microservice testing program.

# Sources:
# 1. https://zeromq.org/get-started/
# 2. https://pyzmq.readthedocs.io/en/latest/api/zmq.html
# 3. https://canvas.oregonstate.edu/courses/1806257/pages/exploration-file-handling-pickling-json?module_item_id=19702215

import time
import zmq
import json

def test_main():
    """
    Client main function for testing program.
    """

    # Create a socket on the client side and connect to "tcp://*:5555"
    context = zmq.Context()
    print(f"Establishing connection...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print(f"Connection established.")

    # Get user input to which client they will be running.
    user_inp = input("What client type will you be using: ")
    if user_inp.lower() == "trivia":
        valid = True
    elif user_inp.lower() == "workout" or user_inp.lower() == "expense":
        valid = True
    else:
        valid = False

    # Loop until a valid client type is input.
    while valid is False:
        user_inp = input("What client type will you be using: ")
        if user_inp.lower() == "trivia":
            valid = True
        elif user_inp.lower() == "workout" or user_inp.lower() == "expense":
            valid = True
        else:
            valid = False

    # Create JSON Object to send to Server/Microservice
    client_json = {
        "client_type" : user_inp,
        "correct" : False
    }

    # Send JSON object from client to microservice.
    socket.send_json(client_json)
    print(f"Client sending to server: {client_json}")

    # Receive a JSON object back from the microservice.
    server_json = socket.recv_json()
    print(f"Receiving: {server_json}")

if __name__ == "__main__":
    test_main()
# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 06MAY2024 @ 11:59 PM PST. Using grace days, new due date is 08MAY2024 @ 11:59 PM PST.
# Description: Congratulations message microservice program.

import time
import zmq
import json

def test_main():
    """
    Client main function
    """

    # Create a socket on the client side and connect to "tcp://*:5555"
    context = zmq.Context()
    print(f"Establishing connection...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print(f"Connection established.")

    client_json = {
        "client_type" : "trivia",
        "correct" : False
    }

    socket.send_json(client_json)

    print(f"Sending: {client_json}")

    server_json = socket.recv_json()
    print(f"Receiving: {server_json}")

if __name__ == "__main__":
    test_main()
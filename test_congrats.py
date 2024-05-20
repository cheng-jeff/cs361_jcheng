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
    print(f"Connecting to CS361 Server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    client_pack = {
        ""
    }

if __name__ == "__main__":
    test_main()
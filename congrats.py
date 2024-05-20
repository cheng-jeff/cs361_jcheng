# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 06MAY2024 @ 11:59 PM PST. Using grace days, new due date is 08MAY2024 @ 11:59 PM PST.
# Description: Congratulations message microservice program.

import time
import zmq
import json

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

        # Read in message from client through the socket created and store in message.
        message = socket.recv()

        # Get the time in seconds since the epoch of the user's PC then use .gmtime method to a time.struct_time object.
        # Then format using .strftime method passing in the time.struct_time object and print the received message with
        # a timestamp.
        curr_time = time.time() - 14400
        curr_time_secs = time.gmtime(curr_time)
        formatted_time = time.strftime("%a, %d %b %Y %H:%M:%S", curr_time_secs)
        print(f"Received message from client side: {message} at {formatted_time}")

        time.sleep(1)

        socket.send(b"A message from CS361.")

if __name__ == "__main__":
    congrats_main()
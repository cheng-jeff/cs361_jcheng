# Name: Jeffrey Cheng
# OSU Email: chengjef@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Due Date: 03June2024 @ 11:59 PM PST.
# Description: Microservice C.

import zmq
import json
import time

def check_max_valid(client_json: object) -> bool:
    """Check the client JSON object to see if the 'correct' attribute exists."""
    if "user_max" in client_json:
        if isinstance(client_json['user_max'], int) == True or isinstance(client_json['user_max'], float) == True:
            return True
        else:
            return False
    else:
        return False

def create_tp(user_max) -> dict:
    training_percentages = {}

    for i in range(0, 101, 5):
        tp = str(i) + "%"
        training_percentages[tp] = user_max * (i / 100)

    return training_percentages


def create_reps() -> dict:
    training_reps = {}

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

    return training_reps

def tp_rep_main() -> None:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:8888")

    while True:
        client_json = socket.recv_json()
        print(f"Microservice D receiving from client: {client_json}.")
        client_json_valid = check_max_valid(client_json)
        msc_tp_json = {}
        msc_reps_json = {}

        if client_json_valid:
            if client_json["command"].lower() == "tp":
                msc_tp_json["tp"] = create_tp(client_json["user_max"])

                socket.send_json(msc_tp_json)
                print(f"Microservice C sending to client: {msc_tp_json}")
            elif client_json["command"].lower() == "reps":
                msc_reps_json["reps"] = create_reps()

                socket.send_json(msc_reps_json)
                print(f"Microservice C sending to client: {msc_reps_json}")
        else:
            continue


if __name__ == "__main__":
    tp_rep_main()
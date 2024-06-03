import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:7777")

def lbs_to_kgs(lb):
    return lb * 0.45359237

def kgs_to_lbs(kg):
    return kg * 2.2

def check_valid(data):
    error = None
    if "convert_type" not in data:
        error = "Convert type not provided. Please indicate whether to convert values to 'lbs' or 'kgs'."
    elif "convert_type" in data:
        if data["convert_type"] != "lbs" and data["convert_type"] != "kgs":
            error = "Invalid convert type. Input 'lbs' to convert values to pounds or 'kgs' to convert to kilograms."
    return error

while True:
    output_json = {}
    data = socket.recv_json()
    try:
        print("Received JSON data:", data)
        convert_list = []

        valid_data = check_valid(data)

        if valid_data is None:
            if isinstance(data["values"], list):
                for value in data["values"]:
                    new_val = float(value)
                    if data["convert_type"] == "lbs":
                        convert_list.append(kgs_to_lbs(new_val))
                    elif data["convert_type"] == "kgs":
                        convert_list.append(lbs_to_kgs(new_val))

                socket.send_json({
                    "converted_type": data["convert_type"],
                    "converted_values": convert_list
                })
            else:
                convert_val = float(data['values'])
                converted_val = None
                if data["convert_type"] == "lbs":
                    converted_val = kgs_to_lbs(convert_val)
                elif data["convert_type"] == "kgs":
                    converted_val = lbs_to_kgs(convert_val)

                socket.send_json({
                    "converted_type": data["convert_type"],
                    "converted_values": converted_val
                })
        else:
            print(valid_data)
    except json.JSONDecodeError as e:
        print("Received a message, but it was not valid JSON:", data)
        print("Error:", e)
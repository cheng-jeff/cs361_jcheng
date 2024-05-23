#CS361 Microservices - ReadMe

This readme file is for all microservices to be established.

## Microservice A - Congratulatory Messenger


This microservice will output a congralutatory message depending on the "client_type" attribute (i.e. Trivia, Workout, or Expenses). If the client type is "Trivia", it will only output a congratulatory if the JSON object has the "correct" attribute set to True. This microservice uses the ZeroMQ communication pipeline.

## Requests

To make a request to the congrats.py microservice program, the client end will need to pass in a JSON object using the ZeroMQ communication pipeline. The client end will need to create a JSON object with two attributes, "client_type" and "correct". The "client_type" attribute may be one of three options: "Trivia", "Workout", or "Expenses"; the "correct" attribute, only relevant to the "Trivia" client type, needs to be a boolean value: True or False.

**Example JSON Object**

```
test_client_json = {
  "client_type" : "Trivia",
  "correct" : True
}
```

The following example code, which can be seen in _test_congrats.py_, can be leveraged for new users to request and receive data from the **Congratulatory Messenger** microservice:

```
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

    # Waiting code...
    waiting = ""

    for i in range(3):
        time.sleep(0.33)
        waiting += "."
        print(f"{waiting}")

    socket.connect("tcp://localhost:5555")
    print(f"Connection established.")

    # Initialize trivia correct
    trivia_correct = False

    # Get user input to which client they will be running.
    user_inp = input("What client type will you be using: ")
    if user_inp.lower() == "trivia":
        valid = True
    elif user_inp.lower() == "workout" or user_inp.lower() == "expense":
        valid = True
        trivia_correct = True
    else:
        valid = False

    # Loop until a valid client type is input.
    while valid is False:
        user_inp = input("What client type will you be using: ")
        if user_inp.lower() == "trivia":
            valid = True
        elif user_inp.lower() == "workout" or user_inp.lower() == "expenses":
            valid = True
            trivia_correct = True
        else:
            valid = False

    if user_inp.lower() == "trivia":
        user_correct = input("Did the user get the question correct? (Y/N) ")
        if user_correct.lower() == "y":
            trivia_correct = True
        elif user_correct.lower() == "n":
            trivia_correct = False
        else:
            user_correct = None
            while user_correct is None:
                user_correct = input("Did the user get the question correct? (Y/N) ")
                if user_correct.lower() == "y":
                    trivia_correct = True
                elif user_correct.lower() == "n":
                    trivia_correct = False
                else:
                    user_correct = None


    # Create JSON Object to send to Server/Microservice
    client_json = {
        "client_type" : user_inp,
        "correct" : trivia_correct
    }

    # Send JSON object from client to microservice.
    socket.send_json(client_json)
    print(f"Client sending to server: {client_json}")

    # Receive a JSON object back from the microservice.
    server_json = socket.recv_json()
    print(f"Receiving: {server_json}")

if __name__ == "__main__":
    test_main()
```

## UML Sequence Diagram
![image](https://github.com/cheng-jeff/cs361_jcheng/assets/59590715/998125f4-ee3b-428f-b6fd-f3965b4fb333)

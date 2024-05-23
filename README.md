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

```

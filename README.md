# TCP Server and Client Examples

This repository contains two Python scripts for creating a TCP server and client, facilitating network communication. The client send sensor data to the server.

## `server.py`

### Overview

The `server.py` script establishes a TCP server that listens on port 8889, awaiting incoming connections. When a connection is established, the server spawns a separate thread to handle the client. Key components of the server script include:

- Creation of a socket using `socket.socket()` with the `AF_INET` address family and `SOCK_STREAM` socket type.
- Binding the server socket to address "0.0.0.0" / localhost and port 8889 to listen for incoming connections.
- Listening for up to 5 pending connections.
- Accepting client connections and initiating a separate thread for each client, invoking the `handle_client` function.

The `handle_client` function manages the communication with individual clients by sending a "pong" response to received data, displaying the received data if available, and breaking the loop when the connection is closed.

### How to Run

To run the server, execute the script. It will listen on port 8889, awaiting incoming client connections.

## `client.py`

### Overview

The `client.py` script functions as a TCP client for communicating with a remote server. It includes the following features:

- Creation of a socket using `socket.socket()` with the `AF_INET` address family and `SOCK_STREAM` socket type.
- Connection to a remote server with IP address "127.0.0.1" / localhost and port 8889.
- Setting a timeout of 10 seconds for socket operations to handle potential delays.
- Sending an initial "ping" message to the server and recording the time taken to establish the connection.
- Running a loop to continually send messages containing data generated by the `generate_data_sensor` function, with a 1-second delay between messages.
- Attempting to send messages, recording the round-trip time, and displaying the sent and received data.
- Handling potential exceptions related to packet loss or timeouts.

### How to Run

To run the client, execute the script. It will connect to the server at IP "127.0.0.1" on port 8889 and exchange messages as described.

---

### Image

![alt text](https://github.com/clem-mont-inha/MidTermsCN/blob/main/image.png?raw=true)
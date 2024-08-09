How It Works:

Server Side:

The server listens on a specified IP address and port (0.0.0.0 and 12345 in this case).
It waits for a client to connect.
Once a connection is established, the server can send and receive messages in a loop.
If the user or the client sends "exit", the connection closes.

Client Side:

The client connects to the server's IP address and port (127.0.0.1 and 12345 in this case, where 127.0.0.1 refers to localhost).
The client sends and receives messages in a loop.
Similarly, the connection closes when "exit" is sent.

Running the Scripts:

Start the server script first.
Then run the client script.
The client will connect to the server, and you can start exchanging messages.
Replace 127.0.0.1 with the server's IP address if the client is on a different machine.

Additional Notes:

Network Permissions: Ensure that your network or firewall settings allow communication through the specified port.
Security: This is a basic example. For production, consider adding encryption, authentication, and error handling.

import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a public host and a port
    server_socket.bind(('0.0.0.0', 12345))
    
    # Become a server socket, with a maximum of 5 connections waiting
    server_socket.listen(5)
    print("Server is listening on port 12345...")

    # Accept connections from outside
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Client has exited the chat.")
            break
        print(f"Client: {message}")

        # Send message to client
        response = input("You: ")
        client_socket.send(response.encode('utf-8'))
        if response.lower() == 'exit':
            break

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

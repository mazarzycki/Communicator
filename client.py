import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server on local computer (use server's IP address)
    client_socket.connect(('127.0.0.1', 12345))
    
    print("Connected to the server. Type 'exit' to leave the chat.")

    while True:
        # Send message to server
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            break

        # Receive message from server
        response = client_socket.recv(1024).decode('utf-8')
        if response.lower() == 'exit':
            print("Server has exited the chat.")
            break
        print(f"Server: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()

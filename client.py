import socket
import threading

print("  Lightweight KCR messanger")
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\nAnoymous: {message}")  # Print the received message
            else:
                break
        except:
            break

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Start a thread to receive messages
thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

# Main loop for sending messages
while True:
    message = input("")  # Get input from the user
    if message:
        client.send(message.encode('utf-8'))  # Send the message to the server

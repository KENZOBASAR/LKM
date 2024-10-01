import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Anoymous: {message}")
                # Broadcast the message to all clients
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    # Remove client and close connection
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))  # Send message to all other clients
            except:
                client.close()
                clients.remove(client)

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)
clients = []

print("Server is listening...")

while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    clients.append(client_socket)

    # Start a thread for the new client
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()

import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = [] # List to keep track of active connections
nicknames = [] # List to track names

def broadcast(message):
    """Sends a message to every client connected to the server."""
    for client in clients:
        client.send(message)

def handle(client):
    """Handles the continuous communication with a single client."""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove and close clients if they disconnect
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    """Accepts new connections and starts a thread for each."""
    print("Server is running and listening...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask the client for a nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        # Start a thread for this specific client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
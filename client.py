import socket

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the server. Type your message!")

while True:
    message = input("")
    if message.lower() == 'quit':
        break
    client.send(message.encode('utf-8'))

client.close()
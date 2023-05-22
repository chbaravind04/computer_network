#SERVER
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (queue up to 5 connections)
server_socket.listen(5)

print('Server is listening on {}:{}'.format(*server_address))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Received connection from {}:{}'.format(*client_address))

# Send data to the client
message = 'Hello, client!'
client_socket.send(message.encode())

# Receive data from the client
data = client_socket.recv(1024)
print('Received data: {}'.format(data.decode()))

# Close the client connection
client_socket.close()

# Close the server socket
server_socket.close()


#---------------------------------------------------------------------------------------
#CLIENT
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)
print('Connected to {}:{}'.format(*server_address))

# Receive data from the server
data = client_socket.recv(1024)
print('Received data: {}'.format(data.decode()))

# Send data to the server
message = 'Hello, server!'
client_socket.send(message.encode())

# Close the client socket
client_socket.close()

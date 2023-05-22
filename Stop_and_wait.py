#--------------------------------------SERVER------------------------------------------
import socket

def start_server():
    host = '127.0.0.1'  # Server IP address
    port = 12345  # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started. Waiting for client connection...")

    while True:
        data, address = server_socket.recvfrom(1024)
        message = data.decode()
        print("Received message from client:", message)

        # Simulating random packet loss
        if message.startswith("ACK"):
            if random.random() < 0.3:
                print("ACK lost. Waiting for retransmission...")
                continue

        response = "ACK" + message  # Echo message with ACK prefix
        server_socket.sendto(response.encode(), address)
        print("Sent ACK to client:", response)

    server_socket.close()

start_server()


#---------------------------------------------------------CLIENT----------------------------------------------------------

import socket
import random

def start_client():
    host = '127.0.0.1'  # Server IP address
    port = 12345  # Port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Enter message to send: ")
    client_socket.sendto(message.encode(), (host, port))
    print("Sent message to server:", message)

    while True:
        data, address = client_socket.recvfrom(1024)
        response = data.decode()
        print("Received ACK from server:", response)

        # Simulating random packet loss
        if random.random() < 0.3:
            print("ACK lost. Waiting for retransmission...")
            continue

        if response[3:] == message:  # Check if ACK matches the original message
            break
        else:
            client_socket.sendto(message.encode(), (host, port))
            print("Sent message to server:", message)

    client_socket.close()

start_client()

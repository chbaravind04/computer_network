#---------------------------SERVER----------------------------
import socket

def transfer_file(conn, filename):
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            conn.sendall(data)
            print("File transfer complete.")
    except IOError:
        print("Error reading file.")

def start_server():
    host = '127.0.0.1'  # Server IP address
    port = 12345  # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server started. Waiting for client connection...")

    conn, addr = server_socket.accept()
    print("Client connected:", addr)

    filename = conn.recv(1024).decode()
    print("Receiving file:", filename)

    transfer_file(conn, filename)

    conn.close()
    server_socket.close()

start_server()


#----------------------------------------------CLIENT-------------------------------------
import socket

def receive_file(sock, filename):
    try:
        with open(filename, 'wb') as file:
            print("Receiving file...")
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                file.write(data)
            print("File received.")
    except IOError:
        print("Error writing file.")

def start_client():
    host = '127.0.0.1'  # Server IP address
    port = 12345  # Port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    filename = input("Enter the file name to request: ")
    client_socket.send(filename.encode())

    receive_file(client_socket, filename)

    client_socket.close()

start_client()

#-----------------------------SERVER-------------------------------------
import socket

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to a specific IP address and port
    server_address = ('', 12345)
    server_socket.bind(server_address)

    print('Server is running. Waiting for incoming fragments...')

    while True:
        # Receive the fragments and address from the client
        fragments, client_address = server_socket.recvfrom(4096)
        
        # Process the received fragments
        # In a real implementation, you would need to reconstruct the original data from the fragments
        # For simplicity, we'll just print the fragments here
        print('Received fragments:', fragments.decode())
        
        # Acknowledge the receipt of the fragments
        server_socket.sendto(b'ACK', client_address)

if __name__ == '__main__':
    main()
#-----------------------------------------------------------CLIENT---------------------------------------------------------------------
import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set the maximum buffer size for sending data
    buffer_size = 1024
    
    # Set the server address and port
    server_address = ('localhost', 12345)

    # Create a large data string to be sent
    data = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' * 1000
    
    # Break the data into fragments based on the buffer size
    fragments = [data[i:i+buffer_size] for i in range(0, len(data), buffer_size)]

    # Send each fragment to the server
    for fragment in fragments:
        client_socket.sendto(fragment.encode(), server_address)
        
        # Wait for the acknowledgement from the server
        ack, _ = client_socket.recvfrom(4096)
        print('Received ACK:', ack.decode())

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    main()

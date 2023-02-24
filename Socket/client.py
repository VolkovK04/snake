import socket 

HOST = input("Server host: ")
PORT = int(input("Server port: "))

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

while True:    
    data = input("Type the message to send: ")    
    data_bytes = data.encode()  # (str to bytes)    
    conn.sendall(data_bytes)  # Send    
    data_bytes = conn.recv(1024)  # Receive    
    data = data_bytes.decode()  # (bytes to str)    
    print("Received:", data)
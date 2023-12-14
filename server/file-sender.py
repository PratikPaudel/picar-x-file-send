from socket import *
import time
import sys
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 29985))
sock.listen()
buffer_size = 1024
print("Server is listening on port 25575")
try:
    while True:
        try:
            connection, addr = sock.accept()
            print(f"Connection established with {addr}")

            connection.send("got it".encode())

            filename = sys.argv[1] #getting the filename from the main server file. 
            print(filename)
            with open(filename, 'rb') as file:
                image_data = file.read()

            connection.sendall(image_data)
            print("Image sent successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.shutdown(SHUT_RDWR)
            connection.close()
except KeyboardInterrupt:
    print("Send picture server is shutting down.")
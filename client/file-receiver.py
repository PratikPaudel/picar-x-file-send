from socket import *
import time

def receive_message():
    yourSock = socket(AF_INET, SOCK_STREAM)
    save_as = 'tcp_received_image.png'
    buffer_size = 1024
    
    try:
        yourSock.connect(('10.50.18.239', 29985))
        response = yourSock.recv(2048)
        response = response.decode()

        if response == "got it":
            with open(save_as, 'wb') as file:
                while True:
                    data = yourSock.recv(buffer_size)
                    if not data:
                        break
                    file.write(data)
            print("Image received successfully")
        else:
            print("Failed to confirm receipt")
    except Exception as e:
        print(f"An error occurred: {e}")

receive_message()
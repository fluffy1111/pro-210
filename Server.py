import socket
from  threading import Thread
import time
import os


IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}



def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    SERVER.bind((IP_ADDRESS,PORT))

    print("\t\t\t\tSERVER IS WAIRING FOR INCOMMING CONNECTION...")
    print("\n")

    acceptConnections()
setup()

setup_thread = Thread(target=setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name]= {
                "client"         : client,
                "address"        : addr,
                "connected_with" : "",
                "file_name"      : "",
                "file_size"      : 4096
            }

        print(f"Connection establish with {client_name} : {addr}")

        thread = Thread(target= handleClient, args=(client,client_name,))
        thread.start()

    while True:
        client,addr = SERVER.accept()
        print(client.adder)
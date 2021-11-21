from logging import ERROR, error
from os import terminal_size
import socket
import threading
import json


HEADER = 1024*4
PORT = 5544
# SERVER = "192.168.1.104"
SERVER = "localhost" # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def validate_json(msg):
    json_msg = json.loads(msg)
    timestamp = []
    temperature = []
    sensorId = []
    try:
        for i in range(len(json_msg)):
            timestamp.append(json_msg[i]["timestamp"])
            temperature.append(json_msg[i]["payload"]["temperature"])
            sensorId.append(json_msg[i]["payload"]["sensorId"])

    except Exception as e:
        print(f"exception occurded: {e}")


def handle_client(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")

    msg = conn.recv(HEADER)
    print(msg)
    msg = json.loads(msg)
    print(msg)
    print(msg[0]["timestamp"])
    connected = True
    """
        while connected:
        if msg_lenth:
            msg_lenth = int(msg_lenth)
            msg = conn.recv(msg_lenth).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
        """
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING]server is starting...")
start()


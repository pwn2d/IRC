import socket
import threading
import colorama 
import sys

colorama.init()

global server_port

connections = []
messages = []

#server ip 198.245.62.27

server = "127.0.0.1"
server_port = 4209

server_socket = socket.socket()
def handle_co(con):
    global data
    data = str(con.recv(1024), "utf-8")
    messages.append(data)
    print(data)
    for connection in connections:
        connection.send(str.encode(data))

def accept_connection():
    global server_socket
    server_socket.bind((server, server_port))
    server_socket.listen(5)
    accept(server_socket)

def accept(socket):
    while True:
        conn, address = socket.accept()
        handle_conns(conn, address)
        accept(socket)
                
def handle_conns(conn, address):
    x = server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    connections.append(conn)
    data = str(conn.recv(1024), "utf-8")
    if data != "":
        print(data, "Message Received from " + str(address[0]) + ":" + str(address[1]))
        if len(connections) >= int(sys.argv[1]):
            for connection in connections:
                connection.send(str.encode("Connected To IRC"))
        if len(connections) > 0:
            for connection in connections:
                connection.send(str.encode("\nNumber of Connections : " + str(len(connections)) + "/" + sys.argv[1]))

        if len(connections) == int(sys.argv[1]):
            print("Everyone Successfully Joined")


            while True:
                for connection in connections:
                    thread = threading.Thread(target=handle_co, args=(connection,))
                    thread.start() 

try:
    accept_connection()
except:
    pass
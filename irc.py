import socket
import colorama
from colorama import Fore
from datetime import datetime
import threading
import os
import sys

server = sys.argv[1]
#server = "127.0.0.1"
server_port = 4209

colorama.init()

s = socket.socket()


def connect_to_server():
    global name
    name = input("Enter Name : ")
    s.connect((server, server_port))
    print(f"{Fore.GREEN}Connecting To Server{Fore.RESET}")
    s.send(str.encode(Fore.RESET + name))
    thread1 = threading.Thread(target=send)
    thread2 = threading.Thread(target=recv)
    thread1.start()
    thread2.start()
        

def send():
    while True:
        global x
        x = input("\n")
        if x == "!clear":
            os.system("cls")
        if x == "!exit":
            exit()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        full_msg = f"\033[1A{Fore.LIGHTBLACK_EX}[{Fore.GREEN}{current_time}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}{name} {Fore.LIGHTBLACK_EX}-{Fore.WHITE} {x}"
        print(f"\033[1A{Fore.LIGHTBLACK_EX}[{Fore.GREEN}{current_time}{Fore.LIGHTBLACK_EX}] {Fore.GREEN}{name} {Fore.LIGHTBLACK_EX}-{Fore.WHITE} {x}", end="\r")
        s.send(str.encode(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}{current_time}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}{name} {Fore.LIGHTBLACK_EX}-{Fore.WHITE} {x}"))


def recv():
    while True:
        data = str(s.recv(1024), "utf-8")
        if data != "":
            if data[31:].startswith(name):
                pass
            else:
                print(data)
            
connect_to_server()

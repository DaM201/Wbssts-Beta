import socket, threading, Resource.message as message, time
from colorama import *
mn = True
def start_clientNoColor(host,port):
    def receive_messages(client_socket):
        while True:
            data = client_socket.recv(1024)
        
            if not data:
                break

            message_receive = data.decode('utf-8')
            message.NoColorMessage.Information(f"NEW MESSAGE (from server or client) >{Fore.RESET} {message_receive}")
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            message.NoColorMessage.Information(f"Successfully connected to server!{Fore.RESET}")
            welcome_message = client_socket.recv(1024).decode('utf-8')
            
            message.NoColorMessage.Information(f"NEW MESSAGE (from server or client) >{Fore.RESET} {welcome_message}")

            receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
            receive_thread.start()
            time.sleep(1)
        except socket.error as e:
            mn = False
            message.NoColorMessage.Error(f"Disconnected from server... Output: {e}")
            time.sleep(1)




def start_client(host,port):
    def receive_messages(client_socket):
        while True:
            data = client_socket.recv(1024)
        
            if not data:
                break

            message_receive = data.decode('utf-8')
            message.Message.Information(f"{Fore.YELLOW}NEW MESSAGE (from server or client) >{Fore.RESET} {message_receive}")
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            message.Message.Information(f"{Fore.GREEN}Successfully connected to server!{Fore.RESET}")
            welcome_message = client_socket.recv(1024).decode('utf-8')
            
            message.Message.Information(f"{Fore.YELLOW}NEW MESSAGE (from server or client) >{Fore.RESET} {welcome_message}")

            receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
            receive_thread.start()
            time.sleep(1)
        except socket.error as e:
            mn = False
            message.Message.Error(f"Disconnected from server... Output: {e}")
            time.sleep(1)

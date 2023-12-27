import socket

def start_client(server_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, 1))
        server_address, server_port = client_socket.getpeername()
        print(f"Připojen k serveru na adrese {server_address}:{server_port}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Od serveru: {data.decode('utf-8')}")

    except socket.error as e:
        print(f"Nepodařilo se připojit k serveru. Chyba: {e}")

    finally:
        client_socket.close()

server_ip = '192.168.0.168'

# Spuštění klienta
start_client(server_ip)

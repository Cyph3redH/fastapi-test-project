import socket
import multiprocessing

HOST = "127.0.0.1"
PORT = 12345

def handle_client(client_socket, client_address):
    print(f"Подключение от {client_address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Получены данные от {client_address}: {data.decode()}")
        client_socket.sendall(data)
    
    client_socket.close()
    print(f"Клиент {client_address} отключился")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущен на {HOST}:{PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            
            process = multiprocessing.Process(
                target=handle_client, 
                args=(client_socket, client_address)
            )
            process.start()
            client_socket.close()  # Важно закрыть в родительском процессе
            
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        server_socket.close()

if __name__ == "__main__":
    main()
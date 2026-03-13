import socket   # Модуль для работы с сетевыми соединениями

HOST = "127.0.0.1"  # Локальный адрес (localhost)
PORT = 12345        # Порт для прослушивания

# Создаем серверный сокет (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind((HOST, PORT))

# Переводим сервер в режим прослушивания
server_socket.listen()

print(f"Сервер запущен на {HOST}:{PORT}... Ожидание подключения.")

while True:
    #   Принимаем входящее соединение
    client_socket, client_address = server_socket.accept()
    
    print(f"Подключение от {client_address}")

    while True:
        # Получаем данные от клиента
        data = client_socket.recv(1024)

        if not data:
            break   # Если данных нет (клиент отключился)

        print(f"Получено: {data.decode()}")

        client_socket.sendall(data)
    
    print(f"Отключение клиента {client_address}")
    client_socket.close()
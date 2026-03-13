import socket   # Модуль для работы с сетевыми соединениями

import threading    # Модуль для многопоточного выполнения

HOST = "127.0.0.1"  # Локальный адрес (localhost)
PORT = 12345        # Порт для прослушивания

# Создаем серверный сокет (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind((HOST, PORT))

# Переводим сервер в режим прослушивания
server_socket.listen()

print(f"Сервер запущен на {HOST}:{PORT}... Ожидание подключения.")

def handle_client(client_socket, client_address):
    """
    Функция обработки подключения клиента.
    Запускается в отдельном потоке для каждого нового клиента.
    """

    print(f"Подключение от {client_address}")   # Выводим информацию о новом подключении
    
    while True:
        data = client_socket.recv(1024)     # Получаем данные от клиента, не более 1024 байт

        if not data:
            break   # Данных нету (клиент отключился)

        print(f"[{client_address}] Получено: {data.decode('utf-8', errors='ignore').strip()}")

        client_socket.sendall(data)     # Отправляем полученные данные обратно клиенту (эхо-ответ)
    
    client_socket.close()       # Закрываем соединение с клиентом

    print(f"Клиент {client_address} отключился")
    
# Основной цикл сервера, ждет подключения клиентов и создает новый поток для каждого из них
while True:
    client_socket, client_address = server_socket.accept()  # Принимаем новое соединение

    # Создаем поток для клиента
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()  # Запускаем поток
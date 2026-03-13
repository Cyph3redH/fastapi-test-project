import asyncio

HOST = "127.0.0.1"
PORT = 12345

# Асинхронная функция обработки клиента

async def handle_client(reader, writer):
    """
    Обрабатывает соединение с клиентом
    Получает данные от клиента и отправляет их обратно (эхо-сервер)
    """
    address = writer.get_extra_info("peername")     # Получаем IP-адрес и порт клиента

    print(f"Подключение от {address}")


    while True:
        data = await reader.read(1024)      # Асинхронно читаем данные от клиента

        if not data:
            break
        
        print(f"[{address}] Получено: {data.decode('utf-8', errors='ignore').strip()}")

        writer.write(data)      # Отправляем данные обратно

        await writer.drain()    # Дожидаемся завершения отправки данных

    print(f"Клиент {address} отключился")

    writer.close()      # Закрываем соединение

    await writer.wait_closed()      # Дожидаемся полного закрытия соединения

# Асинхронная функция для запуска сервера

async def main():
    """
    Создаёт и запускает асинхронный сервер
    """

    server = await asyncio.start_server(handle_client, HOST, PORT)  # Запускаем сервер и привязываем к IP и порту
    
    print(f"Сервер запущен на {HOST}:{PORT}...")


    # Асинхронный контекстный менеджер обеспечивает автоматическое закрытие сервера при завершении работы

    async with server:
        await server.serve_forever()    # Запускаем сервер в бесконечном режиме ожидания клиентов

# Запускаем асинхронный цикл событий
asyncio.run(main())     # Запуск главной асинхронной функции
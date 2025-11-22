#  запустити Redis-сервер
#  pip install redis

import socket
import threading
from typing import Dict
import redis

HOST = "127.0.0.1"   # IP сервера
PORT = 5000          # Порт сервера

# Підключення до Redis
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True,  # повертає str замість bytes
)

# Словник: сокет -> імʼя користувача
clients: Dict[socket.socket, str] = {}
clients_lock = threading.Lock()


def broadcast(message: str, sender_sock: socket.socket | None = None) -> None:
    """Надіслати повідомлення всім підключеним клієнтам (окрім відправника)."""
    with clients_lock:
        dead_sockets = []
        for sock, username in clients.items():
            if sock is sender_sock:
                continue
            try:
                sock.sendall(message.encode("utf-8"))
            except OSError:
                dead_sockets.append(sock)

        # Прибрати «мертві» сокети
        for sock in dead_sockets:
            clients.pop(sock, None)


def handle_client(conn: socket.socket, addr) -> None:
    """Обробка одного клієнта: логін, читання, розсилка повідомлень, статуси."""
    try:
        conn.sendall("Enter your username: ".encode("utf-8"))
        username_data = conn.recv(1024)
        if not username_data:
            conn.close()
            return

        username = username_data.decode("utf-8").strip()
        if not username:
            conn.close()
            return

        # Реєструємо користувача в памʼяті сервера
        with clients_lock:
            clients[conn] = username

        # Статус користувача в Redis
        redis_client.hset(f"user:{username}", mapping={"status": "online"})
        redis_client.sadd("online_users", username)

        join_message = f"{username} joined the chat\n"
        print(f"[INFO] {addr} -> {join_message.strip()}")

        # Зберігаємо повідомлення в Redis
        redis_client.rpush("chat:messages", join_message)

        # Розсилаємо іншим
        broadcast(join_message, sender_sock=None)

        conn.sendall(
            "You are connected. Type messages and press Enter. "
            'Type "/quit" to exit.\n'.encode("utf-8")
        )

        # Основний цикл читання повідомлень
        while True:
            data = conn.recv(1024)
            if not data:
                break

            text = data.decode("utf-8").strip()
            if not text:
                continue

            if text.lower() in {"/quit", "/exit"}:
                break

            msg = f"{username}: {text}\n"
            print(f"[MSG] {msg.strip()}")

            # Зберігаємо повідомлення в Redis
            redis_client.rpush("chat:messages", msg)

            # Надсилаємо іншим клієнтам
            broadcast(msg, sender_sock=conn)

    finally:
        # Вихід користувача
        with clients_lock:
            username = clients.pop(conn, "unknown")

        redis_client.hset(f"user:{username}", mapping={"status": "offline"})
        redis_client.srem("online_users", username)

        leave_message = f"{username} left the chat\n"
        print(f"[INFO] {addr} -> {leave_message.strip()}")
        redis_client.rpush("chat:messages", leave_message)
        broadcast(leave_message, sender_sock=None)

        conn.close()


def main() -> None:
    # Перевірка підключення до Redis
    try:
        redis_client.ping()
        print("[OK] Connected to Redis")
    except redis.exceptions.RedisError as exc:
        print(f"[ERROR] Redis connection failed: {exc}")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print(f"[OK] Chat server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_sock.accept()
            print(f"[NEW] Connection from {addr}")
            thread = threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True,
            )
            thread.start()


if __name__ == "__main__":
    main()

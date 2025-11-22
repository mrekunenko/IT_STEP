import socket
import threading
import sys


HOST = "127.0.0.1"  # IP сервера (той самий, що в server.py)
PORT = 5000         # Порт сервера


def listen_server(sock: socket.socket) -> None:
    """Постійно слухає сервер і виводить отримані повідомлення."""
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break

        if not data:
            break

        print(data.decode("utf-8"), end="")

    print("\n[INFO] Disconnected from server")
    # Якщо сервер закрив зʼєднання — завершуємо клієнт
    sys.exit(0)


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print(f"[OK] Connected to chat server {HOST}:{PORT}")

        # Потік для прослуховування повідомлень
        listener = threading.Thread(target=listen_server, args=(sock,), daemon=True)
        listener.start()

        try:
            # Перше, що введе користувач — це username (сервер попросить)
            while True:
                user_input = input()
                if not user_input:
                    continue

                # Локальна команда виходу
                if user_input.lower() in {"/quit", "/exit"}:
                    sock.sendall(user_input.encode("utf-8"))
                    break

                sock.sendall((user_input + "\n").encode("utf-8"))
        except KeyboardInterrupt:
            print("\n[INFO] Interrupted by user")

    print("[INFO] Client closed")


if __name__ == "__main__":
    main()

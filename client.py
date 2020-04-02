#!/usr/bin/env python3
import socket


def main():
    HOST = "127.0.0.1"
    PORT = 55555
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello")
        question = s.recv(1024).decode()
        while True:
            eval
            answer = str(eval(input(f"{question}: ")))
            s.sendall(answer.encode())
            data = s.recv(1024).decode()
            print(data)
            break


if __name__ == "__main__":
    main()

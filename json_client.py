#!/usr/bin/env python3
import socket
import argparse


def get_args():
    """Pull command line arguments."""
    parser = argparse.ArgumentParser(description='Client for JSON requests')
    parser.add_argument('data', nargs='?',
                        default='{"one": 1, "two": 2, "json": 3}',
                        help='The data to send to the server')
    return parser.parse_args()


def main():
    HOST = "localhost"
    PORT = 9999
    sent_data = get_args().data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(sent_data.encode())
        data = sock.recv(1024).decode()
        print(data)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import json
import socketserver
import threading


class JSONHandler(socketserver.BaseRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()
        print(f"{cur_thread.name}: Handling request")
        # self.request is the TCP socket connected to the client
        # self.data should become the JSON object sent in the request
        self.data = self.request.recv(1024).decode()
        try:
            # validate JSON object
            json.loads(self.data)
            msg = f"{cur_thread.name}: good"
        except json.JSONDecodeError:
            # self.data is not a valid JSON object
            msg = f"{cur_thread.name}: not good"
        # if self.data is formatted correctly, send back confirmation
        print(self.data, msg)
        self.request.sendall(msg.encode())


class JSONServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def get_args():
    """Pull command line arguments."""
    parser = argparse.ArgumentParser(description='Server for JSON requests')
    parser.add_argument('-p', '--port', default=9999, type=int,
                        help='The port to open the server on')
    return parser.parse_args()


def main():
    args = get_args()
    HOST, PORT = "localhost", args.port

    print(f"Opening server on port {PORT}")
    # Create the server, binding to localhost on user specified port
    with JSONServer((HOST, PORT), JSONHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        print(f"Main: Starting server on thread {server_thread.name}")
        server_thread.start()
        server_thread.join()


if __name__ == "__main__":
    main()

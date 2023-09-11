import socket
import threading
import json

with open("config_file.json", "r") as config_file:
    config_data = json.load(config_file)


class ClientHandler:
    def __init__(self, client_sock, client_addr):
        self.client_sock = client_sockimport socket
import threading
import json

with open("config_file.json", "r") as config_file:
    config_data = json.load(config_file)


class ClientHandler:
    def __init__(self, client_sock, client_addr):
        self.client_sock = client_sock
        self.client_addr = client_addr

    def receive_message(self):
        try:
            while True:
                msg = self.client_sock.recv(config_data["size"]).decode(config_data["format"])
                if not msg:
                    print("Client {} left the chat.".format(self.client_addr))
                    break
                print("client: {}".format(msg))
                if msg.lower() == "bye":
                    self.client_sock.send(msg.encode(config_data["format"]))

        except Exception as e:
            print("Error with client {}: {}".format(self.client_addr, str(e)))

    def send_message(self):
        try:
            while True:
                res = input()
                self.client_sock.send(res.encode(config_data["format"]))

        except Exception as e:
            print("Error with client {}: {}".format(self.client_addr, str(e)))


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def start(self):
        print("Server listening on {}:{}".format(self.host, self.port))
        try:
            while True:
                client_sock, client_addr = self.sock.accept()
                print(f"Connected to {client_addr}")
                client_handler = ClientHandler(client_sock, client_addr)
                thread_1 = threading.Thread(target=client_handler.receive_message)
                thread_2 = threading.Thread(target=client_handler.send_message)
                thread_1.start()
                thread_2.start()
        except KeyboardInterrupt:
            print("Server shutting down...")
        finally:
            self.sock.close()


def main():
    server_config = config_data["server"]
    server = Server(server_config["ip"], server_config["port"])
    server.start()


if __name__ == "__main__":
    main()

        self.client_addr = client_addr

    def receive_message(self):
        try:
            while True:
                msg = self.client_sock.recv(config_data["size"]).decode(config_data["format"])
                if not msg:
                    print("Client {} left the chat.".format(self.client_addr))
                    break
                print("client: {}".format(msg))
                if msg.lower() == "bye":
                    self.client_sock.send(msg.encode(config_data["format"]))

        except Exception as e:
            print("Error with client {}: {}".format(self.client_addr, str(e)))

    def send_message(self):
        try:
            while True:
                res = input()
                self.client_sock.send(res.encode(config_data["format"]))

        except Exception as e:
            print("Error with client {}: {}".format(self.client_addr, str(e)))


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def start(self):
        print("Server listening on {}:{}".format(self.host, self.port))
        try:
            while True:
                client_sock, client_addr = self.sock.accept()
                print(f"Connected to {client_addr}")
                client_handler = ClientHandler(client_sock, client_addr)
                thread_1 = threading.Thread(target=client_handler.receive_message)
                thread_2 = threading.Thread(target=client_handler.send_message)
                thread_1.start()
                thread_2.start()
        except KeyboardInterrupt:
            print("Server shutting down...")
        finally:
            self.sock.close()


def main():
    server_config = config_data["server"]
    server = Server(server_config["ip"], server_config["port"])
    server.start()


if __name__ == "__main__":
    main()

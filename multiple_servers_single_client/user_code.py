import socket
import json


with open("config_file.json", "r") as config_file:
    config_data = json.load(config_file)


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def send_message(self, message):
        self.sock.send(message.encode(config_data["format"]))

    def response(self):
        response = self.sock.recv(config_data["size"]).decode(config_data["format"])
        print("Received response:", response)

    def close(self):
        self.sock.close()


def broadcast():
    server_config = config_data["servers"]
    try:
        while True:
            message = input("Enter message to send (type 'bye' to exit): ")
            for server in server_config.values():
                client_obj = Client(server["host"], server["port"])
                client_obj.send_message(message)
                client_obj.response()
                client_obj.close()
            if message.lower() == "bye":
                break
    except KeyboardInterrupt:
        print("\nClient shutting down...")


def main():
    broadcast()


if __name__ == "__main__":
    main()

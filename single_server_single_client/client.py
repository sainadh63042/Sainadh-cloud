import socket
import threading
import json

with open("config_file.json", "r") as config_file:
    config_data = json.load(config_file)


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_message(self):
        try:
            while True:
                message = input()
                self.sock.send(message.encode(config_data["format"]))
                if message.lower() == "bye":
                    break
        except Exception as e:
            print("error: ", str(e))
        finally:
            self.sock.close()

    def receive_message(self):
        try:
            while True:
                response = self.sock.recv(config_data["size"]).decode(config_data["format"])
                if response:
                    break
                print("server: {}".format(response))
        except Exception as e:
            print("error: ", str(e))
        finally:
            self.sock.close()


def main():
    server_config = config_data["server"]
    client = Client(server_config["ip"], server_config["port"])
    thread_1 = threading.Thread(target=client.send_message)
    thread_2 = threading.Thread(target=client.receive_message)
    thread_1.start()
    thread_2.start()


if __name__ == "__main__":
    main()

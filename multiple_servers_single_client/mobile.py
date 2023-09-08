import socket
import threading
import json

with open("config_file.json", "r") as config_file:
    config_data = json.load(config_file)


class UserHandler(threading.Thread):
    def __init__(self, user_sock, user_addr):
        super().__init__()
        self.user_sock = user_sock
        self.User_addr = user_addr

    def run(self):
        try:
            while True:
                data = self.user_sock.recv(config_data["size"]).decode(config_data["format"])
                if data:
                    print("Received from {}: {}".format(self.User_addr, data))
                    response = "Mobile received: {}".format(data)
                    self.user_sock.sendall(response.encode(config_data["format"]))
                if data.lower() == "bye":
                    print("User {} is left the chat.".format(self.User_addr))
                    break
        except Exception as e:
            print("Error with user {}: {}".format(self.User_addr, str(e)))
        finally:
            self.user_sock.close()


class Mobile:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def start(self):
        print("Mobile server listening on {}:{}".format(self.host, self.port))
        try:
            while True:
                user_sock, user_addr = self.sock.accept()
                user_handler = UserHandler(user_sock, user_addr)
                user_handler.start()
        except KeyboardInterrupt:
            print("Mobile shutting down...")
        finally:
            self.sock.close()


def main():
    mobile_config = config_data["servers"]["mobile_server"]
    mobile = Mobile(mobile_config["host"], mobile_config["port"])
    mobile.start()


if __name__ == "__main__":
  main()

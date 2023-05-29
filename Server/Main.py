#!/usr/bin/env python3.11.2
import sys

from colorama import Fore

from Server import Server


class Main:
    """
    I know full fucking well there's an automatic argument parser library. I've been doing programming for YEARS.
    I refuse to use it, I simply like sys.argv better due to the simplicity of lists.
    I just would like to make my own handler too, I think it would be nicer than relying on nothing but other libraries
    to do something simple like this, it's just out of question for me.

    Everything here has been created by me, nevertheless down to something as simple as this.
    So anyway, enjoy the menu!
    """

    def __init__(self) -> None:
        self.argv = sys.argv[1:]
        if len(self.argv) < 2:
            print(
                '\n'.join(f'{Fore.LIGHTYELLOW_EX}{argument_name}{Fore.LIGHTGREEN_EX} - {Fore.LIGHTCYAN_EX}{description}'
                          for argument_name, description in self.dict_arguments.items())
            )
        else:
            ip: str = str(self.argv[0])
            port: int = int(self.argv[1])

            self.start(ip, port)

    # Do not modify this unless you know what you are doing.
    @staticmethod
    def start(host_ip: str, host_port: int):
        return Server(host_ip, host_port)

    @property
    def dict_arguments(self) -> dict:
        return {"IP": "The IP to specify.", "PORT": "The port number to specify."}


if __name__ == '__main__':
    Main()

#!/usr/bin/env python3.11.2
import sys


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
        if sys.argv is None:
            pass

        self.command_name = self.argv[0]
        self.arguments = sys.argv[2:]

        print(self.arguments)

    def specify_arguments(self):
        pass


if __name__ == '__main__':
    Main()

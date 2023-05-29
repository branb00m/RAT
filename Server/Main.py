import sys


class Main:
    def __init__(self) -> None:
        self.argv = sys.argv[1:]

        self.command_name = self.argv[0]
        self.arguments = sys.argv[2:]

        print(self.arguments)


if __name__ == '__main__':
    Main()

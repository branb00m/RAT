from colorama import Fore


class Eval:
    """
    Evaluation. Allows you to execute custom Python code on command.
    You may import packages too (They have to be Python installed.)
    """
    def __init__(self, args: list[str]):
        self.args = args
        self.to_execute = '\n'.join(self.args)

        try:
            exec(self.to_execute)
        except Exception as err:
            print(err)

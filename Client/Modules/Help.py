import os

from colorama import Fore


class Help:
    """
    Help command. What do you think this is?
    """
    def __init__(self, args: list) -> None:
        self.modules_folder: str = 'Modules'
        self.modules_path = os.path.join(os.path.split(os.path.abspath(__file__))[0])
        self.filtered_modules: list[str] = ['__init__.py']

        self._help_str: str = ''
        self._help_counter: int = 0

        for file in sorted(os.listdir(self.modules_path)):
            file: str = file.lower()

            if file not in self.filtered_modules and file.endswith('.py'):
                module_name = file[:-3].capitalize()
                documentation = self.get_documentation(module_name)

                self._help_counter += 1
                self._help_str += f'{Fore.LIGHTGREEN_EX}{module_name}: {documentation}\n'

        print(self._help_str)

    def get_documentation(self, module_name: str):
        return getattr(__import__(f'{self.modules_folder}.{module_name}',
                                  fromlist=[module_name]), module_name).__doc__

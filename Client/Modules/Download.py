import os

import win32api


class Download:
    """
    Allows you to download all files (with an extension filter or not.)
    Example: download .py .txt .png
    or
    Example: download (Which just executes and downloads ALL files.)
    """

    def __init__(self, args: list = None):
        counter = 0
        child_tabs = '  '

        for drive_letter in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            print(drive_letter)

            n = os.walk(drive_letter).__next__()[1]

            for directory in n:
                print(directory)

            print(n)

import subprocess


class Shell:
    def __init__(self, args: list):
        command_output = subprocess.Popen(args,
                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                          shell=True)

        stdout = command_output.stdout.read()
        stdout_decoded = stdout.strip().decode()

        stderr = command_output.stderr.read()
        stderr_decoded = stderr.strip().decode()

        if stdout:
            print(stdout_decoded)
        elif stderr:
            print(stderr_decoded)

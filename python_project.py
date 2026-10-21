import sys, os

class Main:
    def __init__(self, args):
        self.name = " ".join(args[1:])
        self.dirs = [
            self.name,
            f"{self.name}/core",
            f"{self.name}/core/modules",
            f"{self.name}/core/dependencies"
        ]

        self.files = {
            f"{self.name}/main.py" : "",
            f"{self.name}/.gitignore" : """# Folders
env
__pycache__

# Files
config.json
test""",
            f"{self.name}/readme.md" : f"# {self.name}",
            f"{self.name}/core/modules/logging.py" : """from datetime import datetime
from colorama import Fore

def success(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.GREEN}[+]{Fore.RESET}\t{message}"
    if verbose:
        print(msg)
    return msg

def error(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.RED}[-]{Fore.RESET}\t{message}"
    if verbose:
        print(msg)
    return msg

def info(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.BLUE}[!]{Fore.RESET}\t{message}"
    if verbose:
        print(msg)
    return msg

def inpt(message):
    return input( f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}\t{Fore.BLUE}[?]{Fore.RESET}\t{message} : ")"""
        }

        self.make_dirs()
        self.make_files()

    def make_dirs(self):
        for dir in self.dirs:
            os.mkdir(dir)

    def make_files(self):
        for file in self.files:
            open(file, "w").write(self.files[file])



if __name__ == "__main__":
    main = Main(sys.argv)
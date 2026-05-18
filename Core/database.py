from Commands import install
from Commands import uninstall

import sys

def main():
    try:
        args = sys.argv

        if args[1] == 'api' and args[2] == 'install':
            install.install(args)
        elif args[1] == 'api' and args[2] == 'uninstall':
            uninstall.uninstall(args)
    except Exception as e:
        print(f'fatal error , your error is {e}')



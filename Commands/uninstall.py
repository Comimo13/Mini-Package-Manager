import os

def uninstall(args):
    running = True
    while running:
        if args[3] == 'plus':
            if 'plus.py' in os.listdir('Modules'):
                os.remove('Modules/plus.py')
                running = False
            else:
                print('There are no this package')
                running = False
        elif args[3] == 'minus':
            if 'minus.py' in os.listdir('Modules'):
                os.remove('Modules/minus.py')
                running = False
            else:
                print('There are no this package')
                running = False
        elif args[3] == 'divide':
            if 'divide.py' in os.listdir('Modules'):
                os.remove('Modules/divide.py')
                running = False
            else:
                print('There are no this package')
                running = False
        elif args[3] == 'multiply':
            if 'multiply.py' in os.listdir('Modules'):
                os.remove('Modules/multiply.py')
                running = False
            else:
                print('There are no this package')
                running = False
        elif args[3] == 'squareroot':
            if 'squareroot.py' in os.listdir('Modules'):
                os.remove('Modules/squareroot.py')
                running = False
            else:
                print('There are no this package')
                running = False
        elif args[3] == 'pow':
            if 'pow.py' in os.listdir('Modules'):
                os.remove('Modules/pow.py')
                running = False
            else:
                print('There are no this package')
                running = False
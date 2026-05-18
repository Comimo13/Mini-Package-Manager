import shutil

def install(args):
        running = True
        while running:
            if args[3] == 'plus':
                from Functions import plus

                first_input = int(input('Please enter the first number: '))
                second_input = int(input('Please enter the second number: '))
                shutil.copy('Functions/plus.py', 'Modules')
                print(plus.plus(first_input, second_input))
                running = False
            elif args[3] == 'minus':
                from Functions import minus

                first_input = int(input('Please enter the first number: '))
                second_input = int(input('Please enter the second number: '))
                shutil.copy('Functions/minus.py', 'Modules')
                print(minus.minus(first_input, second_input))
                running = False
            elif args[3] == 'divide':
                from Functions import divide

                first_input = int(input('Please enter the first number: '))
                second_input = int(input('Please enter the second number: '))
                shutil.copy('Functions/divide.py', 'Modules')
                print(divide.divide(first_input, second_input))
                running = False
            elif args[3] == 'multiply':
                from Functions import multiply

                first_input = int(input('Please enter the first number: '))
                second_input = int(input('Please enter the second number: '))
                shutil.copy('Functions/multiply.py', 'Modules')
                print(multiply.multiply(first_input, second_input))
                running = False
            elif args[3] == 'squareroot':
                from Functions import squareroot

                second_input = int(input('Please enter the second number: '))
                shutil.copy('Functions/squareroot.py', 'Modules')
                print(squareroot.squareroot(second_input))
            elif args[3] == 'pow':
                from Functions import pow

                first_input = int(input('Please enter the first number: '))
                second_input = int(input('Please enter the second number: '))
                shutil.copy('Functions/squareroot.py', 'Modules')
                print(pow.pow(first_input, second_input))
                running = False
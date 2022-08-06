from termcolor import colored as col
import getpass
import platform
import os
from commands import whoami, sudo

USERNAME = getpass.getuser()
PLATFORM = platform.system()

PASSWORD = '123'

PREFIX_COLOR = 'cyan'

PREFIX = col(f'{str(USERNAME)}@{str(PLATFORM)}', PREFIX_COLOR) + '$ '

os.system('cls' if os.name=='nt' else 'clear')

def sudo_password():
    count = 1
    pwd_input = getpass.getpass('SUDO: Enter password: ')
    if pwd_input == PASSWORD:
        return True
    else:
        while True:
            count += 1
            if count <= 3:
                pwd_input = getpass.getpass('SUDO: Wrong password! Try again: ')
                if pwd_input == PASSWORD:
                    return True
            else:
                print('SUDO: Password was wrong for the third time! EXIT')
                return False

while True:
    command = input(PREFIX)
    if command.lower().startswith('whoami'):
        whoami.command()
    elif command.lower().startswith('sudo'):
        result = sudo_password()
        if result:
            print('Correct pwd')
        else:
            print('Wrong pwd')
    else:
        result = os.system(command)
        
        


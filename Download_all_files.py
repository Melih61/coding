import os
import time
import platform
try:
    import wget
except:
    os.system('pip install wget')
try:
    from termcolor import colored as col
except:
    os.system('pip install termcolor')
import subprocess

github_url = 'https://github.com/XanOpiat/Python-CSGO-Cheat.git'
git_url = 'https://github.com/git-for-windows/git/releases/download/v2.37.1.windows.1/Git-2.37.1-64-bit.exe'

def message(text):
    return col(text, 'green')

if input(message('Do you have git installed on your device? (y/n)')) == 'n':
    if input('We are going to install git to download the files. (y/n)').lower() == 'y':
        platform_name = platform.system()
        if platform_name.lower() == 'windows':
            wget.download(git_url, 'C:\\Users\\git.exe')
            subprocess.Popen(f'C:\\Users\\git.exe')
            os.remove('C:\\Users\\git.exe')
        elif platform_name.lower() == 'linux':
            os.system('sudo apt update')
            os.system('sudo apt-get install git-all')
        else:
            print('Your os is not supported')
if input('Do you want to install all files to your Downloads directory? (y/n)').lower() == 'n':
    directory = input('Enter the directory to install files: ')
    if os.path.exists(directory):
        print('Starting to install files from github (internet connection required)...')
        os.system(f'git clone https://github.com/Melih61/coding.git {str(directory)}/coding_projects')
else:
    print('Starting to install files from github (internet connection required)...')
    os.system(f'git clone https://github.com/Melih61/coding.git C:\\Users\\{str(getpass.getuser())}\\Downloads\\coding_projects') if platform.system() == 'windows' else os.system('git clone https://github.com/Melih61/coding.git ~/Downloads/coding_projects')
print('Successfully installed files\nYou can close this terminal now.')
time.sleep(1000)

import os
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import wget

def startInstaller():
    path = os.path.expanduser('~')
    def install(path):
        def start_to_install():
            if os.path.exists(path):
                if os.path.exists(path+'\\malehTerminal'):
                    pass
                else:
                    os.mkdir(path + '\\malehTerminal')
                with open(path+'\\malehTerminal\\settings.txt', 'w') as file:
                    file.write('PROMPTCOLOR:green\nDIRECTORYCOLOR:cyan')
                    file.close()
                if os.path.exists(path+'\\malehTerminal\\malehTerminal.exe'):
                    try:
                        os.remove(path+'\\malehTerminal\\malehTerminal.exe')
                    except:
                        pass
                wget.download('https://malehterminal.netlify.app/main.exe', path+'\\malehTerminal\\malehTerminal.exe')
                messagebox.showinfo(title='Installation complete', message='Successfully installed malehTerminal')
        start_to_install()
    install(path)

question_box = messagebox.askyesno(title='Installation', message='Do you want to install malehTerminal?')
if question_box:
    startInstaller()
else:
    exit()

from tkinter import *
from tkinter import messagebox
import os

BACKGROUND_COLOR = '#6A6764'
FOREGROUND_COLOR = 'white'

class CreateMenu:
    def __init__(self, text, function):
        Button(main_menu, text=text, width=20, font=('Consolas',15), command=function,foreground=FOREGROUND_COLOR, background=BACKGROUND_COLOR, activeforeground=FOREGROUND_COLOR, activebackground=BACKGROUND_COLOR).pack()

class Empty():
    def __init__(self, window):
        Label(window, text='\n', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()

def move_file():
    def movefile():
        from_path = from_directory.get()
        to_path = to_directory.get()

        basename = os.path.basename(from_path)

        if os.path.exists(from_path):
            if os.path.exists(to_path):
                os.rename(from_path, to_path + f'\\{str(basename)}')
                messagebox.showinfo(title='Move completed', message='Successfully moved file')
            else:
                messagebox.showerror(title='Path not found', message=f'Path "{to_path}" does not exist')
        else:
            messagebox.showerror(title='Path not found', message=f'Path "{from_path}" does not exist')

    movefile_menu = Tk()
    movefile_menu.configure(background=BACKGROUND_COLOR)
    movefile_menu.geometry('400x600')
    movefile_menu.resizable(False, False)
    movefile_menu.title('Move file')

    Label(movefile_menu, text='Move file', font=('Gabriola',25), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack(padx=10, pady=10)

    Label(movefile_menu, text='From: ', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
    from_directory = Entry(movefile_menu, font=('Consolas',15), width=30, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    from_directory.pack()

    Label(movefile_menu, text='\nTo: ', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
    to_directory = Entry(movefile_menu, font=('Consolas',15), width=30, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    to_directory.pack()

    Empty(movefile_menu)
    Button(movefile_menu, text='Move file', font=('Consolas',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, activebackground=BACKGROUND_COLOR, activeforeground=FOREGROUND_COLOR, command=movefile).pack()

    movefile_menu.mainloop()

def create_directory():
    def createdirectory():
        directory = new_directory.get()
        if os.path.exists(directory):
            messagebox.showerror(title='Directory already exists', message=f'Directory "{str(directory)}" already exists')
        else:
            os.mkdir(directory)
            messagebox.showinfo(title='Finished', message='Successfully created directory')
            new_directory.delete(0, END)
    createdir_menu = Tk()
    createdir_menu.geometry('400x600')
    createdir_menu.configure(background=BACKGROUND_COLOR)
    createdir_menu.resizable(False, False)
    createdir_menu.title('Create directory')

    Label(createdir_menu, text='Create directory', font=('Gabriola',25), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack(padx=10, pady=10)

    Label(createdir_menu, text='New directory to create: ', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
    new_directory = Entry(createdir_menu, font=('Consolas',15), width=30, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    new_directory.pack()
    Empty(createdir_menu)
    Button(createdir_menu, text='Create directory', font=('Consolas',15), width=30, command=createdirectory, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, activebackground=BACKGROUND_COLOR, activeforeground=FOREGROUND_COLOR).pack()

    createdir_menu.mainloop()

def delete_files():

    def deletefiles():
        directory = directory_entry.get()
        filetypes = file_types.get(1.0, END).split(' ')

        count = 0

        if os.path.exists(directory):
            all_files = os.listdir(directory)
            for files in all_files:
                for filetype in filetypes:
                    if filetype.endswith('\n'):
                        filetype = filetype.replace('\n', '')
                    if files.endswith(filetype):
                        os.remove(f'{str(directory)}\\{str(files)}')
                        count += 1
            if count == 0:
                messagebox.showwarning(title='No files found', message='No files were found')
            else:
                messagebox.showinfo(title='Deleted files', message=f'Successfully deleted {str(count)} files')
        else:
            messagebox.showerror(title='Directory not found', message=f'Directory {str(directory)} not found')

    deletefiles_menu = Tk()
    deletefiles_menu.title('Delete files')
    deletefiles_menu.geometry('400x600')
    deletefiles_menu.configure(background=BACKGROUND_COLOR)
    deletefiles_menu.resizable(False, False)

    Label(deletefiles_menu, text='Delete files', font=('Gabriola',25), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack(padx=10, pady=10)
    Label(deletefiles_menu, text='Directory:', font=('Consolas',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
    directory_entry = Entry(deletefiles_menu, font=('Consolas',15), width=30, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    directory_entry.pack()
    Empty(deletefiles_menu)
    Label(deletefiles_menu, text='File types', font=('Consolas',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
    file_types = Text(deletefiles_menu, font=('Consolas',15), width=30, height=12, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    file_types.pack()
    Label(deletefiles_menu, font=('Consolas',7), text='Split the file types with a space like: .png .gif .jpg .mp4', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
    Empty(deletefiles_menu)
    Button(deletefiles_menu, font=('Consolas',15), text='Delete files', command=deletefiles, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, activebackground=BACKGROUND_COLOR, activeforeground=FOREGROUND_COLOR).pack()


main_menu = Tk()
main_menu.configure(background=BACKGROUND_COLOR)
main_menu.geometry('400x600')
main_menu.resizable(False, False)
main_menu.title('Main')

Label(main_menu, text='\nBetter Life by maleh\n', width=400, font=('Gabriola',30), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).pack()
CreateMenu(text='Move file', function=move_file)
Empty(main_menu)
CreateMenu(text='Create directory', function=create_directory)
Empty(main_menu)
CreateMenu(text='Delete files', function=delete_files)

main_menu.mainloop()    

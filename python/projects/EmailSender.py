import time
from tkinter import *
from tkinter import ttk
import smtplib
from tkinter.ttk import Style

BACKGROUND_COLOR = '#322f30'
FOREGROUND_COLOR = 'white'

def send_email_gmail():
    sender = email_entry_gmail.get()
    receiver = target_email_entry_gmail.get()
    password = password_email_entry_gmail.get()
    subject = subject_email_entry_gmail.get()
    body = text_gmail.get(1.0, END)
    if(sender == '' or sender == None):
        output_text_gmail.config(state=NORMAL)
        output_text_gmail.delete(1.0, END)
        output_text_gmail.insert(1.0, 'Fehler: Gebe eine gültige E-Mail ein')
        output_text_gmail.config(fg='dark red', state=DISABLED)
    elif(receiver == '' or receiver == None):
        output_text_gmail.config(state=NORMAL)
        output_text_gmail.delete(1.0, END)
        output_text_gmail.insert(1.0, 'Fehler: Gebe eine gültige Empfänger E-Mail ein')
        output_text_gmail.config(fg='dark red', state=DISABLED)
    elif(password == '' or password == None):
        output_text_gmail.config(state=NORMAL)
        output_text_gmail.delete(1.0, END)
        output_text_gmail.insert(1.0, 'Fehler: Gebe ein gültiges Passwort ein')
        output_text_gmail.config(fg='dark red', state=DISABLED)
    elif(subject == '' or subject == None):
        output_text_gmail.config(state=NORMAL)
        output_text_gmail.delete(1.0, END)
        output_text_gmail.insert(1.0, 'Fehler: Gebe eine gültige Überschrift ein')
        output_text_gmail.config(fg='dark red', state=DISABLED)
    elif(body == '' or body == None):
        output_text_gmail.config(state=NORMAL)
        output_text_gmail.delete(1.0, END)
        output_text_gmail.insert(1.0, 'Fehler: Gebe ein gültigen Text ein')
        output_text_gmail.config(fg='dark red', state=DISABLED)
    else:
        output_text_gmail.config(state=NORMAL)
        output_text_gmail.delete(1.0, END)

        message = f"""From: {sender}
        To: {receiver}
        Subject: {subject}\n
        {body}
        """

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
            server.login(sender, password)
            output_text_gmail.config(state=NORMAL)
            output_text_gmail.delete(1.0, END)
            output_text_gmail.insert(1.0,'Erfolgreich angemeldet...\nE-Mail wird gesendet...')
            output_text_gmail.config(state=DISABLED)
            time.sleep(2)
            server.sendmail(sender, receiver, message)
            output_text_gmail.config(state=NORMAL)
            output_text_gmail.delete(1.0, END)
            output_text_gmail.insert(1.0,'E-Mail erfolgreich gesendet!')
            output_text_gmail.config(state=DISABLED)
        except smtplib.SMTPAuthenticationError:
            output_text_gmail.config(state=NORMAL)
            output_text_gmail.delete(1.0, END)
            output_text_gmail.insert(1.0,'Fehler: Es ist ein Fehler bei der Anmeldung aufgetreten!\n'
                                         'Mögliche Ursachen hierfür sind:\n'
                                         '1. Falsches Passwort\n'
                                         '2. 2. Stufe Authentifizierung\n'
                                         'Falls das nicht der Fall sein sollte informiere dich im Internet')
            output_text_gmail.config(state=DISABLED, fg='dark red')
        except Exception:
            output_text_gmail.config(state=NORMAL)
            output_text_gmail.delete(1.0, END)
            output_text_gmail.insert(1.0, 'Fehler: Es ist ein unbekannter Fehler aufgetreten')
            output_text_gmail.config(state=DISABLED, fg='dark red')



def send_email_yahoo():
    sender = email_entry_yahoo.get()
    receiver = target_email_entry_yahoo.get()
    password = password_email_entry_yahoo.get()
    subject = subject_email_entry_yahoo.get()
    body = text_yahoo.get(1.0, END)
    if(sender == '' or sender == None):
        output_text_yahoo.config(state=NORMAL)
        output_text_yahoo.delete(1.0, END)
        output_text_yahoo.insert(1.0, 'Fehler: Gebe eine gültige E-Mail ein')
        output_text_yahoo.config(fg='dark red', state=DISABLED)
    elif(receiver == '' or receiver == None):
        output_text_yahoo.config(state=NORMAL)
        output_text_yahoo.delete(1.0, END)
        output_text_yahoo.insert(1.0, 'Fehler: Gebe eine gültige Empfänger E-Mail ein')
        output_text_yahoo.config(fg='dark red', state=DISABLED)
    elif(password == '' or password == None):
        output_text_yahoo.config(state=NORMAL)
        output_text_yahoo.delete(1.0, END)
        output_text_yahoo.insert(1.0, 'Fehler: Gebe ein gültiges Passwort ein')
        output_text_yahoo.config(fg='dark red', state=DISABLED)
    elif(subject == '' or subject == None):
        output_text_yahoo.config(state=NORMAL)
        output_text_yahoo.delete(1.0, END)
        output_text_yahoo.insert(1.0, 'Fehler: Gebe eine gültige Überschrift ein')
        output_text_yahoo.config(fg='dark red', state=DISABLED)
    elif(body == '' or body == None):
        output_text_yahoo.config(state=NORMAL)
        output_text_yahoo.delete(1.0, END)
        output_text_yahoo.insert(1.0, 'Fehler: Gebe ein gültigen Text ein')
        output_text_yahoo.config(fg='dark red', state=DISABLED)
    else:
        output_text_yahoo.config(state=NORMAL)
        output_text_yahoo.delete(1.0, END)

        message = f"""From: {sender}
        To: {receiver}
        Subject: {subject}\n
        {body}
        """

        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()

        try:
            server.login(sender, password)
            output_text_yahoo.config(state=NORMAL, fg='black')
            output_text_yahoo.delete(1.0, END)
            output_text_yahoo.insert(1.0,'Erfolgreich angemeldet...\nE-Mail wird gesendet...')
            output_text_yahoo.config(state=DISABLED,fg='black')
            time.sleep(2)
            server.sendmail(sender, receiver, message)
            output_text_yahoo.config(state=NORMAL,fg='black')
            output_text_yahoo.delete(1.0, END)
            output_text_yahoo.insert(1.0,'E-Mail erfolgreich gesendet!')
            output_text_yahoo.config(state=DISABLED,fg='black')
        except smtplib.SMTPAuthenticationError:
            output_text_yahoo.config(state=NORMAL, fg='dark red')
            output_text_yahoo.delete(1.0, END)
            output_text_yahoo.insert(1.0,'Fehler: Es ist ein Fehler bei der Anmeldung aufgetreten!\n'
                                         'Mögliche Ursachen hierfür sind:\n'
                                         '1. Falsches Passwort\n'
                                         '2. 2. Stufe Authentifizierung\n'
                                         'Falls das nicht der Fall sein sollte informiere dich im Internet')
            output_text_yahoo.config(state=DISABLED, fg='dark red')
        except Exception:
            output_text_yahoo.config(state=NORMAL, fg='dark red')
            output_text_yahoo.delete(1.0, END)
            output_text_yahoo.insert(1.0,'Fehler: Es ist ein unbekannter Fehler aufgetreten')
            output_text_yahoo.config(state=DISABLED, fg='dark red')




window = Tk()
window.geometry('600x640')
window.resizable(False, False)
window.title('Python E-Mail Sender')
window.config(background=BACKGROUND_COLOR)

style = Style()
style.theme_create(
    "name", parent="alt", settings={
        ".": {"configure": {"background": BACKGROUND_COLOR,
                            "foreground": "white",
                            'borderwidth': 0}},
        "TLabel": {"configure": {"foreground": "white",
                                 "padding": 10,
                                 "font": ("Calibri", 16)}},
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]},
                      'borderwidth': 0
                      },
        "TNotebook.Tab": {
            "configure": {"bordercolor": BACKGROUND_COLOR,
                          'borderwidth': 1,
                          "darkcolor": BACKGROUND_COLOR,
                          "lightcolor": BACKGROUND_COLOR,
                          "padding": [5, 1], "background": BACKGROUND_COLOR
                          },
            "map": {"background": [("selected", BACKGROUND_COLOR)],
                    "expand": [("selected", [1, 1, 1, 0])]}
        }
    })

style.theme_use("name")

notebook = ttk.Notebook(window)

tab_gmail = Frame(notebook, background=BACKGROUND_COLOR)
tab_yahoo = Frame(notebook, background=BACKGROUND_COLOR)

notebook.add(tab_gmail, text='G-Mail')
notebook.add(tab_yahoo, text='Yahoo')

PythonImage = PhotoImage(file='python.png')

main_label = Label(window, image=PythonImage ,text=" Python E-Mail Sender", font=('Courier',25), compound=LEFT, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, padx=10, pady=10)
main_label.pack()

notebook.pack(expand=True, fill='both')

empty_label1 = Label(tab_gmail, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=0,columnspan=4)

email_label_gmail = Label(tab_gmail, text='Deine E-Mail: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
email_label_gmail.grid(row=1,column=0)
email_entry_gmail = Entry(tab_gmail, width=60, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
email_entry_gmail.grid(row=1, column=1)

target_email_label_gmail = Label(tab_gmail, text='Empfänger E-Mail: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
target_email_label_gmail.grid(row=2,column=0)
target_email_entry_gmail = Entry(tab_gmail, width=60, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
target_email_entry_gmail.grid(row=2, column=1)

password_email_label_gmail = Label(tab_gmail, text='E-Mail Passwort: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
password_email_label_gmail.grid(row=3,column=0)
password_email_entry_gmail = Entry(tab_gmail, width=60, show='*', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
password_email_entry_gmail.grid(row=3, column=1)

subject_email_label_gmail = Label(tab_gmail, text='Überschrift: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
subject_email_label_gmail.grid(row=4,column=0)
subject_email_entry_gmail = Entry(tab_gmail, width=60, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
subject_email_entry_gmail.grid(row=4, column=1)

text_gmail_label = Label(tab_gmail, text='Text: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
text_gmail_label.grid(row=5,column=0)
text_gmail = Text(tab_gmail, width=45, height=5, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
text_gmail.grid(row=5,column=1)

empty_label2 = Label(tab_gmail, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=6)

gmail_button = Button(tab_gmail, text='E-Mail senden', font=('Courier',15), command=send_email_gmail, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
gmail_button.grid(row=7, column=0, columnspan=3)

empty_label3 = Label(tab_gmail, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=8)

output_label_gmail = Label(tab_gmail,text='Output:', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=9, column=0, columnspan=3)

output_text_gmail = Text(tab_gmail, font=('Courier',10), width=70, height=9, state=DISABLED, bg='grey')
output_text_gmail.grid(row=10,column=0,columnspan=3)

# yahoo

empty_label1 = Label(tab_yahoo, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=0,columnspan=4)

email_label_yahoo = Label(tab_yahoo, text='Deine E-Mail: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
email_label_yahoo.grid(row=1,column=0)
email_entry_yahoo = Entry(tab_yahoo, width=60, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
email_entry_yahoo.grid(row=1, column=1)

target_email_label_yahoo = Label(tab_yahoo, text='Empfänger E-Mail: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
target_email_label_yahoo.grid(row=2,column=0)
target_email_entry_yahoo = Entry(tab_yahoo, width=60, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
target_email_entry_yahoo.grid(row=2, column=1)

password_email_label_yahoo = Label(tab_yahoo, text='E-Mail Passwort: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
password_email_label_yahoo.grid(row=3,column=0)
password_email_entry_yahoo = Entry(tab_yahoo, width=60, show='*', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
password_email_entry_yahoo.grid(row=3, column=1)

subject_email_label_yahoo = Label(tab_yahoo, text='Überschrift: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
subject_email_label_yahoo.grid(row=4,column=0)
subject_email_entry_yahoo = Entry(tab_yahoo, width=60, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
subject_email_entry_yahoo.grid(row=4, column=1)

text_yahoo_label = Label(tab_yahoo, text='Text: ', font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
text_yahoo_label.grid(row=5,column=0)
text_yahoo = Text(tab_yahoo, width=45, height=5, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
text_yahoo.grid(row=5,column=1)

empty_label2 = Label(tab_yahoo, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=6)

yahoo_button = Button(tab_yahoo, text='E-Mail senden', font=('Courier',15), command=send_email_yahoo, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
yahoo_button.grid(row=7, column=0, columnspan=3)

empty_label3 = Label(tab_yahoo, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=8)

output_label_yahoo = Label(tab_yahoo,text='Output:', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=9, column=0, columnspan=3)

output_text_yahoo = Text(tab_yahoo, font=('Courier',10), width=70, height=9, state=DISABLED, bg='grey')
output_text_yahoo.grid(row=10,column=0,columnspan=3)

window.mainloop()

from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from tkinter import ttk

BACKGROUND_COLOR = '#322f30'
FOREGROUND_COLOR = 'white'
ERROR_COLOR = 'red'

def track_number():
	number = phone_number_entry.get()
	if number == '' or number == None:
		company_country_label.grid_forget()
		phone_country_label.config(foreground=ERROR_COLOR,font=('Courier',15), text='Error: Enter a phone number')
		phone_country_label.grid(row=5, column=0, columnspan=2)
		window.update()
	else:
		try:
			country = phonenumbers.parse(number, 'CH')
			service = phonenumbers.parse(number, 'RO')
			if not geocoder.description_for_number(country, 'en').strip():
				company_country_label.grid_forget()
				phone_country_label.config(foreground=ERROR_COLOR, text=f'Error: {number} is not a number', font=('Courier',15))
				phone_country_label.grid(row=5, column=0, columnspan=2)
				window.update()
			else:
				phone_country_label.config(foreground=FOREGROUND_COLOR, font=('Courier',10))
				phone_country_label.config(text='Country: {}'.format(str(geocoder.description_for_number(country, 'en'))))
				company_country_label.config(text='Service: {}'.format(str(carrier.name_for_number(service, 'en'))))
				phone_country_label.grid(row=5, column=0, columnspan=2)
				company_country_label.grid(row=7, column=0, columnspan=2)
				window.update()
		except Exception:
			company_country_label.grid_forget()
			phone_country_label.config(foreground=ERROR_COLOR, text=f'Error: {number} is not a number', font=('Courier',15))
			phone_country_label.grid(row=5, column=0, columnspan=2)
			window.update()

window = Tk()
window.geometry('600x380')
window.config(background=BACKGROUND_COLOR)
window.title('Phone Number Tracker')

main_frame = Frame(window, background=BACKGROUND_COLOR)
main_frame.pack()

mainlabel = Label(main_frame, text='Phone Number', font=('Courier',45), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
mainlabel.grid(row=0, column=0, columnspan=2)
mainlabel2 = Label(main_frame, text='Tracker', font=('Courier',25), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
mainlabel2.grid(row=1, column=0, columnspan=2)

frame = Frame(window, background=BACKGROUND_COLOR)
frame.pack()

Label(frame, text='\nYou need to use +\nExample: +447975777666',background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR,font=('Courier',10)).grid(row=0,column=0,columnspan=2)
phone_number_label = Label(frame, text='Phone Number: ',font=('Courier',15), background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=1, column=0)
phone_number_entry = Entry(frame, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, width=60)
phone_number_entry.grid(row=1, column=1)
Label(frame, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=2)
button = Button(frame, text='Locate', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, font=('Courier',15), command=track_number)
button.grid(row=3, column=0, columnspan=2)
Label(frame, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=4)
phone_country_label = Label(frame, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, font=('Courier',10))
company_country_label = Label(frame, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, font=('Courier',10))
Label(frame, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR).grid(row=6)

window.mainloop()
#!/usr/bin/env python3.6
from tkinter import *
from tkinter.filedialog import askopenfilename
import iCalSalad

def main():
	file_path = ["", ""]

	window = Tk()
	window.title("salad.nu -> ical")
	window.geometry("300x300")

	file_entry = Label(text="csv file")
	file_entry.pack(fill=X)

	file_entry_button = Button(
		window,
		text="Select File to convert",
		width=15, 
		height=1,
		command = lambda: get_file_path(file_entry, file_path)
	)
	file_entry_button.pack()

	go_button = Button(
		window,
		text="Convert!!",
		width=10,
		height=1,
		command= lambda:convert(file_entry, file_path)
	)
	go_button.pack()

	window.mainloop()

def convert(button, file_path):
	button.config(text="Converting")
	iCalSalad.convert(file_path[0], file_path[1])
	button.config(text="Converted")

def get_file_path(entry_field, file_path):
	path = askopenfilename(title = "Select csv",filetypes = (("csv files","*.csv"),("all files","*.*")))

	if path is not None:
		o = path.rsplit("/", 1)
		file_path[0] = path
		file_path[1] = o[0]+"/nu_calendar.ics"

		entry_field.config(text=o[1])


if __name__ == "__main__":
    main()
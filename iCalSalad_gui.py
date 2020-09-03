from tkinter import Tk, Label, StringVar, Button, X
from tkinter.filedialog import askopenfilename
import iCalSalad

def main():
	file_path = ["", ""]

	window = Tk()
	window.title("salad.nu -> ical")
	window.geometry("300x300")

	file_entry = Label(text="csv file", font="helvetica 14",)
	file_entry.pack(fill=X)

	file_entry_button = Button(
		window,
		text="Select File to convert",
		font="helvetica 14",
		width=15, 
		height=1,
		command = lambda: get_file_path(file_entry, file_path)
	)
	file_entry_button.pack()

	status_text = StringVar()

	go_button = Button(
		window,
		text="Convert",
		font="helvetica 14",
		width=10,
		height=1,
		command= lambda:convert(status_text, file_path)
	)
	go_button.pack()

	status_section = Label(
		textvariable=status_text, 
		font="helvetica 12",
		wraplength=300,
		justify="center",

	)
	status_section.pack()

	window.mainloop()

def add_to_status(status_text, message):
	t = message + "\n" + status_text.get()
	status_text.set(t)

def convert(status_text, file_path):
	add_to_status(status_text, "Converting")
	iCalSalad.convert(file_path[0], file_path[1])
	add_to_status(status_text, f"Converted, saved to {file_path[1]}")

def get_file_path(entry_field, file_path):
	path = askopenfilename(title = "Select csv",filetypes = (("csv files","*.csv"),("all files","*.*")))

	if path is not None:
		o = path.rsplit("/", 1)
		file_path[0] = path
		file_path[1] = o[0]+"/nu_calendar.ics"

		entry_field.config(text=o[1])


if __name__ == "__main__":
    main()
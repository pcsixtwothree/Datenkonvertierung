from tkinter import Tk, simpledialog

root = Tk()
root.withdraw()

user_input = simpledialog.askstring("Input", "Benutzer eintragen:")
print(user_input)
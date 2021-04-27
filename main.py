from tkinter import *

def button_clicked():
    km = round(float(miles_input.get()) * 1.609344)
    km_output.delete(0, END)
    km_output.insert(0, km)

# Set up the screen
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=220, height=100)

# Label
miles_input = Entry(width=10)
miles_input.grid(row=0, column=2)

my_label = Label(text="Miles", font=("Arial", 12))
my_label.grid(row=0, column=3)

my_label = Label(text="is equal to", font=("Arial", 12))
my_label.grid(row=1, column=1)

km_output = Entry(width=10)
km_output.insert(END, string="0")
km_output.grid(row=1, column=2)

my_label = Label(text="Km", font=("Arial", 12))
my_label.grid(row=1, column=3)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

window.mainloop()
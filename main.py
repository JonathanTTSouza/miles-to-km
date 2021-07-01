from tkinter import *


def action():
    result.config(text=f"{float(miles_input.get()) * 1.689}")


window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=300, height=100)

miles_input = Entry()
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

result = Label(height=1, width=15)
result.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=3, row=1)

button = Button(text="Calculate", command=action)
button.grid(column=1, row=3)

window.mainloop()

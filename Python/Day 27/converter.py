from tkinter import *
window = Tk()
window.title("Mile to Km Converter")


# Declarations
miles = Label(text="Miles")
km = Label(text="Km")
equal_to = Label(text="is equal to")
miles_input = Entry(text="0")
km_output = Label(text="0")
calculate = Button(text="Calculate")


def convert():
    km_output["text"] = round(float(miles_input.get()) * 1.6,3)

miles.grid(column=3, row=1)
km.grid(column=3, row=2)
equal_to.grid(column=1, row=2)
miles_input.grid(column=2, row=1)
km_output.grid(column=2, row=2)
calculate.grid(column=2, row=3)
calculate["command"] = convert

window.mainloop()
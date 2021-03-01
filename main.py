from tkinter import *


def miles_to_km():
    miles = float(data_miles.get())
    km = round(miles*1.60934)
    data_km.config(text=f"{km}")


window = Tk()
window.title("Mile to km Converter")
window.config(padx=20, pady=20)

data_miles = Entry(width=7)
data_miles.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

data_km = Label(text="0")
data_km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
window.mainloop()

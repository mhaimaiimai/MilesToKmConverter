from tkinter import *

def calculate():
    mile_data = mile_input.get()
    km_data = float(mile_data)*(1.60934)
    km_label.config(text=km_data)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)

mile_input = Entry(width=10)
mile_input.insert(END, string="0")
mile_input.grid(row=0, column=1)

mile_unit = Label(text="Miles")
mile_unit.grid(row=0, column=2)

text_equalto = Label(text="is equal to")
text_equalto.grid(row=1, column=0)

km_label = Label(text="0")
km_label.grid(row=1, column=1)

km_unit = Label(text="Km")
km_unit.grid(row=1, column=2)
    
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
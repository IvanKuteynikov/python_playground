import tkinter

window = tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(300, 200)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text='Converter')
my_label.grid(column=0, row=0)


def calculate():
    if radio_state.get() == 1:
        result = round(float(input.get()) * 1.60934, 2)
        my_label.config(text=f"Result is {result}")
    else:
        result = round(float(input.get()) / 1.60934, 2)
        my_label.config(text=f"Result is {result}")

def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Miles to KM", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="KM to Miles", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0, row=2)
radiobutton2.grid(column=0, row=3)

input = tkinter.Entry()
input.grid(column=0, row=1)

button = tkinter.Button(text="Convert", command=calculate)
button.grid(column=1, row=1)



window.mainloop()
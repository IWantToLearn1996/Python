import tkinter

def calculate_button():
    print("Clicked!")
    miles = miles_input.get()
    km = float(miles) * 1.609344
    km_result.config(text=km)


# Window
window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height= 100)
window.config(padx=100, pady=20)

# Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=4, row=2)
miles_label.config(padx=10, pady=10)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 18))
equal_label.grid(column=3, row=3)

km_label = tkinter.Label(text="KM", font=("Arial", 24))
km_label.grid(column=4, row=4)
km_label.config(padx=10, pady=10)

km_result = tkinter.Label(text="0")
km_result.grid(column=3, row=4)

# Button
button = tkinter.Button(text="Calculate", command= calculate_button)
button.grid(column=3, row=5,padx=10, pady=10)
button.config(padx=10, pady=10)

# Entry
miles_input = tkinter.Entry(width=10)
print(miles_input.get())
miles_input.grid(column=3, row=2)



window.mainloop()
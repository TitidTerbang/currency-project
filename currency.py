from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Currency Converter')
root.geometry("500x500")

# create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# create two frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# add our tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# disable 2nd tab
my_notebook.tab(1, state='disabled')

#### currency stuff ####
def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("lmao", "ada ada saja negro")
    else:
        #disabled
        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        #enable tab
        my_notebook.tab(1, state='normal')
        #change tab field
        amount_label.config(text=f'Amount Of {home_entry.get()} To Convert To {conversion_entry.get()}')
        converted_label.config(text=f'Equals This Many {conversion_entry.get()}')
        convert_button.config(text=f'Convert From {home_entry.get()}')

def unlock():
    #enable
        home_entry.config(state='normal')
        conversion_entry.config(state='normal')
        rate_entry.config(state='normal')
        #disable tab
        my_notebook.tab(1, state='disabled')

home = LabelFrame(currency_frame, text="currency")
home.pack(pady=20)

#home entry box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# conversion currency frame
conversion = LabelFrame(currency_frame, text="Conversion")
conversion.pack(pady=20)

#convert to label
conversion_label = Label(conversion, text="Currency To Convert To....")
conversion_label.pack(pady=10)

#convert to entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(padx=10, pady=10)

#label
rate_label = Label(conversion, text="Current Conversion Rate..")
rate_label.pack(pady=10)

#rate to entry
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(padx=10, pady=10)

# button button
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# create button
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

#### conversion stuff ####
def convert():
    #clear entry
    converted_entry.delete(0, END)
    #convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    #convert two decimal
    conversion = round(conversion, 2)
    # add comas
    conversion = '{:,}'.format(conversion)
    #update entry box
    converted_entry.insert(0, f'${conversion}')

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text="Amount To Convers")
amount_label.pack(pady=20)

# entry box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(padx=10, pady=10)

# Convert button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# equals frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

# converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

#clear button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# fake label for spacing
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()

root.mainloop()
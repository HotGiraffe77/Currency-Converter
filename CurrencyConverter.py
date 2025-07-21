import random
import tkinter as tk

EXCHANGE_RATE = 0.005

def convert():
    try:
        yen = float(entry_yen.get())
        gbp = yen * EXCHANGE_RATE
        label_result.config(text=f"{gbp:.2f} GBP")
    except ValueError:
        label_result.config(text="Invalid Input...")


root = tk.Tk()
root.title("Currency Converter")
root.geometry("900x600")

tk.Label(root, text="JPY --> GBP").pack(pady=50)
entry_yen = tk.Entry(root)
entry_yen.pack()

tk.Button(root, text="Convert to GBP", command=convert).pack(pady=100)

label_result = tk.Label(root, text="Result will appear here...")
label_result.pack()

root.mainloop()
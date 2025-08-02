import tkinter as tk
import requests

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = from_var.get()
        to_currency = to_var.get()


        api_key = "0ca2f23e91736262851de6bd"
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
        response = requests.get(url)
        print("Status code:", response.status_code)
        print("Raw Resposne:", response.text)

        data = response.json()

        if data["result"] != "success":
            label_result.config(text="API error: check currency codes or key")
            return

        rate = data["conversion_rate"]
        result = amount * rate
        label_result.config(text=f"{result:.2f} {to_currency}")


    except ValueError:
        label_result.config(text="Invalid amount")
    except Exception as e:
        label_result.config(text=f"Error: {e}")
        print("Exception:", e)

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")

# Input
tk.Label(root, text="Amount:").pack(pady=(10, 0))
entry_amount = tk.Entry(root)
entry_amount.pack()

# From Currency
tk.Label(root, text="From:").pack()
from_var = tk.StringVar(value="USD")
tk.OptionMenu(root, from_var, "USD", "EUR", "GBP", "INR", "JPY", "CAD").pack()

# To Currency
tk.Label(root, text="To:").pack()
to_var = tk.StringVar(value="EUR")
tk.OptionMenu(root, to_var, "USD", "EUR", "GBP", "INR", "JPY", "CAD").pack()

# Convert Button
tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result will appear here")
label_result.pack(pady=(10, 0))

root.mainloop()
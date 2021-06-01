import tkinter as tk
from currency_converter import CurrencyConverter

# Contains messagebox that gives information about the application and gives the user help about using the application
def info():
    msgbox = tk.messagebox.showinfo(title="Information and User Help", message="Welcome to the Currency Converter. This application will allow you to convert from one currency to another, with the currency options and exchange rates provided by the European Central Bank. To convert from one currency to another just enter an amount and select the currency you wish to convert from and then select the currency you wish to convert to. You will see the converted result posted in the middle. Thanks for using this application!")
    return msgbox

# Converts currency by taking in user input and selected currency options
def convert_currency():
    amount = entry1.get()
    currency1 = ""
    for i in c.currencies:
        if (i in option1):
            currency1 = i
            break
    currency2 = ""
    for j in c.currencies:
        if (j in option2):
            currency2 = j
            break
    converted = round(c.convert(amount, currency1, currency2), 2)
    label.config(text=converted)


# Build window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x200")

c = CurrencyConverter()

# Main currency options taken from European Central Bank
curr_options = ["United States Dollar (USD)", 
                "Euro (EUR)", 
                "British Pound (GBP)", 
                "Chinese Yuan (CNY)", 
                "Japanese Yen (JPY)", 
                "Canadian Dollar (CAD)", 
                "Australian Dollar (AUD)",
                "Hong Kong Dollar (HKD)",
                "South Korean Won (KRW)",
                "Israeli New Shekel (ILS)",
                "Polish Zloty (PLN)",
                "Danish Krone (DKK)",
                "Hungarian Forint (HUF)",
                "Indoneasian Rupiah (IDR)",
                "Russian Ruble (RUB)",
                "Romanian Leu (RON)",
                "Czech Koruna (CZK)",
                "Croatian Kuna (HRK)",
                "Thai Baht (THB)",
                "Romanian New Leu (RON)",
                "Philippine Peso (PHP)",
                "South African Rand (ZAR)",
                "Cypriot Pound (CYP)",
                "Maltese Lira (MTL)",
                "Indian Rupee (INR)",
                "Singapore Dollar (SGD)",
                "Swedish Krona (SEK)",
                "Latvian Lats (LVL)",
                "Malaysian Ringgit (MYR)",
                "Swiss Franc (CHF)",
                "Slovak Koruna (SKK)",
                "Estonian Kroon (EEK)",
                "Old Turkish Lira (TRL)",
                "Brazilian Real (BRL)",
                "Slovenian Tolar (SIT)",
                "Mexican Peso (MXN)",
                "Bulgarian Lev (BGN)",
                "Turkish Lira (TRY)",
                "Norwegian Krone (NOK)",
                "Icelandic Krona (ISK)",
                "Lithuanian Litas (LTL)",
                "New Zealand Dollar (NZD)",
                ]

# Create first entry bar and dropdown menu for current currency
default_amount = tk.DoubleVar()
default_amount.set(0.00)
entry1 = tk.Entry(root, textvariable=default_amount)
entry1.pack()
amount = entry1.get()

selected_option1 = tk.StringVar()
selected_option1.set("United States Dollar (USD)")
curr_options = sorted(curr_options)
drop1 = tk.OptionMenu(root, selected_option1, *curr_options)
drop1.pack()
option1 = selected_option1.get()

# Create label that displays the answer
label = tk.Label(root)
label.pack()
converted = amount
label['text'] = converted

# Create seond entry bar and dropdown menu for currency user wants to convert to
selected_option2 = tk.StringVar()
selected_option2.set("Euro (EUR)")
drop2 = tk.OptionMenu(root, selected_option2, *curr_options)
drop2.pack()
option2 = selected_option2.get()

# Convert button when clicked converts the currency
convert_button = tk.Button(root,text="Convert", command=convert_currency)
convert_button.pack()

info_button = tk.Button(root,text="Info and Help", command=info)
info_button.pack()

root.mainloop()
    

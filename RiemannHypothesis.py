import math
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar

def zeta_function(s, terms=1000):
    result = 0.0
    for n in range(1, terms + 1):
        result += 1.0 / (n ** s)
    return result

def calculate_zeta():
    s_value = float(entry_s.get())
    result = zeta_function(s_value)
    result_label.config(text=f'Zeta({s_value}) = {result}')

# Creare main window
window = tk.Tk()
window.title("Riemann Hypothesis Calculator")

# Create and sort element for window
label_s = Label(window, text="S Value:")
label_s.pack(pady=10)

entry_s = Entry(window)
entry_s.pack(pady=10)

calculate_button = Button(window, text="Calcular", command=calculate_zeta)
calculate_button.pack(pady=10)

result_label = Label(window, text="")
result_label.pack(pady=10)

# Execute app
window.mainloop()

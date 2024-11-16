import tkinter as tk

def convert_length():
    try:
        length = float(length_entry.get())
        from_unit = from_unit_entry.get().strip().lower()
        to_unit = to_unit_entry.get().strip().lower()

        conversion_factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144
        }

        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            result_label.config(text="Invalid unit! Use m, km, cm, mm, in, ft, or yd.")
            return

        length_in_meters = length / conversion_factors[from_unit]

        result = length_in_meters * conversion_factors[to_unit]

        result_label.config(text=f"Result: {result:.2f} {to_unit.upper()}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid number.")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x250")

length_label = tk.Label(root, text="Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

from_unit_label = tk.Label(root, text="From Unit (m, km, cm, mm, in, ft, yd):")
from_unit_label.pack(pady=5)
from_unit_entry = tk.Entry(root)
from_unit_entry.pack(pady=5)

to_unit_label = tk.Label(root, text="To Unit (m, km, cm, mm, in, ft, yd):")
to_unit_label.pack(pady=5)
to_unit_entry = tk.Entry(root)
to_unit_entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_length)
convert_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
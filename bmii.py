import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Please enter valid positive values for weight and height.")
            return
        
        bmi = weight / (height ** 2)
        
        bmi_result_label.config(text=f"BMI: {bmi:.2f}")
        interpretation = interpret_bmi(bmi)
        interpretation_label.config(text=f"Interpretation: {interpretation}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numerical values for weight and height.")

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

root = tk.Tk()
root.title("BMI Calculator")

root.geometry("400x300")

weight_label = tk.Label(root, text="Enter weight (kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Enter height (m):")
height_label.pack(pady=5)

height_entry = tk.Entry(root)
height_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

bmi_result_label = tk.Label(root, text="BMI: ")
bmi_result_label.pack(pady=5)

interpretation_label = tk.Label(root, text="Interpretation: ")
interpretation_label.pack(pady=5)

root.mainloop()
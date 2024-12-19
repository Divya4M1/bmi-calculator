import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get values from input fields
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # Validate input
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Please enter valid positive values for weight and height.")
            return
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Display the result
        bmi_result_label.config(text=f"BMI: {bmi:.2f}")
        interpretation = interpret_bmi(bmi)
        interpretation_label.config(text=f"Interpretation: {interpretation}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numerical values for weight and height.")

# Function to interpret BMI result
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Set window size
root.geometry("400x300")

# Create widgets (labels, entry fields, buttons)
weight_label = tk.Label(root, text="Enter weight (kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Enter height (m):")
height_label.pack(pady=5)

height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Labels to display results
bmi_result_label = tk.Label(root, text="BMI: ")
bmi_result_label.pack(pady=5)

interpretation_label = tk.Label(root, text="Interpretation: ")
interpretation_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
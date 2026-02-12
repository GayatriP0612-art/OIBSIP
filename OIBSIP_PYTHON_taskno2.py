import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# File for history
HISTORY_FILE = "bmi_history.csv"

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        if weight <= 0 or height_cm <= 0:
            raise ValueError
        if not (100 <= height_cm <= 250):  # Validation for cm range
            raise ValueError("Height must be between 100 and 250 cm.")

        height_m = height_cm / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        category = get_bmi_category(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

        # Save to history (store height in cm)
        save_to_history(weight, height_cm, bmi, category)
    except ValueError as e:
        messagebox.showerror("Error", str(e) or "Please enter valid positive numbers for weight and height.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_to_history(weight, height_cm, bmi, category):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    data = [timestamp, weight, height_cm, bmi, category]

    # Create file with headers if it doesn't exist
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Weight (kg)", "Height (cm)", "BMI", "Category"])  # Updated header

    with open(HISTORY_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def view_history():
    if not os.path.exists(HISTORY_FILE):
        messagebox.showinfo("History", "No history yet. Calculate some BMIs!")
        return

    history_window = tk.Toplevel()
    history_window.title("BMI History")
    history_window.geometry("600x400")

    # Text widget for table
    text = tk.Text(history_window, wrap=tk.NONE)
    text.pack(fill=tk.BOTH, expand=True)

    with open(HISTORY_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            text.insert(tk.END, line)

    # Graph button
    graph_btn = tk.Button(history_window, text="View Trend Graph", command=show_graph)
    graph_btn.pack(pady=10)

def show_graph():
    if not os.path.exists(HISTORY_FILE):
        messagebox.showerror("Error", "No data for graph.")
        return

    dates, bmis = [], []
    with open(HISTORY_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            dates.append(row[0])
            bmis.append(float(row[3]))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(dates, bmis, marker='o', color='blue')
    ax.set_title("BMI Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("BMI")
    ax.grid(True)
    plt.xticks(rotation=45)

    # Embed in Tkinter window
    graph_window = tk.Toplevel()
    graph_window.title("BMI Graph")
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Main GUI
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root, width=20)
weight_entry.pack()

tk.Label(root, text="Height (cm):").pack(pady=5)  # Updated label
height_entry = tk.Entry(root, width=20)
height_entry.pack()

calc_btn = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="green", fg="white", font=("Arial", 12))
calc_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

tk.Button(root, text="View History", command=view_history, bg="blue", fg="white").pack(pady=10)
tk.Button(root, text="Clear History", command=lambda: os.remove(HISTORY_FILE) if os.path.exists(HISTORY_FILE) else None).pack(pady=5)

root.mainloop()
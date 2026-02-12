import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_spinbox.get())
        if length < 8:
            raise ValueError("Length must be at least 8.")

        min_letters = int(min_letters_spinbox.get())
        min_numbers = int(min_numbers_spinbox.get())
        min_symbols = int(min_symbols_spinbox.get())

        if min_letters + min_numbers + min_symbols > length:
            raise ValueError("Minimum requirements exceed total length.")

        exclude = exclude_entry.get().strip()

        # Build char sets
        letters = [c for c in string.ascii_letters if c not in exclude]
        numbers = [c for c in string.digits if c not in exclude]
        symbols = [c for c in string.punctuation if c not in exclude]

        # Enforce mins by adding required first
        password_list = []
        password_list.extend(random.sample(letters, min_letters) if min_letters else [])
        password_list.extend(random.sample(numbers, min_numbers) if min_numbers else [])
        password_list.extend(random.sample(symbols, min_symbols) if min_symbols else [])

        # Fill remaining with random from selected sets
        char_set = []
        if use_letters_var.get(): char_set.extend(letters)
        if use_numbers_var.get(): char_set.extend(numbers)
        if use_symbols_var.get(): char_set.extend(symbols)

        if not char_set:
            raise ValueError("At least one character type must be selected.")

        remaining = length - len(password_list)
        password_list.extend(random.choice(char_set) for _ in range(remaining))

        # Shuffle for randomness
        random.shuffle(password_list)
        password = ''.join(password_list)

        result_label.config(text=f"Password: {password}")
        copy_btn.config(state=tk.NORMAL)  # Enable copy
        global current_password
        current_password = password
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    pyperclip.copy(current_password)
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Main GUI
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x450")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length
tk.Label(root, text="Length (min 8):").pack()
length_spinbox = tk.Spinbox(root, from_=8, to=50, width=5)
length_spinbox.pack(pady=5)

# Char types
use_letters_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Letters", variable=use_letters_var).pack(anchor=tk.W)
tk.Label(root, text="  Min Letters:").pack(anchor=tk.W, padx=20)
min_letters_spinbox = tk.Spinbox(root, from_=0, to=10, width=5)
min_letters_spinbox.pack(anchor=tk.W, padx=20, pady=2)

use_numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=use_numbers_var).pack(anchor=tk.W)
tk.Label(root, text="  Min Numbers:").pack(anchor=tk.W, padx=20)
min_numbers_spinbox = tk.Spinbox(root, from_=0, to=10, width=5)
min_numbers_spinbox.pack(anchor=tk.W, padx=20, pady=2)

use_symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols_var).pack(anchor=tk.W)
tk.Label(root, text="  Min Symbols:").pack(anchor=tk.W, padx=20)
min_symbols_spinbox = tk.Spinbox(root, from_=0, to=10, width=5)
min_symbols_spinbox.pack(anchor=tk.W, padx=20, pady=2)

# Exclude chars
tk.Label(root, text="Exclude Characters (e.g., oO0):").pack(pady=5)
exclude_entry = tk.Entry(root, width=30)
exclude_entry.pack()

# Buttons
gen_btn = tk.Button(root, text="Generate", command=generate_password, bg="green", fg="white")
gen_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED, bg="blue", fg="white")
copy_btn.pack(pady=5)

current_password = ""  # Global for copy

root.mainloop()
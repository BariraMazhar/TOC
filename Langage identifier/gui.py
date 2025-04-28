import tkinter as tk
from tkinter import messagebox
from dfa import LanguageDFA  # Import DFA class from dfa.py

# Function to handle button click
def process_input():
    text = entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text!")
        return

    detected_language = dfa.identify_language(text)
    result_label.config(text=f"Detected Language: {detected_language}", fg=language_colors.get(detected_language, "white"))

# Initialize DFA
dfa = LanguageDFA()

# Color Theme
bg_color = "#1E1E1E"  # Dark background
text_color = "#F8F8F2"  # Light text
button_color = "#61AFEF"  # Stylish button color
entry_bg = "#282C34"  # Darker input box
entry_fg = "#ABB2BF"  # Light gray text
language_colors = {
    "English": "#98C379",  # Green
    "Spanish": "#E5C07B",  # Yellow
    "French": "#E06C75"  # Red
}

# Create GUI window
root = tk.Tk()
root.title("🌍 Language Identifier (DFA)")
root.geometry("450x300")
root.configure(bg=bg_color)

# Title Label
tk.Label(root, text="Language Identifier", font=("Arial", 18, "bold"), bg=bg_color, fg=text_color).pack(pady=10)

# Entry Box
entry = tk.Entry(root, width=40, font=("Arial", 14), bg=entry_bg, fg=entry_fg, insertbackground="white")
entry.pack(pady=10, padx=20, ipady=5)

# Detect Button
detect_button = tk.Button(root, text="🔍 Detect Language", font=("Arial", 12, "bold"), bg=button_color, fg="white", padx=10, pady=5, command=process_input, relief="flat", cursor="hand2")
detect_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Detected Language: ", font=("Arial", 14, "bold"), bg=bg_color, fg=text_color)
result_label.pack(pady=10)

# Run the GUI
root.mainloop()

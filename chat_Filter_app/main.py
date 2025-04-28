import tkinter as tk
from tkinter import messagebox

# DFA simulation for offensive words
def is_offensive(word):
    word = word.lower()
    
    # DFA for 'bad'
    if word == "bad":
        return True
    # DFA for 'dumb'
    if word == "dumb":
        return True
    # DFA for 'ugly'
    if word == "ugly":
        return True
    return False

def check_message():
    # Clear previous output
    output_text.delete('1.0', tk.END)
    
    message = input_entry.get()
    words = message.split()

    for word in words:
        if is_offensive(word):
            # Highlight offensive word
            output_text.insert(tk.END, word + " ", "offensive")
        else:
            output_text.insert(tk.END, word + " ")

# GUI Window
root = tk.Tk()
root.title("Chat Filter Simulator (DFA Based)")
root.geometry("600x400")
root.config(bg="#f0f8ff")

# Heading
heading = tk.Label(root, text="🚨 Chat Filter Using DFA (TOC Project)", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
heading.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter your chat message:", font=("Arial", 12), bg="#f0f8ff")
input_label.pack(side=tk.LEFT, padx=5)

input_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
input_entry.pack(side=tk.LEFT, padx=5)

# Check Button
check_button = tk.Button(root, text="Check Offensive Words", font=("Arial", 12, "bold"), bg="#007acc", fg="white", command=check_message)
check_button.pack(pady=10)

output_frame = tk.Frame(root, bg="#f0f8ff")
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Processed Chat:", font=("Arial", 12), bg="#f0f8ff")
output_label.pack()

output_text = tk.Text(output_frame, width=70, height=10, font=("Arial", 12))
output_text.pack()

output_text.tag_config("offensive", foreground="red", font=("Arial", 12, "bold"))

root.mainloop()

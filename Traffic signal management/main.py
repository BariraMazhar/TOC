import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Traffic Light Management System (DFA Simulation)")
root.geometry("300x500")
root.resizable(False, False)

# Canvas for drawing lights
canvas = tk.Canvas(root, width=200, height=400, bg='white')
canvas.pack(pady=20)

# Create traffic lights (circles)
red_light = canvas.create_oval(50, 30, 150, 130, fill="grey")
yellow_light = canvas.create_oval(50, 150, 150, 250, fill="grey")
green_light = canvas.create_oval(50, 270, 150, 370, fill="grey")

# DFA State
current_state = "Red"

# Function to simulate DFA
def traffic_light_cycle():
    global current_state
    
    if current_state == "Red":
        # Red ON
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="grey")
        canvas.itemconfig(green_light, fill="grey")
        current_state = "Green"
        root.after(4000, traffic_light_cycle)  # Red for 4 seconds
    
    elif current_state == "Green":
        # Green ON
        canvas.itemconfig(red_light, fill="grey")
        canvas.itemconfig(yellow_light, fill="grey")
        canvas.itemconfig(green_light, fill="green")
        current_state = "Yellow"
        root.after(3000, traffic_light_cycle)  # Green for 3 seconds
    
    elif current_state == "Yellow":
        # Yellow ON
        canvas.itemconfig(red_light, fill="grey")
        canvas.itemconfig(yellow_light, fill="yellow")
        canvas.itemconfig(green_light, fill="grey")
        current_state = "Red"
        root.after(1000, traffic_light_cycle)  # Yellow for 1 second

# Start the cycle
traffic_light_cycle()

# Run the GUI
root.mainloop()

import pyautogui
import tempfile
import tkinter as tk

# Create a temporary file to store the cursor coordinates
temp_file = tempfile.NamedTemporaryFile()

# Create a small window to display the cursor coordinates
window = tk.Tk()
window.geometry("200x50")
window.title("Mouse Tracker")

# Create a label to display the cursor coordinates
label = tk.Label(window, text="")
label.pack()

# Function to update the label with the current cursor coordinates
def update_label():
    x, y = pyautogui.position()
    label.config(text=f"({x}, {y})")
    window.after(100, update_label)

# Start updating the label
update_label()

print("Press the delete key to stop tracking the cursor.")

# Function to close the window and delete the temporary file
def close_window(event):
    window.destroy()
    temp_file.close()

# Bind the delete key to the close_window function
window.bind("<Delete>", close_window)

window.mainloop()

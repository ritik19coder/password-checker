import re
import tkinter as tk
from tkinter import messagebox
import os

# Function to check the strength of a password
def check_password_strength(password):
    # Criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # List of common passwords to avoid
    common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", "password1"]
    common_password_criteria = password not in common_passwords

    # Check each criteria and calculate score
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    if common_password_criteria:
        score += 1

    # Provide feedback based on the score
    if score == 6:
        return "Strong Password! All criteria met."
    elif 4 <= score < 6:
        return "Moderate Password. Try adding more variety."
    else:
        return "Weak Password. Improve it by adding uppercase letters, digits, or special characters, and make it longer."

# Function triggered when the user clicks the "Check Password" button
def on_check_password():
    password = password_entry.get()  # Get the entered password
    result = check_password_strength(password)  # Check its strength
    messagebox.showinfo("Password Strength", result)  # Show the result in a message box

# Function to toggle password visibility
def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show="*")
        eye_button.config(image=closed_eye_image)  # Set to closed eye
    else:
        password_entry.config(show="")
        eye_button.config(image=open_eye_image)  # Set to open eye

# Creating the GUI
def create_gui():
    # Initialize the root window
    root = tk.Tk()
    root.title("Password Strength Checker")

    # Set window size
    root.geometry("400x200")

    # Label for instruction
    label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
    label.pack(pady=10)

    # Frame for the password entry and eye button
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Entry widget to take password input
    global password_entry
    password_entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
    password_entry.pack(side=tk.LEFT)  # Add the entry to the left side of the frame

    # Button to toggle password visibility (eye button)
    global eye_button, open_eye_image, closed_eye_image

    # Specify the paths for the eye icon images
    image_dir = "images"  # Update this to the correct path if necessary
    open_eye_path = os.path.join(image_dir, "D:\Porjects\Password strength checker tool\images\open_eye.png")  # Path for open eye image
    closed_eye_path = os.path.join(image_dir, "D:\Porjects\Password strength checker tool\images\closed_eye.png")  # Path for closed eye image

    # Load eye icon images
    open_eye_image = tk.PhotoImage(file=open_eye_path)
    closed_eye_image = tk.PhotoImage(file=closed_eye_path)

    # By default, the password is hidden, so the button shows a closed eye
    eye_button = tk.Button(frame, image=closed_eye_image, command=toggle_password_visibility)
    eye_button.pack(side=tk.LEFT, padx=(10,0))  # Add the eye button to the right side of the entry

    # Button to trigger password check
    check_button = tk.Button(root, text="Check Password", command=on_check_password, font=("Arial", 12))
    check_button.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()

# Run the GUI application
if __name__ == "__main__":
    create_gui()

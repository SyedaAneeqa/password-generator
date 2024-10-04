import tkinter as tk
import random


def generate_password():
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_characters = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
   
    length = int(entry_length.get())
    
    
    all_characters = list(alphabets + alphabets.upper() + numbers + special_characters)
    
 
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
   
    password_label.config(text=password)


root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg="purple")


title_label = tk.Label(root, text="                   WELCOME TO MY LITTLE PASSWORD GENERATOR                   ", font=("Helvetica", 14), pady=10)
title_label.configure(bg="pink")
title_label.pack()


label_length = tk.Label(root, text="Enter how many characters you want in your password", font=("Helvetica", 12))
label_length.configure(bg="pink")
label_length.pack(pady=5)


entry_length = tk.Entry(root)
entry_length.configure(bg="grey")
entry_length.pack(pady=5)


generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_button.configure(bg="light grey")
generate_button.pack(pady=10)


password_label = tk.Label(root, text="Your generated password will appear here", font=("Helvetica", 12), fg="red")
password_label.configure(bg="pink")
password_label.pack(pady=10)


root.mainloop()

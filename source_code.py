from tkinter import *
import pyperclip
import random

root = Tk()
root.title("Password Generator")
root.geometry("350x200")

passwordString = StringVar()
passwordLength = IntVar()

passwordLength.set(0)

def generate():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    password = ""

    for x in range(passwordLength.get()):
        password = password + random.choice(characters)
    passwordString.set(password)

def copytoclipboard():
    random_password = passwordString.get()
    pyperclip.copy(random_password)

Label(root, text="Secure Password Generator", font="Helvetica 16 bold").pack()

Label(root, text="Enter Password Length").pack(pady=3)

Entry(root, textvariable=passwordLength).pack(pady=3)

Button(root, text="Generate Secure Password", command=generate).pack(pady=7)

Entry(root, textvariable=passwordString).pack(pady=3)

Button(root, text="Copy to Clipboard", command=copytoclipboard).pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class Password_generator_app:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator application")
        #password length label post
        self.lengthLabel = tk.Label(master, text = "Password Length: ")
        self.lengthLabel.grid(row=0, column=0, sticky="w", pady=5, padx=15)
        #password entry length limit
        self.lengthEntry =tk.Entry(master, width=12)
        self.lengthEntry.grid(row=0, column=1, pady=7, padx=15)
        self.lengthEntry.insert(0, "15")
        #prompt user to enter password with at lease an uppercase letter    
        self.uppercaseVar = tk.IntVar()
        self.uppercaseCheck = tk.Checkbutton(master, text="Include Uppercase Letters in your password", variable= self.uppercaseVar)
        self.uppercaseCheck.grid(row=1, column=0, columnspan=2, sticky='w', pady=5, padx=10)
        self.uppercaseCheck.select()
        #prompt user to enter password with at least one lowercase letter 
        self.lowercaseVar = tk.IntVar()
        self.lowercaseCheck = tk.Checkbutton(master, text="Include lowercase letters in your password", variable= self.lowercaseVar)
        self.lowercaseCheck.grid(row=1, column=0, columnspan=2, sticky='w', pady=5, padx= 10 )
        self.lowercaseCheck.select()
        #prompt user to enter at least one digit charactor
        self.digitsVar = tk.IntVar()
        self.digitsCheck = tk.Checkbutton(master, text="Include digits in your password", variable = self.digitsVar)
        self.digitsCheck.grid(row=3, column=0, columnspan=2, sticky='w', padx=10, pady=5)
        self.digitsCheck.select()
        #allows user to be able to see button and click
        self.generateButton = tk.Button(master, text="Click to generate password", command=self.generatePassword)
        self.generateButton.grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        #prompts app to display generated password
        self.passwordLabel = tk.Label(master, text="Generated Password: ")
        self.passwordLabel.grid(row=5, column=0, sticky='w', padx=10, pady=5)
        #displays password on a specified space
        self.passwordDisplay = tk.Entry(master, width=30, state="readonly") #this limits the user from editing the password.
        self.passwordDisplay.grid(row=6, column=0, columnspan=2, padx=10,pady=5)

        self.copyButton = tk.Button(master, text="Copy password to clipboard", command=self.copyClipboard)
        self.copyButton.grid(row=7, column=0, columnspan=2, pady=5, padx=10)
    #implement method to generate password randomly
    def generatePassword(self):
        length = int(self.lengthEntry.get())
        if length < 0:
            #if user changes the limit to less than zero then show error message
            messagebox.showerror("Error", "Password length should be greater than 0")
            return
        
        includeUppercase = bool(self.uppercaseVar.get())
        includeLowercase = bool(self.lowercaseVar.get())
        includeDigits = bool(self.digitsVar.get())

        if not (includeUppercase or includeUppercase or includeDigits):
            messagebox.showerror("Error", "Allocate at least one character type")
            return
        
        characters = ''
        if includeUppercase:
            characters += string.ascii_uppercase
        if includeLowercase:
            characters += string.ascii_lowercase
        if includeDigits:
            characters += string.digits

        
        generatedPassword = ''.join(random.choice(characters) for _ in range(length))
        self.passwordDisplay.config(state='normal')
        self.passwordDisplay.delete(0, tk.END) #allows user to delete password if needed to
        self.passwordDisplay.insert(0, generatedPassword) #allows user to generate and insert in password
        self.passwordDisplay.config(state='readonly') #allows user to only read password and not write it.add()

    def copyClipboard(self):
        password = self.passwordDisplay.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Password copied!", "Password has been copied to clipboard!")
        else:
            messagebox.showwarning("Empty", "Nothing to copy!")
#main function to run application
def main():
    root = tk.Tk()
    app = Password_generator_app(root)
    root.mainloop()

if __name__ == "__main__":
    main()

        




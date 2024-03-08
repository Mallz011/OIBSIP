import tkinter as tk
import sqlite3
from tkinter import messagebox

class BMICalculator:
    def __init__(self, master):
        #title setup 
        self.master = master
        self.master.title("BMI Calculator")

        #weight label setup 
        self.label_weight  = tk.Label(master, text = "Enter your weight (kg): ")
        self.label_weight.grid(row=0, column=0, padx=10, pady=10)
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)
        
        #height label setup
        self.label_height = tk.Label(master, text="Enter your height (m): ")
        self.label_height.grid(row=1, column=0, padx=10, pady=10)
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)
        
        #click button to calculte button
        self.calculate_button = tk.Button(master, text ="Calculate BMI", command = self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0,columnspan=2, padx=10, pady =10)
        
        
        #results block
        self.result_label = tk.Label(master, text = " ")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10)

        #view history
        self.view_history_button = tk.Button(master, text="View History", command = self.view_history)
        self.view_history_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        #create table using sqlite3
        self.conn  = sqlite3.connect('BMI_data.db')
        self.con = self.conn.cursor()

        self.con.execute('''CREATE TABLE If NOT EXISTS BMI(
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                             weight REAL,
                          height REAL,
                          BMI REAL)''')
        self.conn.commit()
    #method used to calculate BMI 
    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            BMI = weight/(height ** 2)
            self.result_label.config(text = f"BMI: {BMI: .2f}")

            
            #save data inputed by user
            self.con.execute("insert INTO BMI (weight, height, BMI) VALUES (?, ?, ?)", (weight, height, BMI))
            self.conn.commit()

        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid input for height and weight.")
    #method used to view calculated BMI 
    def view_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("BMI History")

        #create listbox to display history
        history_listbox = tk.Listbox(history_window, width= 50)
        history_listbox.pack(padx=10, pady=10)

        #fetch and display historical BMI data
        self.con.execute("SELECT * FROM BMI")
        data = self.con.fetchall()
        for row in data:
            history_listbox.insert(tk.END, f"Weight: {row[1]} kg, Height: {row[2]} m, BMI: {row[3]: 2f}")
    #method used for closing/deleting history
    def __del__(self):
        self.con.close()
             

def main():
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()




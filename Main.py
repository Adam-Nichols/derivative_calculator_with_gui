from sympy import diff, Symbol
import tkinter as tk


class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Derivative Calculaor")

        self.label = tk.Label(master, text="This program calculates derivatives of functions")
        self.label.pack()

        self.greet_button = tk.Button(master, text='Greet', command=self.greet)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text='Close', command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings")


root = tk.Tk()
my_gui = MainGUI(root)
root.mainloop()

function = input("Please enter the function you would like to differentiate: ")
derivative_variable = Symbol(input("Which function would you like to differentiate with respect to? "))

first_derivative = diff(function, derivative_variable)
first_derivative.doit()

print(first_derivative)

# Import Library
import tkinter as tk

#Main Window
root = tk.Tk()
root.title("My Calculator")
root.geometry("328x454")
root.resizable(0, 1)
clicon = tk.PhotoImage(file="F:\Python Projects\Visual Calculator File\calculator.png")
root.iconphoto(True, clicon)

#Input Option
entry = tk.Entry(root, font= ("Arial", 20), borderwidth = 5, relief = "flat", justify = "right")
entry.grid(row = 0, column = 0, columnspan = 4, ipadx = 8, ipady = 15, pady = 10)

#Buttion Click Function
def button_click(item):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END, current + str(item))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

#Butttons Layout
buttons = [("7",1,0), ("8",1,1), ("9",1,2), ("AC",1,3), ("4",2,0), ("5",2,1), ("6",2,2), ("/",2,3),
           ("1",3,0), ("2",3,1), ("3",3,2), ("*",3,3), ("0",4,0), (".",4,1), ("+",4,2), ("-",4,3), ("=", 5, 0)]

#For Loop
for (text, row, column) in buttons:
    if text == "AC":
        tk.Button(root, text = text, width = 5, height = 2, font = ("Arial", 16), command = clear).grid(row=row, column=column, padx = 5, pady = 5)
    elif text == "=":
        tk.Button(root, text="=", width=25, height= 1, font= ("Arial",16), command= equal).grid(row=row, column=column, columnspan= 4, padx= 5, pady = 5)
    else:
        tk.Button(root, text=text, width = 5, height = 2, font = ("Arial",16), command = lambda t=text: button_click(t)).grid(row=row, column=column, padx=5, pady=5)

#Always Run The Code
root.mainloop()
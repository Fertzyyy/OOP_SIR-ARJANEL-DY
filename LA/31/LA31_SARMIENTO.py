import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg="blue")

name = tk.Entry(root)
name.grid(row=0, column=0, padx=20, pady=0)


frame = tk.Frame(root)
frame.grid(pady = 20)    

def display_text():
    print(name.get())
    
button = tk.Button(root, text="Print", command=display_text)
button.grid(row=0, column=1, padx=20, pady=20)

               
root.mainloop()
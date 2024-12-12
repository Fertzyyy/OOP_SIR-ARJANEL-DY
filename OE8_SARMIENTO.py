import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg="blue")

name = tk.Entry(root)
name.grid(row=0, column=0, padx=20, pady=0)


frame = tk.Frame(root)
frame.grid(pady = 20)    

counter = 1
def display_text():
    global counter
    print(f"{counter}. {name.get()}")
    counter +=1
    
button = tk.Button(root, text="Print", command=display_text)
button.grid(row=0, column=1, padx=0, pady=40)

               
root.mainloop()
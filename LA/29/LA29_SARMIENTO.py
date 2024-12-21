import tkinter as tk

your_name = "DEANGELO JAZZFFER G. SARMIENTO"
your_section = "BSIT -2A"

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")

frame = tk.Frame(root)
frame.pack(pady = 20)

label = tk.Label(frame, text= f"OOP LA#29 {your_name} {your_section}")
label.grid(row=0, column=0, padx=10, pady=10)

"""label2 = tk.Label(root, text="This is a label two")
label2.grid(row=0, column=0, padx=0, pady=0)"""
               
root.mainloop()
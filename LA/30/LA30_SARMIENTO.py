import tkinter as tk

anime_title = "Cowboy Bebop"

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")

frame = tk.Frame(root)
frame.grid(pady = 20)    

counter = 0
def display_text():
    global counter
    print(f"My Favorite anime {anime_title}")
    counter +=1
    
button = tk.Button(root, text="Run", command=display_text)
button.grid(row=0, column=0, padx=20, pady=20)

               
root.mainloop()
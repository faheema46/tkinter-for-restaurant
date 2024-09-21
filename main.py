import tkinter as tk
window=tk.Tk()

window.title("restaurant window")
window.geometry("500x500")

welcome=tk.Label(text="Welcome to our restaurant",fg="black",bg="white")
entry=tk.Entry(fg="black",bg="white",width=50)
button= tk.Button(text="click me",bg="white",fg="black")
welcome.pack()
button.pack()
entry.pack()
window.mainloop()
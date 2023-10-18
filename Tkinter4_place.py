import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Hello, Tkinter!")
label2 = tk.Label(root, text="Goodby, Tkinter!")

# x=20, y=50の座標に配置
label1.place(x=20, y=50)
label2.place(x=50, y=50)

root.mainloop()

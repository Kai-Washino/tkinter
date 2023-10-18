import tkinter as tk 

def on_button_click():
    label.config(text = "ボタンがクリックされました")

root = tk.Tk() 
button = tk.Button(root, text = "クリックしてください", command=on_button_click )
button.pack(side = "top")
label = tk.Label(root, text="こんにちは、Tkinter!") 
label.pack(side = "left")


root.mainloop() # loop開始．

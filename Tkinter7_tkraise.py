import tkinter as tk

def show_frame(frame):
    frame.tkraise()
    print(frame)

root = tk.Tk()

# 初期画面のフレーム
frame1 = tk.Frame(root)
label1 = tk.Label(frame1, text="This is Frame 1")
label1.pack()
button1 = tk.Button(frame1, text="Go to Frame 2", command=lambda: show_frame(frame2))
button1.pack()
frame1.grid(row=0, column=0, sticky="nsew")

# 遷移先のフレーム
frame2 = tk.Frame(root)
label2 = tk.Label(frame2, text="This is Frame 2")
label2.pack()
button2 = tk.Button(frame2, text="Go to Frame 1", command=lambda: show_frame(frame1))
button2.pack()
frame2.grid(row=0, column=0, sticky="nsew")

show_frame(frame1)  # 初期画面としてframe1を表示

root.mainloop()

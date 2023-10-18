import tkinter as tk 

def on_button_click():
    label.config(text = "ボタンがクリックされました")
    entered_text = entry.get()  # テキストボックスに入力されたテキストを取得
    print(entered_text)
    entered_text = text.get("1.0", tk.END)  # Textウィジェットに入力されたテキストを取得
    print(entered_text)

root = tk.Tk() 
button = tk.Button(root, text = "クリックしてください", command=on_button_click )
button.pack(side = "top")
label = tk.Label(root, text="こんにちは、Tkinter!") 
label.pack(side = "left")

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()

#canvasはpackしたあとにも動的に処理できる点がLabelよりも優れている．
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()
canvas.create_rectangle(-120, 25, 100, 75, fill="red")

listbox = tk.Listbox(root)
listbox.pack()
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
selected_item = listbox.curselection()  # 選択された項目を取得

var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="opt1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="opt2")
radio1.pack()
radio2.pack()

var = tk.IntVar()
check = tk.Checkbutton(root, text="Check me", variable=var)
check.pack()


scale = tk.Scale(root, from_=0, to=100)
scale.pack()

# Frameはウィジェットを子として保持できる．FrameはFremaも保持できる．
# packで配置されるFrameは，pack_progate(0)によって，子の大きさに干渉されなくなる．デフォルトはpack_progete(1)で干渉される
frame = tk.Frame(root)
frame.pack_propagate(0)
frame.pack()
label_in_frame = tk.Label(frame, text="Label in Frame")
label_in_frame.grid(row=0, column=0)
label_in_frame.pack()

root.mainloop() # loop開始．

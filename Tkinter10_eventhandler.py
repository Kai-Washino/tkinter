import tkinter as tk
# イベントバインディングは，特定のウィジェットに対しても全体のウィンドウに対しても行うことができる．

def on_canvas_click(event):
    print(f"Canvas clicked at ({event.x}, {event.y})")

def on_key_press(event):
    print(f"Key pressed: {event.char}")

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg='lightgray')
canvas.pack()

# "<Button-1>" は左クリックイベントを意味します
canvas.bind("<Button-1>", on_canvas_click)
root.bind("<Key>", on_key_press)

root.mainloop()

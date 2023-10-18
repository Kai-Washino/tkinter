import tkinter as tk
from tkinter import ttk

root = tk.Tk()


button = tk.Button(root, text="Click Me!", command=lambda: print("Button Clicked!"))
button.pack(pady=20)

available_themes = ttk.Style().theme_names()
print(f"Available Themes: {available_themes}")
ttk.Style().theme_use('clam')

button1 = ttk.Button(root, text="Click Me!", command=lambda: print("Button Clicked!"))
button1.pack(pady=20)

style = ttk.Style()
style.configure("TButton", foreground="red", background="yellow", font=("Arial", 20, "bold"), padding=10)

# カスタムスタイルを適用したButtonウィジェットを作成
button2 = ttk.Button(root, text="Click Me!", style="TButton", command=lambda: print("Button Clicked!"))
button2.pack(pady=20)

root.mainloop()

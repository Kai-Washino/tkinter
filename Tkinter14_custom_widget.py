import tkinter as tk

class CustomWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # ラベルウィジェットの作成と配置
        self.label = tk.Label(self, text="This is a custom widget!")
        self.label.pack()
        
        # ボタンウィジェットの作成と配置
        self.button = tk.Button(self, text="Click me!", command=self.on_button_click)
        self.button.pack()
        
    def on_button_click(self):
        # ボタンがクリックされたときの処理
        print("Button clicked!")

# アプリケーションの作成
root = tk.Tk()

# カスタムウィジェットのインスタンス化と配置
widget = CustomWidget(root)
widget.pack(pady=20)

root.mainloop()

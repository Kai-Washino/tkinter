import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # メインウィンドウを表示しない

# 情報メッセージボックス
messagebox.showinfo("Info", "This is an info message")

# 警告メッセージボックス
messagebox.showwarning("Warning", "This is a warning message")

# エラーメッセージボックス
messagebox.showerror("Error", "This is an error message")

# 確認メッセージボックス（Yes/No）
result = messagebox.askyesno("Confirmation", "Do you want to proceed?")
print(f"User selected: {'Yes' if result else 'No'}")

# ファイルオープンダイアログ
file_path = filedialog.askopenfilename(title="Open a file", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
print(f"Selected file: {file_path}")

# ファイル保存ダイアログ
file_path = filedialog.asksaveasfilename(title="Save a file", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
print(f"File to save: {file_path}")

# ディレクトリ選択ダイアログ
dir_path = filedialog.askdirectory(title="Select a directory")
print(f"Selected directory: {dir_path}")

root.mainloop()

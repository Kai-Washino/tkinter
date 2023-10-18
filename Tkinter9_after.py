import tkinter as tk
    
flag = True
# flag = False
root = tk.Tk()

def update_function():
    global flag
    print("Update!")
    id = root.after(1000, update_function)
    print(flag)
    if(flag):
        root.after_cancel(id)  # スケジュールされたコールバックをキャンセルする
        print("Cancel")
    flag = not flag

id = root.after(1000, update_function)  # 1秒後にupdate_functionを呼び出す

root.mainloop()

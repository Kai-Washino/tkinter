import tkinter as tk
import cv2
from PIL import Image, ImageTk

# カメラから動画をキャプチャする
cap = cv2.VideoCapture(0)

# Tkinterウィンドウを作成する
root = tk.Tk()
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

def update_image():
    # カメラからフレームを読み込む
    ret, frame = cap.read()
    if ret:
        # OpenCVの画像をPIL形式に変換する
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        # PIL形式の画像をTkinterに適した形式に変換する
        photo = ImageTk.PhotoImage(image=image)
        # 画像をCanvas上に表示する
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # 参照を保持することでガベージコレクションを防ぐ
    # 画像を更新する関数を再帰的に呼び出す
    root.after(10, update_image)

# 画像を更新する関数を呼び出す
update_image()
# Tkinterウィンドウを表示する
root.mainloop()

# ウィンドウが閉じられたらカメラを解放する
cap.release()

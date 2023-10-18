import tkinter as tk #まずはtkinterをimport
root = tk.Tk() #tkinterのTkクラスを使用し，主ウィンドウを表示
label = tk.Label(root, text="こんにちは、Tkinter!") #主ウィンドウに対し，tkinterでラベルを付与．ラベルはウィジェット
label.pack() #packはウィジェットをウインドウに配置するためのもの．他には，gridやplaceがある．
root.mainloop() # loop開始．

import tkinter as tk

def new_file():
    print("New File selected")

def open_file():
    print("Open File selected")

def save_file():
    print("Save File selected")

root = tk.Tk()

# Step 1: Create a menu bar
menubar = tk.Menu(root)

# Step 2: Create a File dropdown menu
filemenu = tk.Menu(menubar, tearoff=0)

# Step 3: Add commands to File menu
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

# Step 4: Add File menu to the menu bar
menubar.add_cascade(label="File", menu=filemenu)

# Step 5: Associate the menu bar with the root window
root.config(menu=menubar)

root.mainloop()

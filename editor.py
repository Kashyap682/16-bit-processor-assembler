from tkinter import *
from tkinter import filedialog
import os

def new_file():
    text_info.delete(1.0, END)

def open_file():
    file = filedialog.askopenfile(mode ='r')
    if file is not None:
        content = file.read()
        text_info.delete(1.0, END)
        text_info.insert(END, content)

def save_file():
    file = filedialog.asksaveasfile(mode ='w', defaultextension=".txt")
    if file is not None:
        # slice off the last character from get, as an extra return is added
        content = text_info.get(1.0, END)
        file.write(content)
        file.close()

def save_file_as():
    file = filedialog.asksaveasfile(mode ='w', defaultextension=".txt")
    if file is not None:
        # slice off the last character from get, as an extra return is added
        content = text_info.get(1.0, END)
        file.write(content)
        file.close()

def compile_code():
    os.system("python assembler.py")

def run_code():
    os.system("python sim.py")

root = Tk()
root.geometry("400x400")
root.title("Assembler&Simulator")
root.minsize(height=400, width=400)
root.maxsize(height=400, width=400)

# adding scrollbar
scrollbar = Scrollbar(root)

# packing scrollbar
scrollbar.pack(side=RIGHT, fill=Y)

text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

# configuring the scrollbar
scrollbar.config(command=text_info.yview)

# create a menubar
menu_bar = Menu(root)

# create the file menu
file_menu = Menu(menu_bar, tearoff=0)

# add the new file, open, save, and save as options to the file menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_file_as)

# add the file menu to the menubar
menu_bar.add_cascade(label="File", menu=file_menu)

# create the run menu
run_menu = Menu(menu_bar, tearoff=0)

# add the compile and run options to the run menu
run_menu.add_command(label="Compile", command=compile_code)
run_menu.add_command(label="Run", command=run_code)

# add the run menu to the menubar
menu_bar.add_cascade(label="Run", menu=run_menu)

# display the menu bar
root.config(menu=menu_bar)

root.mainloop()

from tkinter import *

font_size = 16

def new_file():
    print("hey")

    
def save_file():
    print("hey2")

def increse_font_size(event):
    global font_size
    font_size += 2
    update_font()

def decrese_font_size(event):
    global font_size
    font_size = max(2, font_size-2)
    update_font()


def update_font():
    global text, font_size
    custom_font = ("Arial", font_size)
    text.configure(font=custom_font)

root = Tk()
root.title("Text Editor")
root.wm_state('zoomed')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


menu_bar = Menu()
file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(
    label="New",
    accelerator="Ctrl+N",
    command=new_file
)
file_menu.add_command(
    label="Save",
    accelerator="Ctrl+S",
    command=save_file
)

menu_bar.add_cascade(menu=file_menu, label="File")
root.config(menu=menu_bar)

font = ("Arial", font_size)

text = Text(root, font=font)
text.grid(row=0,column=0,sticky="nsew")

root.bind("<Control-plus>", increse_font_size)
root.bind("<Control-minus>", decrese_font_size)

root.mainloop()
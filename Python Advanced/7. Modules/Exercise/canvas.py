from tkinter import *


def create_root():
    root = Tk()

    root.geometry("700x600")
    root.title("GIBINSKi Shop")

    return root


def creat_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame





root = create_root()
frame = creat_frame()

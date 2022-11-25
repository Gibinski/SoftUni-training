from canvas import *


def render_entry():
    register_btn = Button(
        root, 
        text="Register", 
        bg="green", 
        fg="white", 
        borderwidth=0, 
        width=20,
        height=3,
        command=register
    )

    login_btn = Button(
        root, 
        text="Login", 
        bg="blue", 
        fg="white", 
        borderwidth=0, 
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_btn)

def register():
    pass


def login():
    pass
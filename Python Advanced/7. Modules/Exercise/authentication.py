from canvas import *
from json import *
from helpers import clean_screen
from os import path

db_path = path.join("db", "user_information.json")


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
    frame.create_window(350, 320, window=login_btn)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password")

    frame.create_window(200, 50, window=first_nane_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)
    
    registration_btn = Button(
        root, 
        text="Registration", 
        bg="green", 
        fg="white", 
        borderwidth=0, 
        command=registration
    )

    frame.create_window(300, 250, window=registration_btn)
    

def login():
    clean_screen()
    

def registration():
    info_dict = {
        "first_name": first_nane_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "passwor": password_box.get(),
        "products": []
    }

    if check_registration(info_dict):
        with open(db_path, "a") as users_file:
            dump(info_dict, users_file)
            users_file.write("\n")


def check_registration(info: dict):
    for el in list(info.values())[:-1]:
        if el.strip() == "":
            frame.create_text(
                200,
                290, 
                text="We are missing some information, please check your filds!",
                fill="red",
                tags="error"   
            )

            return False

    frame.delete("error")

    info_data = []
    with open(db_path, "r") as user_file:
        for line in user_file:
            info_data.append(loads(line))
    
    for i in range(len(info_data)):
        if info_data[i]["username"] == info["username"]:
            frame.create_text(
                200,
                290, 
                text="Username alredy exist",
                fill="red",
                tags="error"   
            )

    frame.delete("error")

    return True






first_nane_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")

from pathlib import Path
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
sys.path.append(r"C:\Users\osama\Desktop\Symmaiyah\build\Admin_UI")
sys.path.append(r"C:\Users\osama\Desktop\Symmaiyah\build\User_UI")

import HomeAdmin,Home_User

def Show():

    def open_Admin():
        window.destroy()
        HomeAdmin.Show()
    def open_User():
        window.destroy()
        Home_User.Show()
    def handle_login():
        username = entry_1.get()
        if username.lower() == "admin":
            open_Admin()
        else:
            open_User()
    

    window = Tk()

    window.geometry("800x600+350+100")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=r"loginAssets\image_1.png")
    image_1 = canvas.create_image(
        400.0,
        128.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=r"loginAssets\entry_1.png")
    entry_bg_1 = canvas.create_image(
        400.0,
        284.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#CBDEF4",
        fg="#000716",
        highlightthickness=0,
        font=("Inika Bold",12),

    )

    entry_1.place(
        x=246.5,
        y=263.0,
        width=307.0,
        height=41.0
    )

    entry_image_2 = PhotoImage(
        file=r"loginAssets\entry_2.png")
    entry_bg_2 = canvas.create_image(
        400.0,
        379.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#CBDEF4",
        fg="#000716",
        highlightthickness=0,
        show='*',
        font=("Inika Bold",12)
    )
    entry_2.place(
        x=246.5,
        y=358.0,
        width=307.0,
        height=41.0
    )

    canvas.create_text(
        231.0,
        234.0,
        anchor="nw",
        text="Username",
        fill="#022E31",
        font=("Inika Bold", 20 * -1)
    )

    canvas.create_text(
        231.0,
        331.0,
        anchor="nw",
        text="Password",
        fill="#022E31",
        font=("Inika Bold", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=r"loginAssets\button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=handle_login,
        relief="flat",
        background='white'
    )
    button_1.place(
        x=340.0,
        y=485.0,
        width=125.0,
        height=50.0
    )
    window.resizable(False, False)
    window.mainloop()
if __name__ == "__main__":
    Show()
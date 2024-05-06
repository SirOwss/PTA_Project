from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image,ImageTk
import AboutAdmin,ExserciseAdmin,FootAdmin,LegAdmin,SideAdmin,PatientAdmin,HomeAdmin
import sys
sys.path.append(r"C:\Users\osama\Desktop\Symmaiyah\build")

from Primary import Login








def Show():
    def open_Login_Logout():
        window.destroy()
        Login.Show()
    def open_HomePage():
        window.destroy()
        HomeAdmin.Show()
    def open_AboutPage():
        window.destroy()
        AboutAdmin.Show()
    def open_ExsercisePage():
        window.destroy()
        ExserciseAdmin.Show()
    def open_PatinitPage():
        window.destroy()
        PatientAdmin.Show()
    def open_FootPage():
        window.destroy()
        FootAdmin.Show()
    def open_LegPage():
        window.destroy()
        LegAdmin.Show()
    def open_SidePage():
        window.destroy()
        SideAdmin.Show()


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
    button_image_1 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_ExsercisePage,
        relief="flat",
        background='white'
    )
    button_1.place(
        x=277.0,
        y=177.0,
        width=250.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_ExsercisePage,
        relief="flat",
        background='white'
    )
    button_2.place(
        x=277.0,
        y=261.0,
        width=250.0,
        height=55.0
    )

    button_image_3 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=open_ExsercisePage,
        relief="flat",
        background='white'
    )
    button_3.place(
        x=277.0,
        y=342.0,
        width=250.0,
        height=55.0
    )

    image_image_1 = PhotoImage(
        file=r"Admin_UI\assets\frame2\image_1.png")
    image_1 = canvas.create_image(
        54.0,
        49.0,
        image=image_image_1
    )
    ex1_image = Image.open(r"Admin_UI\assets\frame2\ex1.png").resize((100,50),Image.NEAREST)
    image_image_2 = ImageTk.PhotoImage(ex1_image)
    image_2 = canvas.create_image(
        185.0,
        365.0,
        image=image_image_2
    )

    ex2_image = Image.open(r"Admin_UI\assets\frame2\ex2.png").resize((100,50),Image.NEAREST)
    image_image_3 = ImageTk.PhotoImage(ex2_image)
    image_3 = canvas.create_image(
        185.0,
        280.0,
        image=image_image_3
    )

    ex3_image = Image.open(r"Admin_UI\assets\frame2\ex3.png").resize((100,50),Image.NEAREST)
    image_image_4 = ImageTk.PhotoImage(ex3_image)
    image_4 = canvas.create_image(
        185.0,
        195.0,
        image=image_image_4
    )

    button_image_4 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=open_HomePage,
        relief="flat",
        background='white'
    )
    button_4.place(
        x=285.0,
        y=36.0,
        width=59.0,
        height=26.0
    )

    button_image_5 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_5.png")
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=open_PatinitPage,
        relief="flat",
        background='white'
    )
    button_5.place(
        x=359.0,
        y=36.0,
        width=73.0,
        height=26.0
    )

    button_image_6 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_6.png")
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=open_AboutPage,
        relief="flat",
        background='white'
    )
    button_6.place(
        x=447.0,
        y=36.0,
        width=68.0,
        height=26.0
    )

    canvas.create_rectangle(
        146.0,
        89.0,
        653.0,
        90.0,
        fill="#000000",
        outline="")

    button_image_7 = PhotoImage(
        file=r"Admin_UI\assets\frame2\button_7.png")
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=open_Login_Logout,
        relief="flat",
        background='white'
    )
    button_7.place(
        x=740.0,
        y=31.0,
        width=30.0,
        height=30.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    Show()
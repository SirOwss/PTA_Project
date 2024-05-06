from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


import Home_User, About_User,Exsercise_User,Instractions_User
import FootUser1,FootR_User2,FootR_User3,FootL_User2,FootL_User3,Foot_User4
import LegUser1,LegR_User2,LegR_User3,LegL_User2,LegL_User3,Leg_User4
import SideUser1,SideR_User2,SideR_User3,SideL_User2,SideL_User3,Side_User4
import sys
sys.path.append(r"C:\Users\osama\Desktop\Symmaiyah\build")
from Primary import Login

def Show():
    def open_Login_Logout():
        window.destroy()
        Login.Show()
    def open_HomePage():
        window.destroy()
        Home_User.Show()
    def open_AboutPage():
        window.destroy()
        About_User.Show()
    def open_ExsercisePage():
        window.destroy()
        Exsercise_User.Show()
    def open_InstractionsPage():
        window.destroy()
        Instractions_User.Show()
    def open_FootPage1():
        window.destroy()
        FootUser1.Show()
    def open_FootPageR2():
        window.destroy()
        FootR_User2.Show()
    def open_FootPageR3():
        window.destroy()
        FootR_User3.Show()
    def open_FootPageL2():
        window.destroy()
        FootL_User2.Show()
    def open_FootPageL3():
        window.destroy()
        FootL_User3.Show()
    def open_FootPage4():
        window.destroy()
        Foot_User4.Show()
    def open_LegPage1():
        window.destroy()
        LegUser1.Show()
    def open_LegPageR2():
        window.destroy()
        LegR_User2.Show()
    def open_LegPageR3():
        window.destroy()
        LegR_User3.Show()
    def open_LegPageL2():
        window.destroy()
        LegL_User2.Show()
    def open_LegPageL3():
        window.destroy()
        LegL_User3.Show()
    def open_LegPage4():
        window.destroy()
        Leg_User4.Show()
    def open_SidePage1():
        window.destroy()
        SideUser1.Show()
    def open_SidePageR2():
        window.destroy()
        SideR_User2.Show()
    def open_SidePageR3():
        window.destroy()
        SideR_User3.Show()
    def open_SidePageL2():
        window.destroy()
        SideL_User2.Show()
    def open_SidePageL3():
        window.destroy()
        SideL_User3.Show()
    def open_SidePage4():
        window.destroy()
        Side_User4.Show()


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
        file=r"User_UI\asset\frame24\image_1.png")
    image_1 = canvas.create_image(
        54.0,
        49.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=r"User_UI\asset\frame24\image_2.png")
    image_2 = canvas.create_image(
        399.0,
        159.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        146.0,
        89.0,
        653.0,
        90.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        115.0,
        235.0,
        anchor="nw",
        text="INTRODUCING OUR REVOLUTIONARY PHYSICAL THERAPY APPLICATION, DESIGNED \nTO EMPOWER YOU ON YOUR REHABILITATION JOURNEY FROM THE COMFORT OF YOUR \nHOME, ANYTIME. OUR APP PROVIDES PERSONALIZED GUIDANCE AND REAL-TIME \nFEEDBACK TO ENSURE YOUR SAFETY AND UNLOCK MAXIMUM BENEFITS. \nWITH EASY-TO-FOLLOW INSTRUCTIONS AND INNOVATIVE MOTION TRACKING TECHNOLOGY, \nYOU CAN CONFIDENTLY PROGRESS TOWARDS YOUR RECOVERY GOALS WITH \nPROFESSIONAL SUPPORT RIGHT AT YOUR FINGERTIPS.".lower(),
        fill="#000000",
        font=("Itim Regular", 19 * -1)
    )


    image_image_3 = PhotoImage(
        file=r"User_UI\asset\frame24\image_3.png")
    image_3 = canvas.create_image(
        392.0,
        459.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=r"User_UI\asset\frame24\button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_HomePage,
        relief="flat",
        background='white'
    )
    button_1.place(
        x=278.0,
        y=36.0,
        width=59.0,
        height=26.0
    )

    button_image_2 = PhotoImage(
        file=r"User_UI\asset\frame24\button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_InstractionsPage,
        relief="flat",
        background='white'
    )
    button_2.place(
        x=352.0,
        y=36.0,
        width=87.0,
        height=26.0
    )

    button_image_3 = PhotoImage(
        file=r"User_UI\asset\frame24\button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=open_AboutPage,
        relief="flat",
        background='white'
    )
    button_3.place(
        x=454.0,
        y=36.0,
        width=68.0,
        height=26.0
    )

    button_image_4 = PhotoImage(
        file=r"User_UI\asset\frame24\button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=open_Login_Logout,
        relief="flat",
        background='white'
    )
    button_4.place(
        x=740.0,
        y=31.0,
        width=30.0,
        height=35.0
    )
    window.resizable(False, False)
    window.mainloop()
if __name__ == "__main__":
    Show()
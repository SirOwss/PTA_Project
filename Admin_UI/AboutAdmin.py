from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
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
    image_image_1 = PhotoImage(
        file=r"Admin_UI\assets\frame25\image_1.png")
    image_1 = canvas.create_image(
        54.0,
        49.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=r"Admin_UI\assets\frame25\image_2.png")
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
        file=r"Admin_UI\assets\frame25\image_3.png")
    image_3 = canvas.create_image(
        392.0,
        459.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=r"Admin_UI\assets\frame25\button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_HomePage,
        relief="flat",
        background='white'
    )
    button_1.place(
        x=284.0,
        y=36.0,
        width=59.0,
        height=26.0
    )

    button_image_2 = PhotoImage(
        file=r"Admin_UI\assets\frame25\button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_PatinitPage,
        relief="flat",
        background='white'
    )
    button_2.place(
        x=358.0,
        y=36.0,
        width=75.0,
        height=26.0
    )

    button_image_3 = PhotoImage(
        file=r"Admin_UI\assets\frame25\button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=open_AboutPage,
        relief="flat",
        background='white'
    )
    button_3.place(
        x=448.0,
        y=36.0,
        width=68.0,
        height=26.0
    )

    button_image_4 = PhotoImage(
        file=r"Admin_UI\assets\frame25\button_4.png")
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
        height=30.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    Show()
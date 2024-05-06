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
    def read_reps():
        with open("reps_count_Foot_Admin.txt", "r") as file:
            count = int(file.read().strip())
            return count
    def clear_file_contents():
        with open("reps_count_Foot_Admin.txt", 'w')as file:
            pass 
    

    def printout_Report():
        clear_file_contents()
    
    CorrectReps =  read_reps()
    MissingReps = 10-CorrectReps
    AccuracyRatio = (CorrectReps/10) *100


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
        file=r"Admin_UI\assets\frame15\image_1.png")
    image_1 = canvas.create_image(
        538.967529296875,
        233.0,
        image=image_image_1
    )

    

    image_image_3 = PhotoImage(
        file=r"Admin_UI\assets\frame15\image_3.png")
    image_3 = canvas.create_image(
        400.0,
        297.981201171875,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=r"Admin_UI\assets\frame15\image_4.png")
    image_4 = canvas.create_image(
        54.0,
        49.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=r"Admin_UI\assets\frame15\image_5.png")
    image_5 = canvas.create_image(
        261.0,
        233.0,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=r"Admin_UI\assets\frameEn\entry_1.png")
    entry_bg_1 = canvas.create_image(
        400.0,
        500.5,
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
        y=478.0,
        width=307.0,
        height=41.0
    )

    canvas.create_text(
        231.0,
        455.0,
        anchor="nw",
        text="FeedBack For Patinit:",
        fill="#022E31",
        font=("Inika Bold", 15 * -1)
    )

    canvas.create_rectangle(
        146.0,
        89.0,
        653.0,
        90.0,
        fill="#000000",
        outline="")

    button_image_1 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_HomePage,
        relief="flat",
        background='white'
    )
    button_1.place(
        x=285.0,
        y=36.0,
        width=59.0,
        height=26.0
    )

    button_image_2 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_PatinitPage,
        relief="flat",
        background='white'
    )
    button_2.place(
        x=359.0,
        y=36.0,
        width=73.0,
        height=26.0
    )

    button_image_3 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=open_AboutPage,
        relief="flat",
        background='white'
    )
    button_3.place(
        x=447.0,
        y=36.0,
        width=68.0,
        height=26.0
    )

    canvas.create_text(
        340.0,
        136.0,
        anchor="nw",
        text="Foot Stretch",
        fill="#000000",
        font=("Itim Regular", 20 * -1)
    )

    canvas.create_text(
        340.0,
        168.0,
        anchor="nw",
        text="Patient: 001",
        fill="#000000",
        font=("Itim Regular", 20 * -1)
    )

    button_image_4 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=printout_Report,
        relief="flat",
        background='white'
    )
    button_4.place(
        x=174.0,
        y=394.0,
        width=125.0,
        height=45.0
    )

    button_image_5 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_5.png")
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=open_ExsercisePage,
        relief="flat",
        background='white'
    )
    button_5.place(
        x=479.0,
        y=394.0,
        width=125.0,
        height=45.0
    )

    button_image_6 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_6.png")
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=open_Login_Logout,
        relief="flat",
        background='white'
    )
    button_6.place(
        x=740.0,
        y=31.0,
        width=30.0,
        height=30.0
    )
    canvas.create_text(
        450,
        233.5,
        text=str(CorrectReps),
        fill="#FFFFFF",
        font=("Itim Regular", 20 * -1)
    )
    canvas.create_text(
        315,
        300.5,
        text=str(MissingReps),
        fill="#000000",
        font=("Itim Regular", 20 * -1)
    )

    canvas.create_text(
        185,
        233.5,
        text=str(AccuracyRatio)+"%",
        fill="#FFFFFF",
        font=("Itim Regular", 20 * -1)
    )
    button_image_7 = PhotoImage(
        file=r"Admin_UI\assets\frame15\button_4.png")
    button_7 = Button(
        text="Send",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("The Message Are Sent!"),
        relief="flat",
        background='#CBDEF4',
    )
    button_7.place(
        x=510.0,
        y=478.0,
        width=50.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    Show()
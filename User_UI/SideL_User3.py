from pathlib import Path
from tkinter import *
from PIL import Image,ImageTk
import cv2
import numpy as np
import PoseModule as pm

import Home_User, About_User,Exsercise_User,Instractions_User
import FootUser1,FootR_User2,FootR_User3,FootL_User2,FootL_User3,Foot_User4
import LegUser1,LegR_User2,LegR_User3,LegL_User2,LegL_User3,Leg_User4
import SideUser1,SideR_User2,SideR_User3,SideL_User2,SideL_User3,Side_User4
import sys
sys.path.append(r"C:\Users\osama\Desktop\Symmaiyah\build")
from Primary import Login
count = 0
dir = 0
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
    canvas.create_text(
        320.0,
        118.0,
        anchor="nw",
        text="Side Lying Leg Lift",
        fill="#000000",
        font=("Itim Regular", 20 * -1)
    )

    image_image_1 = PhotoImage(
        file=r"User_UI\asset\frame9\image_1.png")
    image_1 = canvas.create_image(
        54.0,
        49.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=r"User_UI\asset\frame9\button_1.png")
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
        file=r"User_UI\asset\frame9\button_2.png")
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
        file=r"User_UI\asset\frame9\button_3.png")
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

    canvas.create_rectangle(
        146.0,
        89.0,
        653.0,
        90.0,
        fill="#000000",
        outline="")

    

    count_text=canvas.create_text(
        216.0,
        487.0,
        anchor="nw",
        text=f"Count of correct exercise repetitions: 0",
        fill="#000000",
        font=("Itim Regular", 20 * -1)
    )



    
    label = Label(window)
    label.grid(row=0, column=1, padx=140, pady=180)
        
    cap = cv2.VideoCapture(0)
        
    detector = pm.poseDetector()
    
    
    def update():
        global count, dir
        
        ret, frame = cap.read()
        if not ret:
            window.after(10, update)
            return

        frame = cv2.resize(frame, (500, 300))
            
        frame = detector.findPose(frame, False)
        lmlist = detector.findPosition(frame, False)
            
        if lmlist:
            angle = detector.findAngle(frame, 24, 23, 25)
            per = np.interp(angle,(249,270),(-100,0))
                
            if per == 0:
                if dir == 0:
                    count +=0.5
                    dir = 1
            if per == -100:
                if dir == 1:
                    count += 0.5
                    dir = 0
            
            
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
            
        label.imgtk = imgtk
        label.configure(image=imgtk)
            
        window.after(10, update)
        canvas.itemconfig(count_text, text=f"Count of correct exercise repetitions: {int(count)}")
        
        
    
    
    update()
    def save_reps(count):
        with open("reps_count_Side.txt", "w") as file:
            file.write(str(int(count)))
    save_reps(count_text)





    canvas.create_text(
        245.0,
        147.0,
        anchor="nw",
        text="Number of repetitions required: 10",
        fill="#000000",
        font=("Itim Regular", 20 * -1)
    )

    button_image_4 = PhotoImage(
        file=r"User_UI\asset\frame9\button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=open_SidePage4,
        relief="flat",
        background='white'
    )
    button_4.place(
        x=354.0,
        y=528.0,
        width=95.0,
        height=60.0
    )

    button_image_5 = PhotoImage(
        file=r"User_UI\asset\frame9\button_5.png")
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=open_Login_Logout,
        relief="flat",
        background='white'
    )
    button_5.place(
        x=740.0,
        y=31.0,
        width=30.0,
        height=35.0
    )
    window.resizable(False, False)
    window.mainloop()
if __name__ == "__main__":
    Show()
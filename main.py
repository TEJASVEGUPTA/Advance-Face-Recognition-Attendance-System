from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import os

from Employee import Employee
from train import Train 
from face_recognition import face_recognition





class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        
        # first image
        img=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\Stanford.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        
        # Second Image
        img1=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        
        
        # Third Image
        img2=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\u.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        
        
        # BG Image
        img3=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)        
        
        
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        # Student Button
        img4=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\student.jpeg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.Student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Student Details",command=self.Student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        
        
        # Detect Face Button
        img5=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        
        # Attendence Face Button
        img6=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\attendance.jpeg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        # Help Button
        img7=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        
        # Train Button
        img8=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)
        
        
        
        # Photos Button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),command=self.open_img,bg="darkblue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)
        
        
        
        # Developers button
        img10=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)
        
        
        # Exit Button
        img11=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)
        
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)
    
    
    def open_img(self):
        os.startfile("data")
        
    
        
        # ===============Function Buttons===================
        
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
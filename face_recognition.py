from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",30,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # ================first image==============
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
              
        
        # ================second image==============
        img_bottom=Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((950, 700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        
        # ===========center button============
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),command=self.face_recog,bg="darkorange",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)

    # ==================Face recognition================
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbours)
            
            
            coor=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host="localhost ",username="root",password="tejasve",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from employee where Employee_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Department from employee where Employee_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Email_ID from employee where Employee_ID="+str(id))
                email=my_cursor.fetchone()
                email="+".join(email)
                
                
                my_cursor.execute("select Employee_ID from employee where Employee_ID="+str(id))
                e_id=my_cursor.fetchone()
                e_id="+".join(e_id)
                
                
                
                
                if confidence>77:
                    cv2.putText(img,f"Employee_id:{e_id}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Email_id:{email}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,245),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
                
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()
            
                    
                    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()
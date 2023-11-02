from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # ===================Variables============
        self.var_dep=StringVar()
        self.var_timing=StringVar()
        self.var_batch=StringVar()
        self.var_email=StringVar()
        self.var_ID=StringVar()
        self.var_name=StringVar()
        # self.var_Photo=StringVar()
        
        
        
         # first image
        img=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\face-recognition.png")
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
        
        
        
        title_lbl=Label(bg_img,text="VISITOR MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        
        
        # left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=("Times new roman", 12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        
        img_left=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        
        
        
        # current dept.        
        dept_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Department Information", font=("Times new roman", 12,"bold"))
        dept_frame.place(x=5,y=135,width=720,height=200)
        
        
        # Dept. Combobox
        dep_label=Label(dept_frame,text="Department",font=("Times new roman", 12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        
        dep_combo=ttk.Combobox(dept_frame,textvariable=self.var_dep, font=("Times new roman", 12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","HR","Soft. Dev.","Trainer","Cleaning","Visitor","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        #batch
        batch_label=Label(dept_frame,text="Department",font=("Times new roman", 12,"bold"))
        batch_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        
        batch_combo=ttk.Combobox(dept_frame,textvariable=self.var_batch, font=("Times new roman", 12,"bold"),state="readonly")
        batch_combo["values"]=("Select Batch","1st","2nd","3rd","4th","Other")
        batch_combo.current(0)
        batch_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        # Timing
        timing_label=Label(dept_frame,text="Timing",font=("Times new roman", 12,"bold"))
        timing_label.grid(row=1,column=0,padx=10,sticky=W)
        
        timing_combo=ttk.Combobox(dept_frame,textvariable=self.var_timing, font=("Times new roman", 12,"bold"),state="readonly")
        timing_combo["values"]=("Select Time","9:30-6:30","9:30-1:3.","1:30-6:30","6:30-9:30","Other")
        timing_combo.current(0)
        timing_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        
        
        
        
        # Visitor Informatrion        
        visitor_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Visitor Information", font=("Times new roman", 12,"bold"))
        visitor_frame.place(x=5,y=250,width=720,height=300)
        
        ID_label=Label(visitor_frame,text="ID:",font=("Times new roman", 13,"bold"))
        ID_label.grid(row=0,column=0,padx=10,sticky=W)
        
        
        # visitor_entry=ttk.Entry(visitor_frame,width=20,font=("Times new roman", 13,"bold"))
        # visitor_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        
        
        
        
        
        
        
        
        
        #employee name
        employee_name_label = Label(visitor_frame,text="Employee Name:",font=("verdana",12,"bold"),bg="white")
        employee_name_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        employee_name_entry = ttk.Entry(visitor_frame,width=20,textvariable=self.var_name,font=("verdana",12,"bold"))
        employee_name_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W) 
        
        #Employee id
        employeeId_label = Label(visitor_frame,text="Employee ID:",font=("verdana",12,"bold"),bg="white")
        employeeId_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        employeeId_entry = ttk.Entry(visitor_frame,textvariable=self.var_ID,width=20,font=("times new roman",12,"bold"))
        employeeId_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Email
        employee_email_label = Label(visitor_frame,text="Email:",font=("verdana",12,"bold"),bg="white")
        employee_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        employee_email_entry = ttk.Entry(visitor_frame,textvariable=self.var_email,width=20,font=("verdana",12,"bold"))
        employee_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        
        
        # date-
        # batch_label=Label(dept_frame,text="Department",font=("Times new roman", 12,"bold"))
        # batch_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        
        # batch_combo=ttk.Combobox(dept_frame,font=("Times new roman", 12,"bold"),state="readonly")
        # batch_combo["values"]=("Select Batch","1st","2nd","3rd","Other")
        # batch_combo.current(0)
        # batch_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        # Right label frame
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       

        # #Class Didvision
        # student_div_label = Label(visitor_frame,text="Class Division:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        # div_combo=ttk.Combobox(visitor_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        # div_combo["values"]=("Morning","Evening")
        # div_combo.current(0)
        # div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # #Roll No
        # student_roll_label = Label(visitor_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        # student_roll_entry = ttk.Entry(visitor_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        # student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        # #Gender
        # student_gender_label = Label(visitor_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        # #combo box 
        # gender_combo=ttk.Combobox(visitor_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        # gender_combo["values"]=("Male","Female","Others")
        # gender_combo.current(0)
        # gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # #Date of Birth
        # student_dob_label = Label(visitor_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        # student_dob_entry = ttk.Entry(visitor_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        # student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # #Email
        # student_email_label = Label(visitor_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        # student_email_entry = ttk.Entry(visitor_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        # student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        # #Phone Number
        # student_mob_label = Label(visitor_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        # student_mob_entry = ttk.Entry(visitor_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        # student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        # #Address
        # student_address_label = Label(visitor_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        # student_address_entry = ttk.Entry(visitor_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        # student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        # #Teacher Name
        # student_tutor_label = Label(visitor_frame,text="Tutor Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        # student_tutor_entry = ttk.Entry(visitor_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        # student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
        
        
        # Radio Button
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(visitor_frame,variable=self.var_radio1,text="take photo sample", value="Yes")
        Radiobutton1.grid(row=6,column=0)
        
        # self.var_radio2=StringVar()
        Radiobutton2=ttk.Radiobutton(visitor_frame,variable=self.var_radio1,text="No photo sample", value="No")
        Radiobutton2.grid(row=6,column=1)
        
        # Buttons Frame
        btn_frame=Frame(visitor_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"),command=self.update_data,bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=18,font=("times new roman",12,"bold"),command=self.delete_data,bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=18,font=("times new roman",12,"bold"),command=self.reset_data,bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(btn_frame,text="Take Photo Sample",width=18,font=("times new roman",12,"bold"),command=self.generate_dataset,bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)
        
        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)
        
        
        
        
        # ================================================================
        
        
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=("Times new roman", 12,"bold"))
        right_frame.place(x=780,y=10,width=700,height=580)
        
        
        img_right=Image.open(r"C:\Users\tejas\OneDrive\Desktop\RW\Adv Face Rec\college_images\student.jpeg")
        img_right=img_right.resize((700,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        # ========================search system==============================
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font=("Times new roman", 12,"bold"))
        search_frame.place(x=5,y=135,width=690,height=70)
        
        search_label=Label(search_frame,text="Search By:",font=("Times new roman", 12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("Times new roman", 12,"bold"),state="readonly")
        search_combo["values"]=("Select ","Employee Id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        search_entry=ttk.Entry(search_frame,width=15,font=("Times new roman", 13,"bold"))
        search_entry.grid(row=0,column=2,padx=4,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        show_all_btn=Button(search_frame,text="Show all",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)
        
        # ============================Table Frame=================================
        
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=690,height=350)
        
        Scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.visitor_table=ttk.Treeview(table_frame,columns=("department","Name","Batch","Email ID","Timing","ID","Photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.visitor_table.xview)
        Scroll_y.config(command=self.visitor_table.yview)
        
        self.visitor_table.heading("department",text="Department")
        self.visitor_table.heading("Batch",text="Batch")
        self.visitor_table.heading("Email ID",text="Email")
        self.visitor_table.heading("Timing",text="Timing")
        self.visitor_table.heading("ID",text="ID")
        self.visitor_table.heading("Name",text="Name")
        # self.visitor_table.heading("Other",text="Other")
        self.visitor_table.heading("Photo",text="Photo Sample Status")
        self.visitor_table["show"]="headings"
        
        self.visitor_table.column("department",width=100)
        self.visitor_table.column("Batch",width=100)
        self.visitor_table.column("Email ID",width=180)
        self.visitor_table.column("Timing",width=100)
        self.visitor_table.column("ID",width=100)
        self.visitor_table.column("Photo",width=100)
        self.visitor_table.column("Name",width=100)
        
        
        
        
        self.visitor_table.pack(fill=BOTH,expand=1)
        self.visitor_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    # ===========================Function Declration==============
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost ",username="root",password="tejasve",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Employee Values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_batch.get(),
                    self.var_email.get(),
                    self.var_timing.get(),
                    self.var_ID.get(),                  
                    self.var_radio1.get(),
                    
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Succesfully Saved new details ",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
        
    #======================fetch data===================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost ",username="root",password="tejasve",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.visitor_table.delete(*self.visitor_table.get_children())
            for i in data:
                self.visitor_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    # ===============================get Cursor===================
    
    def get_cursor(self,event=""):
        cursor_focus=self.visitor_table.focus()
        content=self.visitor_table.item(cursor_focus)
        data=content["values"]
        
       
       
        self.var_dep.set(data[0])
        self.var_name.set(data[1]),
        self.var_batch.set(data[2]),
        self.var_email.set(data[3]),
        self.var_timing.set(data[4]),
        self.var_ID.set(data[5]),                  
        self.var_radio1.set(data[6]),
         
         
# ==============Update Function==============


    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update employee Details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost ",username="root",password="tejasve",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE employee set Department=%s,Name=%s,Batch=%s,Email_ID=%s,Timing=%s,Photos=%s where Employee_ID=%s",(
                        
                            self.var_dep.get(),
                            self.var_name.get(),
                            self.var_batch.get(),
                            self.var_email.get(),
                            self.var_timing.get(),
                            self.var_radio1.get(),
                            self.var_ID.get()    
                        
                        
                        
                        
                        
                        
                        
                        
                            )) 
                else:
                    if not Update:
                        return
                    
                messagebox.showinfo("Success","Employee Details Updated Successfully",parent=self.root)    
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)    



# ===================Delete Function=================

    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Employee ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Deleting Page","Do you want to Delete Employee Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost ",username="root",password="tejasve",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from Employee where Employee_ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            
                messagebox.showinfo("Delete","Succesfully Deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
    # ===========Reset Function=============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set(""),
        self.var_batch.set("Select Batch"),
        self.var_email.set(""),
        self.var_timing.set("Select Time"),
        self.var_ID.set(""),
        self.var_radio1.set("")
            
        
        
#  ==============Generate Dataset or take photo sample=================
    def generate_dataset(self):
        
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost ",username="root",password="tejasve",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from Employee")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE employee set Department=%s,Name=%s,Batch=%s,Email_ID=%s,Timing=%s,Photos=%s where Employee_ID=%s",(
                            
                                self.var_dep.get(),
                                self.var_name.get(),
                                self.var_batch.get(),
                                self.var_email.get(),
                                self.var_timing.get(),
                                self.var_radio1.get(),
                                self.var_ID.get()==id+1    
                            
                            
                            
                            
                            
                            
                            
                            
                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #  ===================Load predefined data on frontals from Open CV==============
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor=1.3
                    #Minimum Neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                
                
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed!!!!")
            except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                        
                       
    
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
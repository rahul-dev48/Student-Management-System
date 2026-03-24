from tkinter import*
from PIL import Image,ImageTk#pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #=======title=======

        title=Label(
            self.root,text="Manage Student Details",
            font=(
                "goudy old style",20,"bold"),
                bg="#033054",fg="white")
        title.place(x=10,y=15,width=1180,height=35)
        #============variables===========
        self.variable_roll=StringVar()
        self.variable_name=StringVar()
        self.variable_email=StringVar()
        self.variable_gender=StringVar()
        self.variable_dob=StringVar()
        self.variable_contact=StringVar()
        self.variable_course=StringVar()
        self.variable_a_date=StringVar()
        self.variable_state=StringVar()
        self.variable_city=StringVar()
        self.variable_pin=StringVar()
        # self.variable_duration=StringVar()
        # self.variable_charges=StringVar()
        #============Widgets===============
        #============column1===============
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style ",15,"bold"),bg="White").place(x=10,y=60)
        lbl_Name=Label(self.root,text="Name",font=("goudy old style ",15,"bold"),bg="White").place(x=10,y=100)
        lbl_Email=Label(self.root,text="Email",font=("goudy old style ",15,"bold"),bg="White").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style ",15,"bold"),bg="White").place(x=10,y=180)

        lbl_state=Label(self.root,text="State",font=("goudy old style ",15,"bold"),bg="White").place(x=10,y=220)
        txt_state=Entry(self.root,textvariable=self.variable_state,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=150,y=220,width=150)
        
        lbl_city=Label(self.root,text="City",font=("goudy old style ",15,"bold"),bg="White").place(x=310,y=220)
        txt_city=Entry(self.root,textvariable=self.variable_city,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=380,y=220,width=100)
        
        
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style ",15,"bold"),bg="White").place(x=500,y=220)
        txt_pin=Entry(self.root,textvariable=self.variable_pin,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=560,y=220,width=120)
        
        lbl_address=Label(self.root,text="Address",font=("goudy old style ",15,"bold"),bg="White").place(x=10,y=260)

        #============Entry Fields==========
        self.txt_roll=Entry(self.root,textvariable=self.variable_roll,font=("goudy old style ",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.variable_name,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.variable_email,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.variable_gender,values=("Select","Male","Female","Other"),font=("goudy old style ",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)


        #============column2===============
        self.course_list=["Empty"]
        #===function_call to update the list
        self.fetch_course()
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style ",15,"bold"),bg="White").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style ",15,"bold"),bg="White").place(x=360,y=100)
        lbl_addmission=Label(self.root,text="Addmission",font=("goudy old style ",15,"bold"),bg="White").place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style ",15,"bold"),bg="White").place(x=360,y=180)
         
        
        #============Entry Fields==========
        txt_dob=Entry(self.root,textvariable=self.variable_dob,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.variable_contact,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=480,y=100,width=200)
        txt_addmission=Entry(self.root,textvariable=self.variable_a_date,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.variable_course,values=self.course_list,font=("goudy old style ",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")


        #==========Text Address=========

        self.txt_address=Text(self.root,font=("goudy old style ",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,width=540,height=100)
        #=====Buttons======
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)

        self.btn_add=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#21f356",fg="white",cursor="hand2",command=self.update)
        self.btn_add.place(x=270,y=400,width=110,height=40)

        self.btn_add=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#c51016",fg="white",cursor="hand2",command=self.delete)
        self.btn_add.place(x=390,y=400,width=110,height=40)

        self.btn_add=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#5b6165",fg="white",cursor="hand2",command=self.clear)
        self.btn_add.place(x=510,y=400,width=110,height=40)

        #=======search panel==========
        self.variable_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style ",15,"bold"),bg="White").place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.variable_search,font=("goudy old style ",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#82bce3",fg="white",cursor="hand2",command=self.searce).place(x=1070,y=60,width=120,height=28)

        #========contant=======
        self.C_Frame=Frame(self.root,bd=3,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        Scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        Scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","pin","address"),xscrollcommand=Scrollx.set,yscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.CourseTable.xview)
        Scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("addmission",text="Addmission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=200)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    #==================================================================================================================
    def clear(self):
        self.show()
        self.variable_roll.set("")
        self.variable_name.set("")
        self.variable_email.set("")
        self.variable_gender.set("Select")
        self.variable_dob.set("")
        self.variable_contact.set("")
        self.variable_a_date.set("")
        self.variable_course.set("Select")
        self.variable_state.set("")
        self.variable_city.set("")
        self.variable_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.variable_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.variable_roll.get()=="":
                messagebox.showerror("Error","Roll NO. Should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.variable_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.variable_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student delete Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        

        


    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.variable_roll.set(row[0])
        self.variable_name.set(row[1])
        self.variable_email.set(row[2])
        self.variable_gender.set(row[3])
        self.variable_dob.set(row[4])
        self.variable_contact.set(row[5])
        self.variable_a_date.set(row[6])
        self.variable_course.set(row[7])
        self.variable_state.set(row[8])
        self.variable_city.set(row[9])
        self.variable_pin.set(row[10])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])
        

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.variable_roll.get()=="":
                messagebox.showerror("Error","Roll Number Should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.variable_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No. already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,addmission,course,state,city,pin,address)values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.variable_roll.get(),
                        self.variable_name.get(),
                        self.variable_email.get(),
                        self.variable_gender.get(),
                        self.variable_dob.get(),
                        self.variable_contact.get(),
                        self.variable_a_date.get(),
                        self.variable_course.get(),
                        self.variable_state.get(),
                        self.variable_city.get(),
                        self.variable_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.variable_roll.get()=="":
                messagebox.showerror("Error","Roll No. Should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.variable_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update  student set name=?,email=?,gender=?,dob=?,contact=?,addmission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.variable_name.get(),
                        self.variable_email.get(),
                        self.variable_gender.get(),
                        self.variable_dob.get(),
                        self.variable_contact.get(),
                        self.variable_a_date.get(),
                        self.variable_course.get(),
                        self.variable_state.get(),
                        self.variable_city.get(),
                        self.variable_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.variable_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def  show (self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
                cur.execute("select * from student")
                rows=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert("",END,values=row)

               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def  fetch_course (self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
                cur.execute("select name from course")
                rows=cur.fetchall()
                if len(rows)>0:
                    for row in rows:
                        self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def  searce (self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
                cur.execute(f"select * from student where roll=?",(self.variable_search.get(),))
                rows=cur.fetchone()
                if rows!=None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                        self.CourseTable.insert("",END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()

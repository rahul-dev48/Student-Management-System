from tkinter import*
from PIL import Image,ImageTk#pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #=======title=======

        title=Label(
            self.root,text="Add Student Result",
            font=(
                "goudy old style",20,"bold"),
                bg="orange",fg="#262626")
        title.place(x=10,y=15,width=1180,height=50)
        #============variables===========
        self.variable_course=StringVar()
        self.variable_duration=StringVar()
        self.variable_charges=StringVar()
        #=======widgets=========
        #=======variable=======
        self.variable_roll=StringVar()
        self.variable_name=StringVar()
        self.variable_course=StringVar()
        self.variable_marks=StringVar()
        self.variable_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

        Lbl_select=Label(self.root,text="Select Student",font=("goudy old Style",20,"bold"),bg="white").place(x=50,y=100)
        Lbl_name=Label(self.root,text="Name",font=("goudy old Style",20,"bold"),bg="white").place(x=50,y=160)
        Lbl_course=Label(self.root,text="Course",font=("goudy old Style",20,"bold"),bg="white").place(x=50,y=220)
        Lbl_markrs_obj=Label(self.root,text="Marks Obtained",font=("goudy old Style",20,"bold"),bg="white").place(x=50,y=280)
        Lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old Style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.variable_roll,values=self.roll_list,font=("goudy old style ",15,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#82bce3",fg="white",cursor="hand2",command=self.searce).place(x=500,y=100,width=100,height=28)
        
        txt_name=Entry(self.root,textvariable=self.variable_name,font=("goudy old style ",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.variable_course,font=("goudy old style ",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.variable_marks,font=("goudy old style ",20,"bold"),bg="lightyellow").place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,textvariable=self.variable_full_marks,font=("goudy old style ",20,"bold"),bg="lightyellow").place(x=280,y=340,width=320)


        #========button=====
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)


        #=================image==========================
        
        self.bg_img=Image.open("image/result.jpeg")
        self.bg_img=self.bg_img.resize((500,300),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.labl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)


    #============================================================================================================

    def  fetch_roll (self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
                cur.execute("select roll,name from student")
                rows=cur.fetchall()
                if len(rows)>0:
                    for row in rows:
                        self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    

    def  searce (self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
                cur.execute(f"select name,course from student where roll=?",(self.variable_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                     self.variable_name.set(row[0])
                     self.variable_course.set(row[1])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.variable_name.get()=="":
                messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.variable_roll.get(),self.variable_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per=(int(self.variable_marks.get())*100)/int(self.variable_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per)values(?,?,?,?,?,?)",(
                        self.variable_roll.get(),
                        self.variable_name.get(),
                        self.variable_course.get(),
                        self.variable_marks.get(),
                        self.variable_full_marks.get(),
                        str(per)
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def clear(self):
         self.variable_roll.set("Select"),
         self.variable_name.set(""),
         self.variable_course.set(""),
         self.variable_marks.set(""),
         self.variable_full_marks.set(""),

        




if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()
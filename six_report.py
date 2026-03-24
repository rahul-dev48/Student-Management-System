from tkinter import*
from PIL import Image,ImageTk#pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #=======title=======

        title=Label(
            self.root,text="View Student Result",
            font=(
                "goudy old style",20,"bold"),
                bg="orange",fg="#262626")
        title.place(x=10,y=15,width=1180,height=50)
        #======search=========
        self.variable_search=StringVar()
        self.variable_id=""
        Lbl_search=Label(self.root,text="Search By Roll No.",font=("goudy old Style",20,"bold"),bg="white").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.variable_search,font=("goudy old Style",20,),bg="lightyellow").place(x=520,y=100,width=150)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#82bce3",fg="white",cursor="hand2",command=self.searce).place(x=680,y=100,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=35)

        #=====result labels========
        lbl_roll=Label(self.root,text="Roll No",font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full=Label(self.root,text="Total Marks",font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)
        

        self.roll=Label(self.root,font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)

        self.name=Label(self.root,font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)

        self.course=Label(self.root,font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)

        self.marks=Label(self.root,font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)

        self.full=Label(self.root,font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)

        self.per=Label(self.root,font=("goudy old Style",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        #===========Button delete========
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=35)
        #=====================================================================
    def  searce (self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.variable_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("Select * from result where roll=?",(self.variable_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.variable_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                        
                else:
                     messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        con.close()

    def clear(self):
        self.variable_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.variable_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.variable_id=="":
                messagebox.showerror("Error","Search Student result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.variable_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invelid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.variable_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result delete Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        


if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()




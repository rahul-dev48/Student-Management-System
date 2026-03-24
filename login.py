from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Developed By Rahul | Webcode")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # ===== MULTIPLE USERS DATA =====
        self.users = {
            "Rahul": "123456",
            "Amit": "111111",
            "Neha": "222222"
        }

        # ===== IMAGE =====
        img = Image.open("image/p.jpeg")
        img = img.resize((350, 550), Image.LANCZOS)
        self.phone_image = ImageTk.PhotoImage(img)
        Label(self.root, image=self.phone_image, bd=0).place(x=200, y=50)

        # ===== LOGIN FRAME =====
        login_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        login_frame.place(x=570, y=50, width=350, height=460)

        Label(login_frame, text="Login System",
              font=("Elephant", 30, "bold"),
              bg="white").place(x=0, y=30, relwidth=1)

        Label(login_frame, text="Username",
              font=("Andalus", 15),
              bg="white", fg="#767171").place(x=50, y=100)

        self.username = StringVar()
        self.password = StringVar()

        Entry(login_frame, textvariable=self.username,
              font=("times new roman", 15),
              bg="#ECECEC").place(x=50, y=140, width=250)

        Label(login_frame, text="Password",
              font=("Andalus", 15),
              bg="white", fg="#767171").place(x=50, y=200)

        Entry(login_frame, textvariable=self.password,
              show="*",
              font=("times new roman", 15),
              bg="#ECECEC").place(x=50, y=240, width=250)

        Button(login_frame, text="Log In",
               command=self.login,
               font=("Arial Rounded MT Bold", 15),
               bg="#00B0F0", fg="white",
               cursor="hand2").place(x=50, y=300, width=250, height=35)

        Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)
        Label(login_frame, text="OR",
              fg="lightgray", bg="white",
              font=("times new roman", 15, "bold")).place(x=150, y=355)

        Button(login_frame, text="Forget Password?",
               command=self.forget_password,
               font=("times new roman", 13),
               bg="white", fg="#00759E",
               bd=0, cursor="hand2").place(x=100, y=390)

        # ===== REGISTER FRAME =====
        register_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        register_frame.place(x=570, y=525, width=350, height=75)

        Label(register_frame, text="Don't have an account ?",
              font=("times new roman", 13),
              bg="white").place(x=40, y=20)

        Button(register_frame, text="Sign Up",
               command=self.signup,
               font=("times new roman", 13, "bold"),
               bg="white", fg="#00759E",
               bd=0, cursor="hand2").place(x=225, y=17)

    # ===== LOGIN FUNCTION =====
    def login(self):
        u = self.username.get()
        p = self.password.get()

        if u == "" or p == "":
            messagebox.showerror("Error", "All fields are required")

        elif u not in self.users:
            messagebox.showerror("Error", "Username not found")

        elif self.users[u] != p:
            messagebox.showerror("Error", "Wrong Password")

        else:
            messagebox.showinfo("Success", f"Welcome : {u}")
            os.system("python one_dashboard.py")

    # ===== FORGET PASSWORD =====
    def forget_password(self):
        win = Toplevel(self.root)
        win.title("Forget Password")
        win.geometry("350x260+600+200")
        win.config(bg="white")

        Label(win, text="Forget Password",
              font=("Elephant", 20),
              bg="white").pack(pady=15)

        Label(win, text="Enter Username",
              font=("times new roman", 14),
              bg="white").pack(pady=5)

        user_var = StringVar()

        Entry(win, textvariable=user_var,
              font=("times new roman", 14),
              bg="#ECECEC").pack(pady=10)

        def check_user():
            u = user_var.get()

            if u == "":
                messagebox.showerror("Error", "Username required", parent=win)

            elif u in self.users:
                messagebox.showinfo(
                    "Password Found",
                    f"Username : {u}\nPassword : {self.users[u]}",
                    parent=win
                )
                win.destroy()

            else:
                messagebox.showerror("Error", "Account not found", parent=win)

        Button(win, text="Submit",
               command=check_user,
               font=("Arial Rounded MT Bold", 14),
               bg="#00B0F0", fg="white").pack(pady=20)

    # ===== SIGN UP =====
    def signup(self):
        win = Toplevel(self.root)
        win.title("Sign Up")
        win.geometry("350x300+600+200")
        win.config(bg="white")

        Label(win, text="Create Account",
              font=("Elephant", 20),
              bg="white").pack(pady=20)

        new_user = StringVar()
        new_pass = StringVar()

        Entry(win, textvariable=new_user,
              font=("times new roman", 14),
              bg="#ECECEC").pack(pady=10)

        Entry(win, textvariable=new_pass,
              show="*",
              font=("times new roman", 14),
              bg="#ECECEC").pack(pady=10)

        def save_user():
            u = new_user.get()
            p = new_pass.get()

            if u == "" or p == "":
                messagebox.showerror("Error", "All fields required")

            elif u in self.users:
                messagebox.showerror("Error", "Username already exists")

            else:
                self.users[u] = p
                messagebox.showinfo("Success", "Account Created Successfully")
                win.destroy()

        Button(win, text="Register",
               command=save_user,
               font=("Arial Rounded MT Bold", 14),
               bg="#00B0F0", fg="white").pack(pady=20)


# ===== MAIN =====
root = Tk()
obj = login_System(root)
root.mainloop()

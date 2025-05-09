from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from Add import ClassManagementSystem
class LoginPage:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Login")
        self.root.geometry("800x600")
        self.root.maxsize(800,600)
        self.root.configure(bg="#0d0d1a")
        img=Image.open(r"F:\New folder (3)\footer-logo.png")
        img=img.resize((100,40),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbling=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        lbling.place(x=5,y=4,width=100,height=80)
        
        title = Label(root, text="Login", font=("Arial", 24, "bold"), bg="#0d0d1a", fg="#ffffff")
        title.pack(pady=(50, 5))
        subtitle = Label(root, text="to decode your dreams", font=("Arial", 12), bg="#0d0d1a", fg="#cccccc")
        subtitle.pack(pady=(0, 30))
        # Entry field
        username=Label(self.root,text='Username',font=("Arial", 14), bg="#262626", fg="#ffffff", bd=0)
        username.place(x=250,y=155)

        self.entry1 = Entry(root, width=30, font=("Arial", 14), bg="#262626", fg="#ffffff", bd=0, insertbackground="white")
        self.entry1.place(x=250,y=200)
        self.entry1.insert(0, "")

        password=Label(self.root,text='Password',font=("Arial", 14), bg="#262626", fg="#ffffff", bd=0)
        password.place(x=250,y=250)

        self.entry2 = Entry(root, width=30, font=("Arial", 14), bg="#262626", fg="#ffffff", bd=0, insertbackground="white")
        self.entry2.place(x=250,y=300)
        self.entry2.insert(0, "")
        login_btn =Button(root, text="Login",command=self.login, font=("Arial", 14, "bold"), bg="#a0ff00", fg="#000000", width=20, bd=0)
        login_btn.place(x=300,y=400)

    def login(self):
        username = self.entry1.get().strip()
        password = self.entry2.get().strip()

        # Check if both fields are filled
        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='SQLPassword12#',database='itvedant')
            cursor=conn.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            if result:
                    messagebox.showinfo("Login Success", f"Welcome, {username}!")
                    self.new_window = Toplevel(self.root)
                    self.app = ClassManagementSystem(self.new_window)  # Open your new window
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        #     if result:
        #         messagebox.showinfo("Login Success", f"Welcome, {username}!")
        #     else:
        #         messagebox.showerror("Login Failed", "Invalid username or password")

        # except mysql.connector.Error as err:
        #     messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        
       

        
    #     # Styling
    # def style_widget(widget, fg="#ffffff", bg="#0d0d1a", font=("Arial", 12)):
    #     widget.configure(fg=fg, bg=bg, font=font)
    # Title




        

if __name__=="__main__":
    root=Tk()
    obj=LoginPage(root)
    root.mainloop()
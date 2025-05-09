from tkinter import *
from tkinter import ttk 
import mysql.connector 
from tkinter import messagebox as tmsg
from PIL import Image,ImageTk
import datetime
from  Dashboard import Dashboard

class ClassManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x600")
        self.root.title("Wingz")
        self.root.maxsize(800,600)
        root.configure(bg="#0d0d1a")
        img1=Image.open(r'G:\python\prop\1609855173964.png')
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg='#0d0d1a',borderwidth=0)
        lblimg1.place(x=5,y=1,width=100,height=100)
        # Labels and Entry fields
        self.id_Var=IntVar()
        self.name_Var=StringVar()
        self.attendance_var=StringVar()
        self.assignment_var=StringVar()
        self.assessment_var=StringVar()
        self.Internal_mock_var=StringVar()
        self.project_var=StringVar()
        self.CCE_var=StringVar()

        ID=Label(self.root, text="Student ID:", bg="#0d0d1a", fg="#ffffff")
        ID.place(x=96,y=20)
        
        self.id =Entry(root,textvariable=self.id_Var, width=50)
        self.id.place(x=200, y=20)
        
        Name=Label(root, text="Name:", bg="#0d0d1a", fg="#ffffff")
        Name.place(x=96,y=50)
        
        self.entry_name =Entry(root,textvariable=self.name_Var, width=50)
        self.entry_name.place(x=200, y=50)

        attendance=Label(root, text="Attendance:", bg="#0d0d1a", fg="#ffffff")
        attendance.place(x=96,y=80)
        self.entry_attendance =Entry(root,textvariable=self.attendance_var, width=50)
        self.entry_attendance.place(x=200, y=80)

        assignment=Label(root, text="Assignment:", bg="#0d0d1a", fg="#ffffff")
        assignment.place(x=96,y=110)
        self.entry_assignment =Entry(root,textvariable=self.assignment_var, width=50)
        self.entry_assignment.place(x=200, y=110)

        assessment=Label(root, text="Assessment:", bg="#0d0d1a", fg="#ffffff")
        assessment.place(x=96,y=140)
        self.entry_assessment = Entry(root,textvariable=self.assessment_var, width=50)
        self.entry_assessment.place(x=200, y=140)

        Internal=Label(root, text="Internal Mock:", bg="#0d0d1a", fg="#ffffff")
        Internal.place(x=96,y=170)
        self.entry_internal_mock = Entry(root,textvariable=self.Internal_mock_var, width=50)
        self.entry_internal_mock.place(x=200, y=170)

        project=Label(root, text="Project Evaluation:", bg="#0d0d1a", fg="#ffffff")
        project.place(x=96,y=200)
        self.entry_project_evaluation = Entry(root,textvariable=self.project_var, width=50)
        self.entry_project_evaluation.place(x=200, y=200)

        CCE=Label(root, text="CCE Exam:", bg="#0d0d1a", fg="#ffffff")
        CCE.place(x=96,y=230)
        self.entry_cce_exam = Entry(root,textvariable=self.CCE_var, width=50)
        self.entry_cce_exam.place(x=200,y=230)


        # Data Table with Scrollbar
        frame = Frame(root)
        frame.place(x=50, y=340,width=700,height=250)

        scrollbar_y = Scrollbar(frame,orient=VERTICAL)
        
        scrollbar_x = Scrollbar(frame,orient=HORIZONTAL)
        

        self.tree = ttk.Treeview(frame, columns=("Student_id","Name", "Attendance", "Assignment", "Assessment", "Internal Mock", "Project Evaluation", "CCE Exam"), show='headings', yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set)
        
        scrollbar_x.config(command=self.tree.xview)
        scrollbar_y.config(command=self.tree.yview)
        for col in ("Student_id","Name", "Attendance", "Assignment", "Assessment", "Internal Mock", "Project Evaluation", "CCE Exam"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        scrollbar_y.pack(side='right', fill='y')
        scrollbar_x.pack(side='bottom', fill='x')
        self.tree.pack(side='left', fill='both', expand=True)
        
        btnaDDdata=Button(self.root,text="Add Data",command=self.add_data,font=("arial",12,"bold"),width=18,bg="#a0ff00",fg="white")
        btnaDDdata.place(x=520,y=20)

        btnupdate=Button(self.root,text="Update",command=self.update,font=("arial",12,"bold"),width=18,bg="#a0ff00",fg="white")
        btnupdate.place(x=520,y=70)
        
        btndelete=Button(self.root,text="Delete",command=self.delete,font=("arial",12,"bold"),width=18,bg="#a0ff00",fg="white")
        btndelete.place(x=520,y=120)

        btnreset=Button(self.root,text="Reset",command=self.reset,font=("arial",12,"bold"),width=18,bg="#a0ff00",fg="white")
        btnreset.place(x=520,y=170)

        btnShowdata=Button(self.root,text="Show Data",command=self.show_data,font=("arial",12,"bold"),width=18,bg="#a0ff00",fg="white")
        btnShowdata.place(x=520,y=220)

        btnShowstatus=Button(self.root,text="Show Class Status",command=self.open_dashboard,font=("arial",12,"bold"),width=18,bg="#a0ff00",fg="white")
        btnShowstatus.place(x=300,y=280)
    def open_dashboard(self):
        self.new_window = Toplevel(self.root)  # Opens a new window
        self.app = Dashboard(self.new_window)
    

    # def add_data(self):
        
    #     conn=mysql.connector.connect(host="localhost",username="root",password='SQLPassword12#',database='itvedant')
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("Insert into leaderboard values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.id_Var,self.name_Var.get(),self.attendance.get(),self.assignment.get(),
    #                                                                                                     self.assessment.get(),
    #                                                                                                     self.Internal.get(),
    #                                                                                                     self.project.get(),
    #                                                                                                     self.CCE.get(),
    #                                                                                                     ))
    #     conn.commit()
    #     conn.close()
    #     self.fetch_data()
    #     tmsg.showinfo("Success","Memeber has been inserted successfully")
    def add_data(self):
        student_id=self.id_Var.get()
        name = self.name_Var.get().strip()
        attendance = self.attendance_var.get()
        assignment = self.assignment_var.get()
        assessment = self.assessment_var.get()
        internal_mock = self.Internal_mock_var.get()
        project_evaluation = self.project_var.get()
        cce_exam = self.CCE_var.get()
        # name = self.name_Var.get()
        # attendance = float(self.attendance_var.get())
        # assignment = float(self.assignment_var.get())
        # assessment = float(self.assessment_var.get())
        # internal_mock = float(self.Internal_mock_var.get())
        # project_evaluation = float(self.project_var.get())
        # cce_exam = float(self.CCE_var.get())
        
        
        if not all([name, attendance, assignment, assessment, internal_mock, project_evaluation, cce_exam]):
                tmsg.showerror("Error", "All fields are required!")
                return
        
        
        try:
            # Convert StringVar values to correct types
            # name = self.name_Var.get()
            attendance = float(attendance)
            assignment = float(assignment)
            assessment = float(assessment)
            internal_mock = float(internal_mock)
            project_evaluation = float(project_evaluation)
            cce_exam = float(cce_exam)
            

            
            conn=mysql.connector.connect(host="localhost",username="root",password='SQLPassword12#',database='itvedant')
            my_cursor=conn.cursor()
            # SQL query to insert data
            query = """
                INSERT INTO leaderboard (student_id,name, attendance, assignment, assessment, internal_mock, project_evaluation, cce_exam)
                VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
            """
            values = (student_id,name, attendance, assignment, assessment, internal_mock, project_evaluation, cce_exam)

            # Execute and commit
            my_cursor.execute(query, values)
            conn.commit()
            conn.close()
            self.fetch_data()
            tmsg.showinfo("Success","Memeber has been inserted successfully")

        except ValueError:
            tmsg.showinfo("Error","Please enter valid numeric values")
            # print("Please enter valid numeric values for scores.")
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")

        
    # def fetch_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password='SQLPassword12#',database='itvedant')
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("Select * from leaderboard")
    #     rows=my_cursor.fetchall()
    #     if len(rows)!=0:
    #         self.tree.delete(*self.tree.get_children())
    #         for i in rows:
    #             self.tree.insert("",END,values=i)
    #             conn.commit()
    #     conn.close()

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="SQLPassword12#",database="itvedant")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM leaderboard")
            rows = my_cursor.fetchall()  # Fetch all records

            conn.close()  # Close connection after fetching data

            return rows if rows else []  # Ensure it always returns a list

        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return []  # Return an empty list in case of failure


    def reset(self):
        self.id_Var.set(0)
        self.name_Var.set(""),
        self.attendance_var.set("") ,
        self.assignment_var.set(""),
        self.assessment_var.set(""), 
        self.Internal_mock_var.set(""),
        self.project_var.set(""),
        self.CCE_var.set("")
        
    def update(self):
        name = self.name_Var.get()
        attendance = float(self.attendance_var.get())
        assignment = float(self.assignment_var.get())
        assessment = float(self.assessment_var.get())
        internal_mock = float(self.Internal_mock_var.get())
        project_evaluation = float(self.project_var.get())
        cce_exam = float(self.CCE_var.get())        
        conn=mysql.connector.connect(host="localhost",username="root",password='SQLPassword12#',database='itvedant')
        my_cursor=conn.cursor()
        my_cursor.execute("update leaderboard set name=%s,attendance=%s,assignment=%s,assessment=%s,internal_mock=%s,project_evaluation=%s,cce_exam=%s where student_id=%s",
                                                                                                       (name,
                                                                                                        attendance,
                                                                                                        assignment,
                                                                                                        assessment,
                                                                                                        internal_mock,
                                                                                                        project_evaluation,
                                                                                                        cce_exam,
                                                                                                       self.id_Var.get()))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        tmsg.showinfo("Success","Memeber has been updated")
    

    

    
    def delete(self):
        if  self.id_Var.get()==0:
            tmsg.showerror("Error","First select the Student ID")
            return  # Stop execution here
    

        
        try:# Check if the student ID exists before deleting
            self.conn=mysql.connector.connect(host="localhost",username="root",password='SQLPassword12#',database='itvedant')
            self.my_cursor=self.conn.cursor()
            self.my_cursor.execute("SELECT * FROM leaderboard WHERE student_id = %s", (self.id_Var.get(),))
            record = self.my_cursor.fetchone()
            if not record:
                tmsg.showerror("Error", "Student ID not found!")
                return

            # Confirm deletion
            confirm = tmsg.askyesno("Confirm Delete", f"Are you sure you want to delete Student ID {self.id_Var.get()}?")
            if confirm:
                self.my_cursor.execute("DELETE FROM leaderboard WHERE student_id = %s", (self.id_Var.get(),))
                self.conn.commit()

                tmsg.showinfo("Success", "Record deleted successfully!")

                # **Refresh Treeview after deletion**
                self.show_data()

        except Exception as e:
              tmsg.showerror("Error", f"Database Error: {e}")

        # else:
        #     conn=mysql.connector.connect(host="localhost",username="root",password='SQLPassword12#',database='itvedant')
        #     my_cursor=conn.cursor()
        #     query="delete from leaderboard where student_id=%s"
        #     value=(self.id_Var.get(),)
        #     my_cursor.execute(query,value)

        #     self.fetch_data()
        #     conn.commit()
            
        #     self.reset()
        #     conn.close()
        #     tmsg.showinfo("Success","Member has been deleted")
    # def show_data(self):
    #     for item in self.tree.get_children():
    #         self.tree.delete(item)  # Clear old data
    
    #     rows = self.fetch_data()
    #     for row in rows:
    #         self.tree.insert('', END, values=row)

    def show_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)  # Clear old data

        rows = self.fetch_data()

        if not rows:  # Handle empty data case
            print("No data retrieved from the database.")
            return

        for row in rows:
            self.tree.insert('', 'end', values=row)

    
    

if __name__=="__main__":
    root=Tk()
    obj=ClassManagementSystem(root)
    root.mainloop()
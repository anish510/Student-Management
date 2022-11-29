from logging import setLogRecordFactory
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.tix import PopupMenu
from turtle import width
from tkinter import simpledialog
import pymysql


from matplotlib.pyplot import text

class Student():
    def __init__(self,root):#constructor# 

        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1600x900+0+0")
        title = Label(self.root,text="Student Management System",bd=9,font=("Roboto",50,"bold"),bg="TEAL",fg="WHITE")
        title.pack(side=TOP,fill=X)
        
        #-------all variables----#
        self.name_var=StringVar()
        self.roll_no_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #== MANAGE FRAMES ==
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="WHITE")
        Manage_Frame.place(x=10,y=120,width=480,height=728)

        m_title = Label(Manage_Frame,text="Manage Student",bg="white",fg="black",font=("Roboto",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_name = Label(Manage_Frame,text="Name",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_name.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_name = Entry(Manage_Frame,textvariable= self.name_var,font=("Roboto",15,),bd=5,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=10,padx=30,sticky="w")
        
        lbl_roll = Label(Manage_Frame,text="Roll No",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_roll.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_roll = Entry(Manage_Frame,textvariable= self.roll_no_var,font=("Roboto",15,),bd=5,relief=GROOVE)
        txt_roll.grid(row=2,column=1,pady=10,padx=30,sticky="w")
        
        lbl_dob = Label(Manage_Frame,text="D.O.B",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_dob = Entry(Manage_Frame,textvariable= self.dob_var,font=("Roboto",15),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=30,sticky="w")
        
        lbl_email = Label(Manage_Frame,text="Email",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_email = Entry(Manage_Frame,textvariable= self.email_var,font=("Roboto",15),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=30,sticky="w")
        
        lbl_contact = Label(Manage_Frame,text="Contact",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable= self.contact_var,font=("Roboto",15),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=30,sticky="w")
        
        lbl_gender = Label(Manage_Frame,text="Gender",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable= self.gender_var,font=("Roboto",14),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=30,pady=10,sticky='w')

        lbl_address = Label(Manage_Frame,text="Address",bg="WHITE",fg="BLACK",font=("Roboto",15,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address=Text(Manage_Frame,width=20,height=3,font=("Roboto",15),bd=5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,pady=10,padx=30,sticky="w")
        
    #========BUTTONS FRAME==========#
        
        btn_frame = Frame(Manage_Frame,bd=3,relief=RIDGE,bg="WHITE")
        btn_frame.place(x=1,y=650,width=470,height=70)

        Addbtn = Button(btn_frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,pady=10,padx=20,sticky="w")
        Updatebtn = Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,pady=15,padx=10,sticky="w")
        deletebtn = Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,pady=15,padx=10,sticky="w")
        clearbtn = Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,pady=20,padx=10,sticky="w")


   #== DETAILS FRAMES ==
        details_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="Light blue")
        details_Frame.place(x=500,y=120,width=1080,height=728)

        searchbtn = Button(details_Frame,text="Search",width=15,command=self.search_data).grid(row=0,column=3,pady=20,padx=200,sticky="w")
        showbtn = Button(details_Frame,text="Show All",width=15,command=self.fetch_data).grid(row=0,column=4,pady=20,padx=200,sticky="w")

    #======TABLE FRAME ============#
        table_frame = Frame(details_Frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=1,y=70,width=1070 ,height=650)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(table_frame,column=("name","roll","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill = Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="ROLL")
        self.Student_table.heading("name",text="NAME")
        self.Student_table.heading("email",text="EMAIL")
        self.Student_table.heading("gender",text="GENDER")
        self.Student_table.heading("contact",text="CONTACT")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="ADDRESS")
        
        self.Student_table['show']= 'headings'
        self.Student_table.column("roll", width=90)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=80)
        self.Student_table.column("contact", width=90)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    #---------add-data------------#   
    def add_student(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","all fields are required to fill")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="student management")
            cur=con.cursor()
            cur.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s)",(self.name_var.get(),
                                                                        self.roll_no_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END)
                                                                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success","Data entered")
    #---------show-all----------#        
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student management")
        cur=con.cursor() 
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close() 
        
    def clear(self):
        self.name_var.set("")
        self.roll_no_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
    
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.name_var.set(row[0])
        self.roll_no_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    #-------update-data-------------#
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student management")
        cur=con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_address.get('1.0',END),
            self.roll_no_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success","Data entered")
    #---------delete-data------------#
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student management")
        cur=con.cursor()
        cur.execute("delete from student where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear
        

    #-------search-by-roll-no--------#
    def search_data(self):
        x=simpledialog.askstring("Search","Enter Roll number")
        con=pymysql.connect(host="localhost",user="root",password="",database="student management")
        cur=con.cursor()
        cur.execute("select * from student where roll_no=%s",x)
        rows=cur.fetchall()
        if len(rows)!= 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
        else:
            messagebox.showerror("","No data with given Roll No.")    
            con.commit() 
        con.close() 

        
class Student():
    pass
    root= Tk()
    obj= Student(root)
    root.mainloop()
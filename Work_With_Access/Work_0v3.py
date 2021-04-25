from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import BOTH
from tkinter import END
from tkinter import HORIZONTAL
from tkinter import ttk
from tkinter.ttk import Combobox
import datetime
from tkinter import filedialog
import pyodbc as sqlMS
from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label
 

class GUI():
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        connStr = (
                   r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                   r"DBQ=C:\Users\savel\source\repos\Work_0\Work_0\Students.accdb;"
                   )
        self.conn = sqlMS.connect(connStr)
        self.cursor=self.conn.cursor()

    def Start_Win(self):
        self.list_row=list()
        self.win=Tk()
        self.win.title("Lab")
        self.win.geometry("720x720")
        self.win.resizable(False,False)
        self.file=list()

        lbl_ID=Label(self.win,text="Enter student ID",justify=CENTER)
        lbl_ID.grid(row=0)
        lbl_Fn=Label(self.win,text="Enter Firstname",justify=CENTER)
        lbl_Fn.grid(row=2)
        lbl_Sn=Label(self.win,text="Enter Surname",justify=CENTER)
        lbl_Sn.grid(row=4)
        lbl_Age=Label(self.win,text="Choose your Age",justify=CENTER)
        lbl_Age.grid(row=6)

        self.login_ID = Entry(self.win, width=30,name='txt')
        self.login_ID.grid(column=0,row=1)
        self.login_Fn= Entry(self.win, width=30,name='txt_1')
        self.login_Fn.grid(column=0,row=3)
        self.login_Sn = Entry(self.win, width=30,name='txt_2')
        self.login_Sn.grid(column=0,row=5)

        self.age = Scale(self.win,orient=HORIZONTAL ,length=300,from_=15,to=60,resolution=1)
        self.age.grid(column=0,row=7) 

        self.Degree = BooleanVar()
        self.cb = Checkbutton(self.win, text="Undergraduate\Graduate", variable=self.Degree)
        self.cb.grid(column=0,row=8)

        Add_in_list=Button(self.win, text="Add to Database", name="add to database", command=self.Add_to_list)
        Add_in_list.grid(column=0,row=9)
        Check_bd=Button(self.win, text="Check bd", name="check bd", command=self.Check_bd)
        Check_bd.grid(column=0,row=10)
        Quit=Button(self.win, text="Quit", name="quit", command=self.Quit_From_Prog)
        Quit.grid(column=0,row=11)
        Del=Button(self.win, text="Delete", name="del", command=self.delete)
        Del.grid(column=0,row=12)

        scrollbar = Scrollbar(self.win)
        scrollbar.place(x=694,y=10)

        self.lb = Listbox(yscrollcommand=scrollbar.set,height=40,width=60)
        self.lb.bind("<<ListboxSelect>>", self.onSelect)
        self.lb.place(x=330, y=10)
        scrollbar.config(command=self.lb.yview)

        self.win.mainloop()


    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.var.set(value)


    def Check_bd(self):
        self.lb.delete(0,'end')
        self.cursor.execute('select *from Students where ID>0')
        for i in self.cursor.fetchall():
            strin=''
            for elem in i:
                strin=strin+' '+str(elem)
            self.lb.insert(END, strin)

    def Quit_From_Prog(self):
        self.win.destroy()
    

    def upd(self):
        self.cursor.execute('''
                UPDATE Table_Name 
                SET Column1_Name = value1, Column2_Name = value2
                WHERE First_Name = 'Maria' (condition)
               ''')
        self.conn.commit()

    def delete(self):
        self.cursor.execute(''' 
                DELETE FROM Students
                WHERE ID >10
               ''')
        self.conn.commit()


    def Add_to_list(self):
        Age = str(self.age.get())
        Id=str(self.login_ID.get())
        Fname=str(self.login_Fn.get())
        Sname=str(self.login_Sn.get())
        Degree=str(self.Degree.get())
        #self.cursor.execute('SELECT TOP 1 * FROM Students ORDER BY ID DESC')
        #print(self.cursor.fetchall())
        self.cursor.execute('''
                    INSERT INTO Students (StudentID,Firstname,Surname,Degree,Age)
                    VALUES(?, ?, ?, ?, ?)''', (Id, Fname,Sname,Degree,Age))
        self.conn.commit()


    def scale_get():
        s1 = str(scal.get())


if __name__ == "__main__":
    obj4=GUI()
    obj4.Start_Win()    
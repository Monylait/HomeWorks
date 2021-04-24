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




class GUI():
    
    def __init__(self, *args, **kwargs):
        connStr = (
                   r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                   r"DBQ=C:\Users\savel\source\repos\Work_0\Work_0\TennisClub.mdb;"
                   )
        self.conn = sqlMS.connect(connStr)
        self.cursor=self.conn.cursor()

    def Start_Win(self):
        self.list_row=list()
        self.win=Tk()
        self.win.title("Lab")
        self.win.geometry("310x400")
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

        self.scal = Scale(self.win,orient=HORIZONTAL ,length=300,from_=15,to=60,resolution=1)
        self.scal.grid(column=0,row=7) 

        self.var = BooleanVar()
        self.cb = Checkbutton(self.win, text="Undergraduate\Graduate", variable=self.var)
        self.cb.grid(column=0,row=8)

        Add_in_list=Button(self.win, text="Add to Database", name="add to database", command=self.Add_to_list)
        Add_in_list.grid(column=0,row=9)
        Check_bd=Button(self.win, text="Check bd", name="check bd", command=self.Check_bd)
        Check_bd.grid(column=0,row=10)
        Quit=Button(self.win, text="Quit", name="quit", command=self.Quit_From_Prog)
        Quit.grid(column=0,row=11)

        self.win.mainloop()

    def Check_bd(self):
        self.cursor.execute('select *from Member where ID>0')
        for i in self.cursor.fetchall():
            print(i)

    def Quit_From_Prog(self):
        print("Quit")

    
    def upd(self):
        print("Update")

    def Add_to_list(self):
        print("work")
        


    def scale_get():
        s1 = str(scal.get())


if __name__ == "__main__":
    obj4=GUI()
    obj4.Start_Win()

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import END
from tkinter import HORIZONTAL
from tkinter.ttk import Combobox
import pypyodbc as sqlMS
from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label
 

class GUI(): 
    
    def __init__(self, *args, **kwargs):  # тут производится подключение к бд
        super().__init__()
        connStr = (
                   r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                   r"DBQ=C:\Users\savel\source\repos\Work_0\Work_0\Students.accdb;" #обязательно указывается абсолютный путь к файлу включая расширение
                   )
        self.conn = sqlMS.connect(connStr)   #конектимся с бд
        self.cursor=self.conn.cursor() #получаем курсор из бд, чтобы потом работать с бд

    def Start_Win(self): #мой стартовый метод, который и вызывается. тут производится создание и размещение всех эллементов программы
        self.win=Tk()
        self.win.title("Lab") # название программы отображается в верхнем левом углу
        self.win.geometry("720x720")  #размер программы
        self.win.resizable(False,False)

        canvas = Canvas()
        canvas.create_line(0, 25, 400, 25)
        canvas.place(x=0, y=250)

        lbl_ID=Label(self.win,text="Enter student ID",justify=CENTER)
        lbl_ID.grid(row=0)
        lbl_Fn=Label(self.win,text="Enter Firstname",justify=CENTER)
        lbl_Fn.grid(row=2)
        lbl_Sn=Label(self.win,text="Enter Surname",justify=CENTER)
        lbl_Sn.grid(row=4)
        lbl_Age=Label(self.win,text="Choose student's age",justify=CENTER)
        lbl_Age.grid(row=6)
        lbl_Info=Label(self.win,text="The program can check bd and show all results - Check Bd\n If you need, you can choose one note and delete it ->\nCreate your choose from list and press Delete\nThe Add to Database button use all elements upper.\n If user dont write there anything - in database create note\nwith empty cells",justify=CENTER)
        lbl_Info.place(x=10,y=280)

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
        Check_bd.place(x=580, y=660)
        Quit=Button(self.win, text="Quit", name="quit", command=self.Quit_From_Prog,background="#FF0000")
        Quit.place(x=660, y=660)
        Del=Button(self.win, text="Delete", name="del", command=self.delete,background="#FA8072")
        Del.place(x=158, y=230)
        Find=Button(self.win, text="Find", name="find", command=self.find)
        Find.place(x=103, y=230)

        scrollbar = Scrollbar(self.win)
        scrollbar.place(x=694,y=10)

        self.lb = Listbox(yscrollcommand=scrollbar.set,height=40,width=60,selectmode=SINGLE)
        self.lb.bind("<<ListboxSelect>>", self.onSelect)
        self.lb.place(x=330, y=10)
        scrollbar.config(command=self.lb.yview)


        self.win.mainloop()


    def onSelect(self, val):
        idx = self.lb.curselection()
        value = self.lb.get(idx)
        self.value=value.split()


    def find(self):
        self.cursor.execute(''' 
                SELECT * FROM Students
                WHERE StudentID=?
               ''', (str(self.login_ID.get())))     
        for i in self.cursor.fetchall():
            strin=''
            for elem in i:
                strin=strin+' '+str(elem)
            self.lb.insert(END, strin)


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
        if self.value==True:
            self.cursor.execute(''' 
                    DELETE FROM Students
                    WHERE StudentID=?
                   ''', (str(self.login_ID.get())))
            self.conn.commit()
        else:
            self.cursor.execute(''' 
                    DELETE FROM Students
                    WHERE StudentID=?
                   ''', (self.value[1]))
            self.conn.commit()
        Check_bd()


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


if __name__ == "__main__": #экранируем все что ниже этой строки чтобы не создать рекурсию - код запускает этот учатоск кода и создает себя же, где делает то же самое бесконечное ичсло раз
    obj4=GUI() # создаем объект класса GUI
    obj4.Start_Win()    #запускаем метод из этого класса - по факту запускаем приложение

import os
import multiprocessing as mp
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import BOTH
from tkinter import END
from tkinter import HORIZONTAL
from tkinter import ttk
from tkinter.ttk import Combobox

class GUI():


    def antiproblem(self):
        login=self.login
        file=self.file
        with mp.Pool(processes=1) as my_pool:
            self.p1=my_pool.starmap(self.read_csv_login,
                                    iterable=[
                                              [login,file]
                                             ]
                                    )
            my_pool.close


    def read_csv_login(self):
        self.list_row=list()
        i=0
        with open(self.file) as f:
           reader = csv.reader(f)
           for row in reader:
               if i>0 and row[3]==self.login:
                   rows=str()
                   check=0
                   for j in row:
                       if check==0:
                           rows=rows+j
                           check+=1
                       else:
                           rows=rows+","+j
                   rows=rows+"\n"
                   self.list_row.append(rows)
               elif i==0: 
                   self.start_row=row
                   i+=1
               else:pass
        p=list()
        p.append(self.list_row)
        p.append(self.start_row)
        return p


    def read_csv_Time(self,):
        self.list_row=list()
        i=0
        with open(self.file) as f:
            reader = csv.reader(f)
            for row in reader:
                if self.Time_check==0:
                    check=row[0]
                    if check>row[0]:
                        check=row[0]
                elif self.Time_check!=0:
                    pass
                else:pass

    def back_in_menu(self):
        lst=self.win.grid_slaves()
        for l in lst:
            l.destroy()
        a=self.win
        a.after(1000, lambda: a.destroy())
        self.Start_Win()


    def Start_Win(self):
        self.win=Tk()
        self.win.title("Lol")
        self.win.geometry("1360x480")
        check_list=[0]
        btn_1 = Button(self.win, text="поиск всех сессий по логину",name='btn_1', command=self.clicked_1)
        btn_1.grid(column=0, row=1)
        btn_2 = Button(self.win, text="поиск сессий в определенном временном диапазоне",name='btn_2', command=self.clicked_2)
        btn_2.grid(column=0, row=2)
        btn_3 = Button(self.win, text="фильтрация по длительности",name='btn_3', command=self.clicked_3)
        btn_3.grid(column=0, row=3)
        self.win.resizable(False,False)
        self.win.mainloop()


    def clicked_1(self):
        self.file=None
        lst=self.win.grid_slaves()
        for l in lst:
            if l.winfo_name()=='btn_2' or l.winfo_name()=='btn_3' or l.winfo_name()=='btn_1':
                l.destroy()
        lbl=Label(self.win,text="Введите логин",justify=CENTER)
        lbl.grid(row=0)
        self.login_en = Entry(self.win, width=30,name='txt')
        self.login_en.grid(column=0,row=1)
        lbl_2=Label(self.win,text="Enter way to file")
        lbl_2.grid(column=0,row=2)
        self.lbl_3=Label(self.win,text="File way...")
        self.lbl_3.grid(column=0,row=3)
        Browse_file=Button(self.win, text="browse", name="browse", command=self.way_file)
        Browse_file.grid(column=1,row=3)
        lbl_4=Label(self.win,text="Take num rows")
        lbl_4.grid(column=0,row=4)
        self.combo = Combobox(self.win,width=5)
        self.combo['values'] = (10, 20, 30)  
        self.combo.current(0)
        self.combo.grid(column=1, row=4)
        submit_txt=Button(self.win, text="next", name="next", command=self.check_param)
        submit_txt.grid(column=0,row=5)


    def clicked_2(self):
        self.file=None
        lst=self.win.grid_slaves()
        for l in lst:
            if l.winfo_name()=='btn_2' or l.winfo_name()=='btn_3' or l.winfo_name()=='btn_1':
                l.destroy()
        lbl=Label(self.win,text="Введите временной диапазон в формате c ДД ММ ГГ ЧЧ ММ СС по ДД ММ ГГ ЧЧ ММ СС",justify=CENTER)
        lbl.grid(row=0,columnspan=70)
        self.day = Entry(self.win, width=10)
        self.day.grid(column=1,row=1)
        self.month = Entry(self.win, width=10)
        self.month.grid(column=2,row=1)
        self.year = Entry(self.win, width=10)
        self.year.grid(column=3,row=1)
        self.hour = Entry(self.win, width=10)
        self.hour.grid(column=4,row=1)
        self.min = Entry(self.win, width=10)
        self.min.grid(column=5,row=1)
        self.sec = Entry(self.win, width=10)
        self.sec.grid(column=6,row=1)
        self.day_1 = Entry(self.win, width=10)
        self.day_1.grid(column=1,row=2)
        self.month_1 = Entry(self.win, width=10)
        self.month_1.grid(column=2,row=2)
        self.year_1 = Entry(self.win, width=10)
        self.year_1.grid(column=3,row=2)
        self.hour_1 = Entry(self.win, width=10)
        self.hour_1.grid(column=4,row=2)
        self.min_1 = Entry(self.win, width=10)
        self.min_1.grid(column=5,row=2)
        self.sec_1 = Entry(self.win, width=10)
        self.sec_1.grid(column=6,row=2)
        lbl_2=Label(self.win,text="Enter way to file")
        lbl_2.grid(column=0,row=3)
        self.lbl_3=Label(self.win,text="File way...")
        self.lbl_3.grid(column=0,row=4)
        Browse_file=Button(self.win, text="browse", name="browse", command=self.way_file)
        Browse_file.grid(column=1,row=4)
        lbl_4=Label(self.win,text="Take num rows")
        lbl_4.grid(column=0,row=5)
        self.combo = Combobox(self.win,width=5)
        self.combo['values'] = (10, 20, 30)  
        self.combo.current(0)
        self.combo.grid(column=1, row=5)
        submit_txt=Button(self.win, text="next", name="next", command=self.check_param)
        submit_txt.grid(column=0,row=6)


    def check_param(self):
        Errors=0
        self.login=self.login_en.get()
        if len(self.login)<1:
            messagebox.showinfo('Логин', 'обосрався')
            Errors+=1
        self.rows=int(self.combo.get())
        if self.rows==10 or self.rows==20 or self.rows==30:
            pass
        else: 
            messagebox.showinfo('Rows', 'обосрався')
            Errors+=1
        if  self.file!=None:
            pass
        else: 
            messagebox.showinfo('Way', 'обосрався')
            Errors+=1
        if Errors==0:
            self.finish_click_1()



            
    def check_param_2(self):
        Errors=0
        self.day=self.day.get()
        self.day=self.day.get()
        if len(self.login)<1:
            Errors+=1
        self.rows=int(self.combo.get())
        if self.rows==10 or self.rows==20 or self.rows==30:
            pass
        else: 
            messagebox.showinfo('Rows', 'обосрався')
            Errors+=1
        if  self.file!=None:
            pass
        else: 
            messagebox.showinfo('Way', 'обосрався')
            Errors+=1
        if Errors==0:
            self.finish_click_2()

    def clicked_3(self):
        messagebox.showinfo('функция', 'более не поддерживается')


    def way_file(self):
        self.file = filedialog.askopenfilename(filetypes = (("TXT files", "*.txt"),
                                                      ("HTML files", "*.html;*.htm"),
                                                      ("All files", "*.*") ))
        self.file_test=self.file.split(".")
        flag=True
        print(self.file)
        while flag:
            if self.file_test[-1]!="csv":
                    self.file = filedialog.askopenfilename(filetypes = (("TXT files", "*.txt"),
                                                          ("HTML files", "*.html;*.htm"),
                                                          ("All files", "*.*") ))
            else: flag=False
        self.lbl_3.configure(text=self.file)


            
    def finish_click_3(self):
        messagebox.showinfo('функция', 'более не поддерживается')


    def finish_click_2(self):
        messagebox.showinfo('функция', 'более не поддерживается')

    def output(self):
        self.console.configure(state='normal')
        text=''
        for i in range(0,self.rows):
            try:
                text=text+str(self.num)+"|"+self.list_row[i+self.rowrows]
                self.num+=1
            except IndexError:
                pass
        self.rowrows+=self.rows
        self.console.insert(END,text)
        self.console.yview(END)


    def save_result(self):
        text=""
        check=0
        for j in self.start_row:
            if check==0:
                text=text+j
                check+=1
            else:
                text=text+","+j
        text=text+"\n"
        with open("result.csv","w") as file:
            for i in self.list_row:
                text=text+i
            file.write(text)
        self.save=False

    def finish_click_1(self):
        lst=self.win.grid_slaves()
        for l in lst:
            l.destroy()
        self.read_csv_login()
        self.rowrows=0
        self.num=1
        print(len(self.list_row))
        ttk.Button(self.win, text='Вывести выбранное количество сессий',command=self.output).pack()
        ttk.Separator(self.win, orient=HORIZONTAL).pack(fill=BOTH)  # line in-between
        self.console = scrolledtext.ScrolledText(self.win,width=1360, state="disabled")
        self.console.pack()
        back=Button(self.win, text="back in menu", name="back", command=self.back_in_menu)
        back.pack()
        self.save=True
        if self.save!=False:
            back=Button(self.win, text="save result", command=self.save_result)
            back.pack()


obj4=GUI()
obj4.Start_Win()

#скролбара нет, когда водится дохуя строк все летит по пизде. Сделать не бесконечное нажатие строк - снять блокировку
#процесс для подгрузки лабы
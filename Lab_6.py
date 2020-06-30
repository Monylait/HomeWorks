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
import datetime



def read_csv_login(login,file):
    list_row=list()
    i=0
    with open(file) as f:
       reader = csv.reader(f)
       for row in reader:
           if i>0 and row[3]==login:
               rows=str()
               check=0
               for j in row:
                   if check==0:
                       rows=rows+j
                       check+=1
                   else:
                       rows=rows+","+j
               rows=rows+"\n"
               list_row.append(rows)
           elif i==0: 
               start_row=row
               i+=1
           else:pass
    p=list()
    p.append(list_row)
    p.append(start_row)
    return p


def read_csv(start,stop,file):
    list_row=list()
    i=0
    with open(file) as f:
       reader = csv.reader(f)
       print(start,stop)
       for row in reader:
           if i>0 and int(row[0])>=stop and int(row[1])<=start:
               rows=str()
               check=0
               for j in row:
                   if check==0:
                       rows=rows+j
                       check+=1
                   else:
                       rows=rows+","+j
               rows=rows+"\n"
               list_row.append(rows)
           elif i==0: 
               start_row=row
               i+=1
           else:pass
    p=list()
    p.append(list_row)
    p.append(start_row)
    return p


class GUI():


    def antiproblem(self):  
        login=self.login
        file=self.file
        with mp.Pool(processes=1) as my_pool:
            self.p1=my_pool.starmap(read_csv_login,
                                    iterable=[
                                              [login,file]
                                             ]
                                    ) 


    def antiproblem_2(self):  
        start=int(self.start)
        stop=int(self.stop)
        file=self.file
        with mp.Pool(processes=1) as my_pool:
            self.p1=my_pool.starmap(read_csv,
                                    iterable=[
                                              [start,stop,file]
                                             ]
                                    ) 
        

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
        self.win.title("Lab_6")
        self.win.geometry("1360x480")
        check_list=[0]
        btn_1 = Button(self.win, text="поиск всех сессий по логину",name='btn_1', command=self.clicked_1)
        btn_1.grid(column=0, row=1)
        btn_2 = Button(self.win, text="поиск сессий в определенном временном диапазоне",name='btn_2', command=self.clicked_2)
        btn_2.grid(column=0, row=2)
        self.win.resizable(False,False)
        self.win.mainloop()


    def clicked_1(self):
        self.file=None
        lst=self.win.grid_slaves()
        for l in lst:
            if l.winfo_name()=='btn_2' or l.winfo_name()=='btn_1':
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
        self.day_1_1 = Entry(self.win, width=10)
        self.day_1_1.grid(column=1,row=1)
        self.month_1_1 = Entry(self.win, width=10)
        self.month_1_1.grid(column=2,row=1)
        self.year_1_1 = Entry(self.win, width=10)
        self.year_1_1.grid(column=3,row=1)
        self.hour_1_1 = Entry(self.win, width=10)
        self.hour_1_1.grid(column=4,row=1)
        self.min_1_1 = Entry(self.win, width=10)
        self.min_1_1.grid(column=5,row=1)
        self.sec_1_1 = Entry(self.win, width=10)
        self.sec_1_1.grid(column=6,row=1)
        self.day_2 = Entry(self.win, width=10)
        self.day_2.grid(column=1,row=2)
        self.month_2 = Entry(self.win, width=10)
        self.month_2.grid(column=2,row=2)
        self.year_2 = Entry(self.win, width=10)
        self.year_2.grid(column=3,row=2)
        self.hour_2 = Entry(self.win, width=10)
        self.hour_2.grid(column=4,row=2)
        self.min_2 = Entry(self.win, width=10)
        self.min_2.grid(column=5,row=2)
        self.sec_2 = Entry(self.win, width=10)
        self.sec_2.grid(column=6,row=2)
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
        submit_txt=Button(self.win, text="next", name="next", command=self.check_param_2)
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
        self.day_1=self.day_1_1.get()
        self.month_1=self.month_1_1.get()
        self.year_1=self.year_1_1.get()
        self.hour_1=self.hour_1_1.get()
        self.min_1=self.min_1_1.get()
        self.sec_1=self.sec_1_1.get()
        self.day_2=self.day_2.get()
        self.month_2=self.month_2.get()
        self.year_2=self.year_2.get()
        self.hour_2=self.hour_2.get()
        self.min_2=self.min_2.get()
        self.sec_2=self.sec_2.get()
        try:
            if int(self.day_1)<31 and int(self.day_1)>0 and int(self.day_2)<31 and int(self.day_2)>0:
                pass
            else:
                messagebox.showinfo('Days', 'обосрався')
            if int(self.month_1)<13 and int(self.month_1)>0 and int(self.month_2)<13 and int(self.month_2)>0:
                pass
            else:
                messagebox.showinfo('Month', 'обосрався')
            if int(self.year_1)<3000 and int(self.year_1)>1969 and int(self.year_2)<3000 and int(self.year_2)>1969 and int(self.year_1)>=int(self.year_2):
                pass
            else:
                messagebox.showinfo('Years', 'обосрався')
            if int(self.hour_1)<25 and int(self.hour_1)>-1 and int(self.hour_2)<25 and int(self.hour_2)>-1:
                pass
            else:
                messagebox.showinfo('Hours', 'обосрався')
            if int(self.min_1)<60 and int(self.min_1)>-1 and int(self.min_2)<60 and int(self.min_2)>-1:
                pass
            else:
                messagebox.showinfo('Mins', 'обосрався')
            if int(self.sec_1)<60 and int(self.sec_1)>-1 and int(self.sec_2)<60 and int(self.sec_2)>-1:
                pass
            else:
                messagebox.showinfo('Secs', 'обосрався')
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
        except Exception:
            messagebox.showinfo('Problem with time', 'обосрався')
            Errors+=1
        if Errors==0:
            print("lol")
            check_1=datetime.datetime(int(self.year_1),int(self.month_1),int(self.day_1), int(self.hour_1),int(self.min_1),int(self.sec_1))
            check_2=datetime.datetime(int(self.year_2),int(self.month_2),int(self.day_2), int(self.hour_2),int(self.min_2),int(self.sec_2))
            self.start=datetime.datetime(int(self.year_1),int(self.month_1),int(self.day_1), int(self.hour_1),int(self.min_1),int(self.sec_1)).timestamp()
            self.stop=datetime.datetime(int(self.year_2),int(self.month_2),int(self.day_2), int(self.hour_2),int(self.min_2),int(self.sec_2)).timestamp()
            if self.start<self.stop:
                messagebox.showinfo('Data wrong - start<stop', 'обосрався')
                Errors+=1
            if Errors==0:
                self.finish_click_2()


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


    def finish_click_2(self):
        lst=self.win.grid_slaves()
        for l in lst:
            l.destroy()
        self.antiproblem_2()
        self.rowrows=0
        self.num=1
        p=self.p1[0] 
        self.list_row=p[0]
        self.start_row=p[1] 
        ttk.Button(self.win, text='Вывести выбранное количество сессий',command=self.output).pack()
        ttk.Separator(self.win, orient=HORIZONTAL).pack(fill=BOTH)  
        self.console = scrolledtext.ScrolledText(self.win,width=1360, state="disabled")
        self.console.pack()
        back=Button(self.win, text="back in menu", name="back", command=self.back_in_menu)
        back.pack()
        self.save=True
        if self.save!=False:
            back=Button(self.win, text="save result", command=self.save_result)
            back.pack()

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
        self.antiproblem()
        self.rowrows=0
        self.num=1
        print(self.p1)
        p=self.p1[0]
        self.list_row=p[0]
        self.start_row=p[1]
        ttk.Button(self.win, text='Вывести выбранное количество сессий',command=self.output).pack()
        ttk.Separator(self.win, orient=HORIZONTAL).pack(fill=BOTH)
        self.console = scrolledtext.ScrolledText(self.win,width=1360, state="disabled")
        self.console.pack()
        back=Button(self.win, text="back in menu", name="back", command=self.back_in_menu)
        back.pack()
        self.save=True
        if self.save!=False:
            back=Button(self.win, text="save result", command=self.save_result)
            back.pack()

if __name__=="__main__":
    obj4=GUI()
    obj4.Start_Win()
     
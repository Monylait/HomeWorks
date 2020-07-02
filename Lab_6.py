import os
import multiprocessing as mp
import csv
import asyncio
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


def read_csv(login:str,file:list,start:int,stop:int,status:int)->list:
    list_row=list()
    time_list=list()
    first_row=0
    print(status)
    for file_from_directory in file:
        start_row=""
        with open(file_from_directory) as f:
            time_list=list()
            reader = csv.reader(f)
            for row in reader: 
                    if status==1:
                        try:
                            if first_row>0 and row[3]==login:
                                rows=str()
                                first_ellem=0
                                for j in row:
                                    if first_ellem==0:
                                        rows=rows+str(j)
                                        first_ellem+=1
                                    else:
                                        rows=rows+","+str(j)
                                rows=rows+"\n"
                                time_list.append(rows)
                            elif first_row==0: 
                                for j in row:
                                    if first_row==0:
                                        start_row=start_row+str(j)
                                        first_row+=1
                                    else:
                                        start_row=start_row+","+str(j)
                                start_row=start_row+"\n"
                                time_list.append(start_row)
                        except Exception:
                            messagebox.showinfo("Сейчас обрабатывается", file_from_directory)
                    elif status==2:
                        try:
                            if first_row>0 and int(row[0])>=int(stop) and int(row[1])<=int(start):
                                rows=str()
                                first_ellem=0
                                for j in row:
                                    if first_ellem==0:
                                        rows=rows+str(j)
                                        first_ellem+=1
                                    else:
                                        rows=rows+","+str(j)
                                rows=rows+"\n"
                                time_list.append(rows)
                            elif first_row==0: 
                                for j in row:
                                    if first_row==0:
                                        start_row=start_row+str(j)
                                        first_row+=1
                                    else:
                                        start_row=start_row+","+str(j)
                                start_row=start_row+"\n"
                                time_list.append(start_row)
                        except Exception:
                            messagebox.showinfo("Сейчас обрабатывается", file_from_directory)
        list_row=list_row+time_list
    p=list()
    p.append(list_row)
    p1=list()
    p1.append(p)
    return p1


def save_result(list_row,i):
    text=""
    print("Start save")
    with open("result.csv","w") as file:
        for i in list_row:
            text=text+i
        file.write(text)
    messagebox.showinfo("Успех", "Успешно сохранено в файле result.csv")


#async def antiproblem(status,login,file,start,stop): 
#        print("antiproblem")
#        if status==1:
#            log=login
#            fil=file
#            star=0
#            sto=0
#        if status==2:
#            log=""
#            fil=file
#            star=int(start)
#            sto=int(stop)
#        with mp.Pool(processes=1) as my_pool:
#            p1=my_pool.starmap(read_csv,
#                                    iterable=[
#                                              [log,fil,star,sto,status]
#                                             ]
#                                    ) 
#        return p1
        


class GUI():

    def __init__(self):
        self.my_pool=mp.Pool(1)
        self.my_pool_save=mp.Pool(1)

    def back_in_menu(self):
        lst=self.win.grid_slaves()
        for l in lst:
            l.destroy()
        a=self.win
        a.after(1000, lambda: a.destroy())
        self.Start_Win()


    def Start_Win(self):
        self.list_check=0
        self.list_row=list()
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
        self.file=list()
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
        self.file=list()
        lst=self.win.grid_slaves()
        for l in lst:
            if l.winfo_name()=='btn_2' or l.winfo_name()=='btn_3' or l.winfo_name()=='btn_1':
                l.destroy()
        lbl=Label(self.win,text="Введите временной диапазон в формате до ДД ММ ГГ ЧЧ ММ СС с ДД ММ ГГ ЧЧ ММ СС",justify=CENTER)
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
        time=0
        func_start=0
        self.login=self.login_en.get()
        if len(self.login)<1:
            messagebox.showinfo('Логин', 'incorrect')
            Errors+=1
        self.rows=int(self.combo.get())
        if self.rows==10 or self.rows==20 or self.rows==30:
            time+=1
        else: 
            messagebox.showinfo('Rows', 'incorrect')
            Errors+=1
        if  self.file!=None and time==1:
            self.my_pool.apply_async(func=read_csv,args=("",self.file,0,0,1),callback=self.table_data) 
            func_start=1
        else: 
            messagebox.showinfo('Way', 'incorrect')
            Errors+=1
        if Errors==0 and func_start==1:
            self.finish_click(1)

            
    def check_param_2(self):
        Errors=0
        self.day_1=self.day_1_1.get()
        self.month_1=self.month_1_1.get()
        self.year_1=self.year_1_1.get()
        self.hour_1=self.hour_1_1.get()
        self.min_1=self.min_1_1.get()
        self.sec_1=self.sec_1_1.get()
        self.day_2_1=self.day_2.get()
        self.month_2_1=self.month_2.get()
        self.year_2_1=self.year_2.get()
        self.hour_2_1=self.hour_2.get()
        self.min_2_1=self.min_2.get()
        self.sec_2_1=self.sec_2.get()
        time=0
        func_start=0
        try:
            if int(self.day_1)<31 and int(self.day_1)>0 and int(self.day_2_1)<31 and int(self.day_2_1)>0:
                time+=1
            else:
                messagebox.showinfo('Days', 'incorrect')
            if int(self.month_1)<13 and int(self.month_1)>0 and int(self.month_2_1)<13 and int(self.month_2_1)>0:
                time+=1
            else:
                messagebox.showinfo('Month', 'incorrect')
            if int(self.year_1)<3000 and int(self.year_1)>1969 and int(self.year_2_1)<3000 and int(self.year_2_1)>1969 and int(self.year_1)>=int(self.year_2_1):
                time+=1
            else:
                messagebox.showinfo('Years', 'incorrect')
            if int(self.hour_1)<25 and int(self.hour_1)>-1 and int(self.hour_2_1)<25 and int(self.hour_2_1)>-1:
                time+=1
            else:
                messagebox.showinfo('Hours', 'incorrect')
            if int(self.min_1)<60 and int(self.min_1)>-1 and int(self.min_2_1)<60 and int(self.min_2_1)>-1:
                time+=1
            else:
                messagebox.showinfo('Mins', 'incorrect')
            if int(self.sec_1)<60 and int(self.sec_1)>-1 and int(self.sec_2_1)<60 and int(self.sec_2_1)>-1:
                time+=1
            else:
                messagebox.showinfo('Secs', 'incorrect')
            self.rows=int(self.combo.get())
            if time==6:
                self.start=datetime.datetime(int(self.year_1),int(self.month_1),int(self.day_1), int(self.hour_1),int(self.min_1),int(self.sec_1)).timestamp()
                self.stop=datetime.datetime(int(self.year_2_1),int(self.month_2_1),int(self.day_2_1), int(self.hour_2_1),int(self.min_2_1),int(self.sec_2_1)).timestamp()
            if self.rows==10 or self.rows==20 or self.rows==30:
                pass
            else: 
                messagebox.showinfo('Rows', 'incorrect')
                Errors+=1
            if  self.file!=None and time==6:
                self.my_pool.apply_async(func=read_csv,args=("",self.file,self.start,self.stop,2),callback=self.table_data) 
                func_start=1
            else: 
                messagebox.showinfo('Way', 'incorrect')
                Errors=1         
        except Exception:
            messagebox.showinfo('Problem with time', 'incorrect')
            Errors+=1
        if Errors==0 and func_start==1:
            if self.start<self.stop:
                messagebox.showinfo('Data wrong - start<stop', 'incorrect')
                Errors+=1
            if Errors==0:
                self.finish_click(2)


    def way_file(self):
        directory=filedialog.askdirectory()
        file=os.listdir(directory)
        j=0
        print(directory,file)
        for i in file:
            j=i.split(".")
            if j[-1]=="csv":
                i_1=os.path.join(directory,i)
                print(i_1)
                self.file.append(i_1)
        print(self.file)
        if len(file)<1:
            messagebox.showinfo('Havent files', 'Error')
        else: 
            self.lbl_3.configure(text="we have directory and see files")

    def table_data(self,p):
        p1=p[0] 
        self.list_row=p1[0]
        self.list_check=1


    def output(self):
        if len(self.list_row)>0 and len(self.list_row)<self.rows:
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
        else:
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


    def try_save(self):
        if self.list_check==1:
            print(self.list_row)
            self.my_pool_save.apply_async(func=save_result,args=(self.list_row,0)) 
        else:
            messagebox.showinfo('Сant save', 'We not finished read files,pleas wait')


    def finish_click(self,status):
        lst=self.win.grid_slaves()
        for l in lst:
            l.destroy()
        self.rowrows=0
        self.num=1
        ttk.Button(self.win, text='Вывести выбранное количество сессий',command=self.output).pack()
        ttk.Separator(self.win, orient=HORIZONTAL).pack(fill=BOTH)
        self.console = scrolledtext.ScrolledText(self.win,width=1360, state="disabled")
        self.console.pack()
        back=Button(self.win, text="back in menu", name="back", command=self.back_in_menu)
        back.pack()
        back=Button(self.win, text="save result",name="save", command=self.try_save)
        back.pack()


if __name__ == "__main__":
    obj4=GUI()
    obj4.Start_Win()







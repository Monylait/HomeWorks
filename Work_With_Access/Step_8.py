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
        self.win=Tk()
        self.win.title("Lab")
        self.win.geometry("200x200")
        self.win.resizable(False,False)

    def Start_Win(self):
        self.texts = Entry(self.win, width=30,name='txt')
        self.texts.pack()
        Check=Button(self.win, text="Check", name="check bd", command=self.onSelect)
        Check.pack()
        self.label = Label(text=None)
        self.label.pack()
        self.win.mainloop()
   
    def onSelect(self):
        var = str(self.texts.get())
        self.label.destroy()
        self.label = Label(text=var)
        self.label.pack()
 

if __name__ == "__main__":
    obj=GUI()
    obj.Start_Win()
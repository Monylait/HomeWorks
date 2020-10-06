import pymongo
from pymongo import MongoClient
import datetime
import pprint
import csv
import timeit
import os 
import multiprocessing as mp
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget,QDialog,QVBoxLayout,QComboBox,QFileDialog, QTableWidget,QTableWidgetItem
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets
import PySide2.QtCore as QtCore 
from PySide2.QtCore import QFileInfo

client=MongoClient('localhost', 27017)
db = client['test-database']
posts=db.postsers
db.posts.create_index("nik")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab_8")
        self.setSize() 
        self.setIcon()
        self.center()
        self.setButtons()
        self.Help_Button()
        self.Search_Button()
        self.setFontBox()
        self.Table()


    def center(self):
        qRect=self.frameGeometry()
        centerPoint=QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


    def setSize(self):
        self.setGeometry(0,0,800,720)
        self.setMinimumHeight(720)
        self.setMinimumWidth(800)
        self.setMaximumHeight(720)
        self.setMaximumWidth(800)
 
     
    def setIcon(self):
        appIcon= QIcon("3.jpg")
        self.setWindowIcon(appIcon)


    def setButtons(self):
        Browse_Button=QPushButton("Browse",self)
        Browse_Button.move(25,640)
        Browse_Button.clicked.connect(self.File_path)



    def File_path(self):
        self.dialog = QFileDialog(self)
        self.path=self.dialog.getOpenFileName()
        self.fi=QFileInfo(self.path[0])
        self.FileSize=self.fi.size()
        parsing(self.path[0],self.FileSize)
        self.FileSize=self.fi.size()
    
        
    def New_Window_Message(self):
        userinfo = QMessageBox.question(self,"COnfirme", "Do u?",QMessageBox.Yes,QMessageBox.No)
        if userinfo==QMessageBox.Yes:
            print("Yes")
        if userinfo==QMessageBox.No:
            print("No")

    
    def Help_Button(self):
        self.aboutButton=QPushButton("Open About",self)
        self.aboutButton.move(681,670)
        self.aboutButton.clicked.connect(self.aboutBox)


    def printfel(self,x):
        if x==0:
            print("One")
        elif x==1:
            print("Two")
        elif x==2:
            print("Three")
    
            
    def Search_Button(self):
        self.Search_button=QPushButton("Accept and Search",self)
        self.Search_button.move(197,669)
        self.Search_button.clicked.connect(self.aboutBox)


    def Table(self):
        self.tableWidget =QTableWidget(self)
        self.tableWidget.setColumnCount(7)
        self.Set_Count_Lists_In_Table()
        self.tableWidget.setRowCount(100)  
        self.tableWidget.move(25,7)
        self.tableWidget.setMinimumHeight(600)
        self.tableWidget.setMinimumWidth(750)
        self.tableWidget.setMaximumHeight(600)
        self.tableWidget.setMaximumWidth(750)
        self.tableWidget.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3","Header 4", "Header 5", "Header 6","Header 7"])
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Системный номер"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("random_name0"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("random_fname0"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("random_phone0"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("928641057"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("WeB_BackenD"))
        self.tableWidget.setItem(0, 6, QTableWidgetItem("0118532866300"))
        



    def aboutBox(self):
        QMessageBox.about(self.aboutButton,"about menu","About text more text")


    def Set_Count_Lists_In_Table(self):
            cbox  = QComboBox(self)
            size=db.posts.find().count() 
            lists_in_table=list()
            for i in range(1,size):
                lists_in_table.append(str(i))
            tables=(lists_in_table)
            cbox.addItems(tables)
            cbox.move(26,670)
            cbox.currentIndexChanged.connect(self. printfel)


    def setFontBox(self):
        cbox  = QComboBox(self)
        tables=("Поиск по нику","Поиск по телефону","Поиск по члену")
        cbox.addItems(tables)
        cbox.move(26,670)
        cbox.currentIndexChanged.connect(self. printfel)


def append_collection(Document):

    post = {"Number": Document[0],
        "name": Document[1],
        "fname": Document[2],
        "phone": Document[3],
        "uid":Document[4],
        "nik":Document[5],
        "wo":Document[6]
        }
    post_id=posts.insert_one(post).inserted_id


def parsing(path,File_Size):
    j=0
    j_row=''
    a = timeit.default_timer()
    with open(path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            Document=list()
            if j!=9:
                j_row+=row[0]
            if j==9:
                avg_time=timeit.default_timer()-a
                size=(int(File_Size)/(int(len(j_row.encode('utf-8'))/10)))
                avg_time=avg_time*size
                print(">>>>>>>>>>>>>>>>>> size",size/3600)
            row=row[0].split("|")
            for i in range(1,8):
                Document.append(row[i])
            append_collection(Document)
            print(j)
            j+=1
    
    print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")


    
myApp=QApplication(sys.argv)
window=Window()
window.show()
myApp.exec_()

sys.exit(0)

       
import pymongo
from pymongo import MongoClient
import datetime
import pprint
import csv
import timeit
import os 
import multiprocessing as mp
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget,QDialog,QVBoxLayout,QComboBox,QFileDialog, QTableWidget,QTableWidgetItem,QLineEdit,QInputDialog,QProgressBar
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets
import PySide2.QtCore as QtCore 
from PySide2.QtCore import QFileInfo
import multiprocessing
from threading import Thread
import queue
import time



client=MongoClient('localhost', 27017)
db = client['test-database']
posts=db.postsers
db.posts.create_index("Number")#,"name","fname","phone","uid","nik","wo"])



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
        self.choose=0
        self.point=0
        self.point_check=0
        self.result={"Системный номер","random_name0","random_fname0","random_phone0","928641057","WeB_BackenD","0118532866300"}


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

    def CreateNewDoc(self):
         number,ok = QInputDialog.getText(self, 'Input Dialog',
                'Write Number:')
         if ok:
             name,ok = QInputDialog.getText(self, 'Input Dialog',
                'Write name:')
             if ok:
                fname,ok = QInputDialog.getText(self, 'Input Dialog',
                'Write fname:')
                if ok:
                     phone,ok = QInputDialog.getText(self, 'Input Dialog',
                     'Write phone:')
                     if ok:
                         uid,ok = QInputDialog.getText(self, 'Input Dialog',
                         'Write uid:')
                         if ok:
                            nik,ok = QInputDialog.getText(self, 'Input Dialog',
                            'Write nik:')
                            if ok:
                                wo,ok = QInputDialog.getText(self, 'Input Dialog',
                                'Write wo:')
                                if ok:
                                    post = {
                                    "Number": number,
                                    "name": name,
                                    "fname": fname,
                                    "phone": phone,
                                    "uid": uid,
                                    "nik": nik,
                                    "wo": wo
                                     }
                                    post_id=posts.insert_one(post).inserted_id


    def setButtons(self):
        Create_Doc=QPushButton("Create",self)
        Browse_Button=QPushButton("Browse",self)
        Browse_Button.move(24,649)
        Create_Doc.move(101,649)
        Browse_Button.clicked.connect(self.File_path)
        Create_Doc.clicked.connect(self.CreateNewDoc)


    def File_path(self):
        self.dialog = QFileDialog(self)
        self.path=self.dialog.getOpenFileName()
        self.fi=QFileInfo(self.path[0])
        self.FileSize=self.fi.size()
        self.point-=1
        self.qe = queue.Queue()
        self.thread1 = Thread(target=parsing, args=(self.path[0], self.FileSize,self.qe))
        self.thread1.start()
        QtCore.QTimer.singleShot(1000,self.TimerQ)


    def TimerQ(self):
        j=0
        self.result=posts.find()
        for i in self.result:
                if self.point==-1:
                    if i:
                        self.tableWidget.setItem(j, 0, QTableWidgetItem(i['Number']))
                        self.tableWidget.setItem(j, 1, QTableWidgetItem(i['name']))
                        self.tableWidget.setItem(j, 2, QTableWidgetItem(i['fname']))
                        self.tableWidget.setItem(j, 3, QTableWidgetItem(i['phone']))
                        self.tableWidget.setItem(j, 4, QTableWidgetItem(i['uid']))
                        self.tableWidget.setItem(j, 5, QTableWidgetItem(i['nik']))
                        self.tableWidget.setItem(j, 6, QTableWidgetItem(i['wo']))
                        j+=1
                    else:
                        break
                    if j==100:
                        self.point=0
                        self.point_check=100
                        break
        QMessageBox.warning(self.Back,"Warning!","База данных еще загружается, все функции кроме просмотра - заблокированы",buttons=QMessageBox.Ok)
 
       
    def ProgressBar(self):
        i=0
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.progressbar=QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.move(200,675)
        while self.thread1.is_alive():
            n = self.qe.get()
            i+=1
            self.progressbar.setValue(i)


    #def New_Window_Message(self):
    #    userinfo = QMessageBox.question(self,"COnfirme", "Do u?",QMessageBox.Yes,QMessageBox.No)
    #    if userinfo==QMessageBox.Yes:
    #        print("Yes")
    #    if userinfo==QMessageBox.No:
    #        print("No")

    
    def Help_Button(self):
        self.aboutButton=QPushButton("Open About",self)
        self.aboutButton.move(701,675)
        self.aboutButton.clicked.connect(self.aboutBox)


    def printfel(self,x):
        if x==0:
            self.choose=x
        elif x==1:
            self.choose=x
        elif x==2:
            self.choose=x
    
            
    def Search_Button(self):
        self.Search_button=QPushButton("Accept and Search",self)
        self.Search_button.move(152,674)
        self.Search_button.clicked.connect(self.Enter_nick)


    def Table(self):
        self.tableWidget =QTableWidget(self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(100)  
        self.tableWidget.move(25,7)
        self.tableWidget.setMinimumHeight(600)
        self.tableWidget.setMinimumWidth(750)
        self.tableWidget.setMaximumHeight(600)
        self.tableWidget.setMaximumWidth(750)
        self.tableWidget.setHorizontalHeaderLabels(["Number", "name", "fname","phone", "uid", "nik","wo"])
        self.NextButton_Back()


    def setTable(self):
        j=0
        print("start")
        self.tableWidget.clearContents()
        for i in self.result:
                    self.tableWidget.setItem(j, 0, QTableWidgetItem(i['Number']))
                    self.tableWidget.setItem(j, 1, QTableWidgetItem(i['name']))
                    self.tableWidget.setItem(j, 2, QTableWidgetItem(i['fname']))
                    self.tableWidget.setItem(j, 3, QTableWidgetItem(i['phone']))
                    self.tableWidget.setItem(j, 4, QTableWidgetItem(i['uid']))
                    self.tableWidget.setItem(j, 5, QTableWidgetItem(i['nik']))
                    self.tableWidget.setItem(j, 6, QTableWidgetItem(i['wo']))
                    j+=1
                    if j==100:
                        break


    def NextButton_Back(self):
        self.Next=QPushButton("Next >>",self)
        self.Back=QPushButton("<< Back",self)
        self.Next.move(400,610)
        self.Back.move(330,610)
        self.Next.clicked.connect(self.point_plus)
        self.Back.clicked.connect(self.point_minus)
        
    def point_plus(self):
        self.point+=1
        self.setTable()

    def point_minus(self):
        if self.point<1:
            QMessageBox.warning(self.Back,"Warning!","We cant go back",buttons=QMessageBox.Ok)
        else:
            self.point-=1
            self.setTable()

    def search(self): #dont work need rework
        result = find_document(series_collection, {'name': 'FRIENDS'})
        print(result)
        delete_document(series_collection, {'_id': id_})


    def aboutBox(self):
        QMessageBox.about(self.aboutButton,"about menu","About text more text")


    def Enter_nick(self):
        if self.choose==0:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for Number:')
        elif self.choose==1:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for name:')
        elif self.choose==2:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for fname:')
        elif self.choose==3:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for phone:')
        elif self.choose==4:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for uid:')
        elif self.choose==5:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for nik:')
        elif self.choose==6:
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                'Search for wo:')

        if ok:
            if self.choose==0:
                self.result=posts.find({"Number":str(text)})
            elif self.choose==1:
                self.result=posts.find({"name":str(text)})
            elif self.choose==2:
                self.result=posts.find({"fname":str(text)})
            elif self.choose==3:
                self.result=posts.find({"phone":str(text)})
            elif self.choose==4:
                self.result=posts.find({"uid":str(text)})
            elif self.choose==5:
                self.result=posts.find({"nik":str(text)})
            elif self.choose==6:
                self.result=posts.find({"wo":str(text)})
            j=0
            self.tableWidget.clearContents()
            for i in self.result:
                self.tableWidget.setItem(j, 0, QTableWidgetItem(i['Number']))
                self.tableWidget.setItem(j, 1, QTableWidgetItem(i['name']))
                self.tableWidget.setItem(j, 2, QTableWidgetItem(i['fname']))
                self.tableWidget.setItem(j, 3, QTableWidgetItem(i['phone']))
                self.tableWidget.setItem(j, 4, QTableWidgetItem(i['uid']))
                self.tableWidget.setItem(j, 5, QTableWidgetItem(i['nik']))
                self.tableWidget.setItem(j, 6, QTableWidgetItem(i['wo']))
                j+=1


    def setFontBox(self): #####################################################поиск по нику и телефону не робит - не робит дальше фамилии
        cbox  = QComboBox(self)
        tables=("Поиск по номеру","Поиск по имени","Поиск по фамилии","Поиск по телефону","Поиск по uid","Поиск по нику","Поиск по wo")
        cbox.addItems(tables)
        cbox.move(25,676)
        cbox.currentIndexChanged.connect(self.printfel)





def parsing(path,File_Size,q):
    j=1
    j_row=''
    size=int(File_Size/185)
    precent=int(size/100)
    a = timeit.default_timer()
    with open(path, "r", newline="") as file:
        flag=False
        reader = csv.reader(file)
        first_row=file.readline()
        for row in reader:
            Document=list()
            row=row[0].split("|")
            for i in range(1,8):
                Document.append(row[i])
            post = {
                   "Number": Document[0],
                   "name": Document[1],
                   "fname": Document[2],
                   "phone": Document[3],
                   "uid":Document[4],
                   "nik":Document[5],
                   "wo":Document[6]
                    }
            post_id=posts.insert_one(post).inserted_id
            j+=1
            if j==precent:
                flag=True
                q.put_nowait(flag)

    print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")


myApp=QApplication(sys.argv)
window=Window()
window.show()
myApp.exec_()

sys.exit(0)

       
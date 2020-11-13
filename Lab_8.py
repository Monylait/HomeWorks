import pymongo
from pymongo import MongoClient
import csv
import timeit
import os 
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
import bson




FONT = "FreeSansBold.ttf"

client=MongoClient('localhost', 27017)
db = client['test-database']
posts=db.postsers
db.posts.create_index("nik")
db.posts.create_index("phone")
db.posts.create_index("fname")


stop_threads = False


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
        self.point=0
        self.point_check=0
        self.result={"Системный номер","random_name0","random_fname0","random_phone0","928641057","WeB_BackenD","0118532866300"}
        self.back=False



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

    
    def EdditDoc(self):
        pass

    def setButtons(self):
        Create_Doc=QPushButton("Create",self)
        Browse_Button=QPushButton("Browse",self)
        self.Stop_But=QPushButton("Stop Parsing",self)
        self.Update_Data=QPushButton("Update Data",self)
        Browse_Button.move(24,649)
        Create_Doc.move(99,649)
        self.Stop_But.move(174,649)
        self.Update_Data.move(174,624)
        self.Stop_But.setDisabled(True)
        self.Update_Data.setDisabled(True)
        Browse_Button.clicked.connect(self.File_path)
        Create_Doc.clicked.connect(self.CreateNewDoc)
        self.Update_Data.clicked.connect(self.change)
 
   
    def File_path(self):
        try:
            self.dialog = QFileDialog(self)
            self.path=self.dialog.getOpenFileName()
            self.fi=QFileInfo(self.path[0])
            self.FileSize=self.fi.size()
            self.point-=1
            self.thread1 = Thread(target=parsing, args=(self.path[0], self.FileSize))
            stop_threads = False
            self.thread1.start()
            time.sleep(0.5)
            QMessageBox.warning(self.Back,"Warning!","База данных еще загружается, все функции кроме просмотра - заблокированы",buttons=QMessageBox.Ok)
            time.sleep(2)
            self.StopButton()
            self.TimerQ()
        except FileNotFoundError:
            pass


    def change(self):
        if self.alive(5)==0:
            row =  self.tableWidget.currentRow()
            column = self.tableWidget.currentColumn() 
            value ,ok = QInputDialog.getText(self,"Вввод нового значения","Введите новое значение",QLineEdit.Normal,'')
            if value and ok:
                data=list()
                documents=list()
                copi_table=list()
                try:
                    for r in range(0,100):
                        for c in range(0,7):
                            documents.append(self.tableWidget.item(r,c).text())
                        cpop_Table={
                               "Number": documents[0],
                               "name":   documents[1],
                               "fname":  documents[2],
                               "phone":  documents[3],
                               "uid":    documents[4],
                               "nik":    documents[5],
                               "wo":     documents[6]
                                }
                        copi_table.append(cpop_Table)
                        documents=list()
                except AttributeError:
                    pass
                for currentColum in range (7):
                    item=self.tableWidget.item(row,currentColum).text()
                    data.append(item)
                header= ['Number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
                post = {
                           "Number": data[0],
                           "name": data[1],
                           "fname": data[2],
                           "phone": data[3],
                           "uid":data[4],
                           "nik":data[5],
                           "wo":data[6]
                            }
                posts.update_one(post, {"$set":{f'{header[column]}': f'{value}'}})
                post[header[column]]=value
                copi_table[row]=post
                self.tableWidget.clearContents()
                j=0
                for i in copi_table:
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
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите данные.')


    def alive(self,Number):
        if self.thread1.is_alive():
            QMessageBox.warning(self.Back,"Warning!","База данных еще загружается, все функции кроме просмотра и создания - заблокированы",buttons=QMessageBox.Ok)
        else:
            if Number==1:
                self.Stop_But.setDisabled(True)
                return 0
            if Number==2:
                self.Stop_But.setDisabled(True)
                return 0
            if Number==3:
                self.Stop_But.setDisabled(True)
                return 0
            if Number==4:
                self.Stop_But.setDisabled(True)
                return 0
            if Number==5:
                self.Stop_But.setDisabled(True)
                return 0
                

    def StopButton(self):
        self.Stop_But.setDisabled(False)
        self.Stop_But.clicked.connect(self.stopped)


    def stopped(self): 
        global stop_threads
        stop_threads = True
        self.Stop_But.setDisabled(True)
        QMessageBox.warning(self.Back,"Warning!","Запись в базу данных остановлена. Чтение из файла прекращено",buttons=QMessageBox.Ok)


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
        self.Update_Data.setDisabled(False)

          
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
        if self.alive(1)==0:
            self.point+=1
            self.setTable()


    def point_minus(self):
        if self.alive(2)==0:
            if self.point<1:
                QMessageBox.warning(self.Back,"Warning!","We cant go back",buttons=QMessageBox.Ok)
            else:
                self.point-=1
                self.back=True
                self.setTable()


    def search(self): #dont work need rework
        result = find_document(series_collection, {'name': 'FRIENDS'})
        print(result)
        delete_document(series_collection, {'_id': id_})


    def aboutBox(self):
        QMessageBox.about(self.aboutButton,"about menu","https://www.youtube.com/watch?v=dQw4w9WgXcQ")


    def Enter_nick(self):
        if self.alive(3)==0:
            if self.choose==0:
                text, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Search for nik:')
            elif self.choose==1:
                text, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Search for phone:')
            elif self.choose==2:
                text, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Search for fname:')
            if ok:
                if self.choose==0:
                    self.result=posts.find({"nik":str(text)})
                elif self.choose==1:
                    self.result=posts.find({"phone":str(text)})
                elif self.choose==2:
                    self.result=posts.find({"fname":str(text)})
                msgBox=QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Сохранить результат в файл?")
                msgBox.setWindowTitle("?")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                returnvalue=msgBox.exec()
                if returnvalue == QtWidgets.QMessageBox.Ok:
                    text, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Enter name file')
                    self.save_file(text)
                else:
                    msgBox=QtWidgets.QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Вывести результат в таблицу?")
                    msgBox.setWindowTitle("?")
                    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                    returnvalue=msgBox.exec()
                    if returnvalue == QtWidgets.QMessageBox.Ok:
                        j=0
                        self.Next.setDisabled(True)
                        self.Back.setDisabled(True)
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


    def save_file(self,text):
        with open(text,"w",encoding="UTF-8") as file:
            result=self.result
            for i in result:
                string=""
                string=string+str(i['Number'])+"|"+str(i['name'])+"|"+str(i['fname'])+"|"+str(i['phone'])+"|"+str(i['uid'])+"|"+str(i['nik'])+"|"+str(i['wo']+"\n")
                file.write(string)
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Вывести результат в таблицу?")
        msgBox.setWindowTitle("?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnvalue=msgBox.exec()
        if returnvalue == QtWidgets.QMessageBox.Ok:
            j=0
            self.Next.setDisabled(True)
            self.Back.setDisabled(True)
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



    def setFontBox(self):
        cbox  = QComboBox(self)
        tables=("Поиск по нику","Поиск по телефону","Поиск по фамилии")
        cbox.addItems(tables)
        cbox.move(25,676)
        cbox.currentIndexChanged.connect(self.printfel)





def parsing(path,File_Size):
    j=1
    j_row=''
    size=int(File_Size/185)
    precent=int(size/100)
    a = timeit.default_timer()
    with open(path, "r", newline="") as file:
        list_of_posts=list()
        reader = csv.reader(file)
        first_row=file.readline()
        for row in reader:
            row=row[0].split("|")
            post = {
                   "Number": row[1],
                   "name": row[2],
                   "fname": row[3],
                   "phone": row[4],
                   "uid":row[5],
                   "nik":row[6],
                   "wo":row[7]
                    }
            list_of_posts.append(post)
            global stop_threads
            if stop_threads:
                post_id=posts.insert_many(list_of_posts)
                break
            if len(list_of_posts)==100000:
                post_id=posts.insert_many(list_of_posts)
                list_of_posts.clear()
        if len(list_of_posts)!=0:
            post_id=posts.insert_many(list_of_posts)

    print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")


myApp=QApplication(sys.argv)
window=Window()
window.show()
myApp.exec_()

sys.exit(0)

       

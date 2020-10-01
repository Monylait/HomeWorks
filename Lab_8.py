import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget,QDialog,QVBoxLayout,QComboBox,QFileDialog, QTableWidget,QTableWidgetItem
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets
import PySide2.QtCore as QtCore 
from PySide2.QtCore import QFileInfo


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
        self.setGeometry(0,0,1080,720)
        self.setMinimumHeight(720)
        self.setMinimumWidth(1080)
        self.setMaximumHeight(720)
        self.setMaximumWidth(1080)
 
     
    def setIcon(self):
        appIcon= QIcon("3.jpg")
        self.setWindowIcon(appIcon)


    def setButtons(self):
        Browse_Button=QPushButton("Browse",self)
        Browse_Button.move(49,640)
        Browse_Button.clicked.connect(self.File_path)


    def File_path(self):
        self.dialog = QFileDialog(self)
        self.path=self.dialog.getOpenFileName()
        self.path=self.path[0]
        self.fi=QFileInfo(self.path)
        print(self.fi)
        print(self.path)
        self.FileSize=self.fi.size() # in bytes
    
        
    def New_Window_Message(self):
        userinfo = QMessageBox.question(self,"COnfirme", "Do u?",QMessageBox.Yes,QMessageBox.No)
        if userinfo==QMessageBox.Yes:
            print("Yes")
        if userinfo==QMessageBox.No:
            print("No")

    
    def Help_Button(self):
        self.aboutButton=QPushButton("Open About",self)
        self.aboutButton.move(960,670)
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
        self.Search_button.move(180,669)
        self.Search_button.clicked.connect(self.aboutBox)


    def Table(self):
        self.tableWidget =QTableWidget(self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(100)  
        self.tableWidget.move(100,7)
        self.tableWidget.setMinimumHeight(600)
        self.tableWidget.setMinimumWidth(750)
        self.tableWidget.setMaximumHeight(600)
        self.tableWidget.setMaximumWidth(750)
        self.tableWidget.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3","Header 4", "Header 5", "Header 6","Header 7"])
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Text in column 3"))


    def aboutBox(self):
        QMessageBox.about(self.aboutButton,"about menu","About text more text")


    def setFontBox(self):
        cbox  = QComboBox(self)
        tables=("Поиск по нику","Поиск по телефону","Поиск по члену")
        cbox.addItems(tables)
        cbox.move(50,670)
        cbox.currentIndexChanged.connect(self. printfel)




myApp=QApplication(sys.argv)
window=Window()
window.show()

myApp.exec_()

sys.exit(0)
import pymongo
from pymongo import MongoClient
import csv
import os 
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget,QDialog,QVBoxLayout,QComboBox,QFileDialog, QTableWidget,QTableWidgetItem,QLineEdit,QInputDialog,QProgressBar
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets
import PySide2.QtCore as QtCore 
from PySide2.QtCore import QFileInfo
import requests
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import shodan
import timeit
import json


client=MongoClient('localhost',27017)
db=client['test-database']
posts=db.posters
db.posts.create_index("kk")


class Window(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab_11")
        self.setSize()
        self.setIcon()
        self.Table()
        self.setButtons()
        self.config()
        self.CheckApi()
        self.J=0


    def setSize(self):
       self.setGeometry(0,0,1200,720)
       self.setMinimumHeight(345)
       self.setMinimumWidth(1274)
       self.setMaximumHeight(345)
       self.setMaximumWidth(1274)
    

    def center(self):
        qRect=self.frameGeometry()
        centerPoint=QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


    def setIcon(self):
        appIcon= QIcon("log.ico")
        self.setWindowIcon(appIcon)


    def config(self):
        code = 'booooooobs'

        with open("private_rsa_key.bin",'r',encoding='utf-8') as priv_key:
            file=priv_key.read()
        with open("config.txt", 'rb') as fobj:
            private_key = RSA.import_key(
                file,
                 passphrase=code
             )
            
            enc_session_key, nonce, tag, ciphertext = [
                fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
            ]
          
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)

            cipher_aes: EaxMode = AES.new(session_key, AES.MODE_EAX,nonce)# type: ignore
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            self.API=data.decode('utf-8')


    def privat_key(self):
        with open("rsa-private.txt",'r',encoding='utf-8') as priv_key:
            file=priv_key.read()
        return file


    def CheckApi(self):
        j="https://api.shodan.io/api-info?key="+self.API
        response=requests.get(j)
        response=response.json()
        query_credits=''
        plan=''
        scan_credits=''
        for i in response:
            if i=="query_credits":
                query_credits=response[i]
            if i=="plan":
                plan=response[i]
            if i=="scan_credits":
                scan_credits=response[i]
        self.tableWidgetSmall =QTableWidget(self)
        self.tableWidgetSmall.setColumnCount(1)
        self.tableWidgetSmall.setRowCount(3)  
        self.tableWidgetSmall.move(1074,217)
        self.tableWidgetSmall.setMinimumHeight(115)
        self.tableWidgetSmall.setMinimumWidth(180)
        self.tableWidgetSmall.setMaximumHeight(115)
        self.tableWidgetSmall.setMaximumWidth(180)
        self.tableWidgetSmall.setVerticalHeaderLabels(["Plan", "query_credits", "scan_credits"])
        self.tableWidgetSmall.setItem(0, 0, QTableWidgetItem(plan))
        self.tableWidgetSmall.setItem(0, 1, QTableWidgetItem(str(query_credits)))
        self.tableWidgetSmall.setItem(0, 2, QTableWidgetItem(str(scan_credits)))


    def Table(self):
        self.tableWidget =QTableWidget(self)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)  
        self.tableWidget.move(25,7)
        self.tableWidget.setMinimumHeight(325)
        self.tableWidget.setMinimumWidth(1024)
        self.tableWidget.setMaximumHeight(325)
        self.tableWidget.setMaximumWidth(1024)
        self.tableWidget.setHorizontalHeaderLabels(["Time scan", "IP адрес", "Country_name","Hostnames","Product","Os","Timestamp","Banner","Port","Org"])


    def setButtons(self):
        Create_Token=QPushButton("Create_Token",self)
        Create_Token.move(1073,7)
        Create_Token.clicked.connect(self.Create_Tok)
        Search=QPushButton("Search",self)
        Search.move(1073,187)
        Search.clicked.connect(self.Search_API)
        Load=QPushButton("Load from file",self)
        Load.move(1180,187)
        Load.clicked.connect(self.Load_File)


    def Create_Tok(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Введите ваш API')
        if ok:
            text=text.encode('utf-8')
            code = 'booooooobs'
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(
                passphrase=code, 
                pkcs=8, 
                protection="scryptAndAES128-CBC"
            )
            with open('private_rsa_key.bin', 'wb') as file_key:
                file_key.write(encrypted_key)
            publick=key.publickey().exportKey() 
            with open("config.txt", 'wb') as out_file:
                recipient_key = RSA.import_key(
                    publick
                )
       
                session_key = get_random_bytes(16)
       
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                out_file.write(cipher_rsa.encrypt(session_key))
       
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                ciphertext, tag = cipher_aes.encrypt_and_digest(text)
       
                out_file.write(cipher_aes.nonce)
                out_file.write(tag)
                out_file.write(ciphertext)


    def Search_API(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Введите IP')
        if ok:
            a = timeit.default_timer()
            j="https://api.shodan.io/shodan/host/"+str(text)+"?key="+self.API
            response=requests.get(j)
            time= timeit.default_timer()-a
            response=response.json()
            ip='None'
            country_name='None'
            hostnames='None'
            data='None'
            product='None'
            oS='None'
            timestamp='None'
            banner='None'
            org='None'
            port='None'
            flag=True
            for key in response:
                if key=="error":
                    response=response[key]
                    j="error_msg "+response
                    QMessageBox.about(self, 'Ошибка', str(j))
                    flag=False
                    break
                if key=="ip":
                    ip=response[key]
                if key=="country_name":
                    country_name=response[key]
                if key=="hostnames":
                    hostnames=response[key]
                    if hostnames=='':
                        hostnames="None"
                if key=="data":
                    data=response[key]
                    data=data[0]
                for key in data:
                    if key=="product":
                        product=data[key]
                    if key=="os":
                        oS=data[key]
                    if key=="timestamp":
                        timestamp=data[key]
                    if key=="banner":
                        banner=data[key]
                    if key=="org":
                        org=data[key]
                    if key=="port":
                        port=data[key]
            while flag:
                j=self.J%10
                self.tableWidget.setHorizontalHeaderLabels(["Time scan", "IP адрес", "Country_name","Hostnames","Product","Os","Timestamp","Banner","Port","Org"])
                self.tableWidget.setItem(j, 0, QTableWidgetItem(str(time)))
                self.tableWidget.setItem(j, 1, QTableWidgetItem(str(ip)))
                self.tableWidget.setItem(j, 2, QTableWidgetItem(str(country_name)))
                self.tableWidget.setItem(j, 3, QTableWidgetItem(str(hostnames)))
                self.tableWidget.setItem(j, 4, QTableWidgetItem(str(product)))
                self.tableWidget.setItem(j, 5, QTableWidgetItem(str(oS)))
                self.tableWidget.setItem(j, 6, QTableWidgetItem(str(timestamp)))
                self.tableWidget.setItem(j, 7, QTableWidgetItem(str(banner)))
                self.tableWidget.setItem(j, 8, QTableWidgetItem(str(port)))
                self.tableWidget.setItem(j, 9, QTableWidgetItem(str(org)))
                self.J+=1
                if self.J>10:
                    with open("Log.csv","r",encoding="utf-8") as log:
                        list_log=log.read().split("\n")
                    with open("Log.csv","w",encoding="utf-8") as log:
                        string=str(time)+"|"+str(ip)+"|"+str(country_name)+"|"+str(hostnames)+"|"+str(product)+"|"+str(oS)+"|"+str(timestamp)+"|"+str(banner)+"|"+str(org)+"|"+str(port)
                        list_log[j]=string
                        for i in list_log:
                            log.write(i+"\n")
                else:
                    try:
                        with open("Log.csv","a",encoding="utf-8") as log:
                            string=str(time)+"|"+str(ip)+"|"+str(country_name)+"|"+str(hostnames)+"|"+str(product)+"|"+str(oS)+"|"+str(timestamp)+"|"+str(banner)+"|"+str(org)+"|"+str(port)+"\n"
                            log.write(string)
                    except FileNotFoundError:
                        with open("Log.csv","w",encoding="utf-8") as log:
                            string=str(time)+"|"+str(ip)+"|"+str(country_name)+"|"+str(hostnames)+"|"+str(product)+"|"+str(oS)+"|"+str(timestamp)+"|"+str(banner)+"|"+str(org)+"|"+str(port)+"\n"
                            log.write(string)
                self.CheckApi()
                flag=False
                break
    

    def Load_File(self):
        fileName = QFileDialog.getOpenFileName(self)
        print(fileName[0])
        with open(fileName[0],"r",encoding="utf-8") as log:
            list_log=log.read().split("\n")
        j=0
        for i in list_log:
            i=i.split("|")
            self.tableWidget.setItem(j, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(j, 1, QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(j, 2, QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(j, 3, QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(j, 4, QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(j, 5, QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(j, 6, QTableWidgetItem(str(i[6])))
            self.tableWidget.setItem(j, 7, QTableWidgetItem(str(i[7])))
            self.tableWidget.setItem(j, 8, QTableWidgetItem(str(i[8])))
            self.tableWidget.setItem(j, 9, QTableWidgetItem(str(i[9])))
            j+=1


myApp=QApplication(sys.argv)
window=Window()
window.show()
myApp.exec_()

sys.exit(0)
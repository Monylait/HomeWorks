import requests
import datetime
import webbrowser
import json
import httplib2
import os
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget,QFileDialog,QInputDialog
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import QObject, Slot, Signal, QThread
import multiprocessing
from threading import Thread


FONT = "FreeSansBold.ttf"
h = httplib2.Http('.cache')


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PL_v.0.1")
        self.setSize() 
        self.setIcon() 
        self.center() 
        self.ID_app=0
        self.AT=0
        self.path_file=0
        self.Load_Liist=10
        self.setButtons()
        self.start_conf()
        self.thread = QtCore.QThread()
           


    def start_conf(self):
        try:
            with open("config.txt","r",encoding="utf-8") as file:
                line=file.readline()
                self.ID_app=line.split()[1]
                line=file.readline()
                self.AT=line.split()[1]
                line=file.readline()
                self.path_file=line.split()[1]
            if self.ID_app==0 or self.AT==0 or self.path_file==0:
                msgBox=QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Фаил настроек не полный, для успешной работы необходимо пересоздать данный файл")
                msgBox.setWindowTitle("?")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                returnvalue=msgBox.exec()
                if returnvalue == QtWidgets.QMessageBox.Ok:
                    self.Create_Tok()
                else:
                    myApp.exec_()
                    sys.exit(0)
        except FileNotFoundError:
            msgBox=QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Файл настроек поврежден/не обнаружен, для работы необходимо пересоздать/создать данный файл")
            msgBox.setWindowTitle("?")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            returnvalue=msgBox.exec()
            if returnvalue == QtWidgets.QMessageBox.Ok:
                self.Create_Tok()
            else:
                myApp.exec_()
                sys.exit(0)
        except IndexError:
            msgBox=QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Файл настроек поврежден/не обнаружен, для работы необходимо пересоздать/создать данный файл")
            msgBox.setWindowTitle("?")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            returnvalue=msgBox.exec()
            if returnvalue == QtWidgets.QMessageBox.Ok:
                self.Create_Tok()
            else:
                myApp.exec_()
                sys.exit(0)


    def setSize(self):
        self.setGeometry(0,0,250,100)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(100)
        self.setMaximumWidth(250)


    def setIcon(self):
        appIcon= QIcon("3.jpg")
        self.setWindowIcon(appIcon)
 

    def center(self):
        qRect=self.frameGeometry()
        centerPoint=QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


    def setButtons(self):
        Create_Token=QPushButton("#Reconfig#",self)
        Browse_Button=QPushButton("#Browse#",self)
        self.aboutButton=QPushButton("Open About",self)
        Download=QPushButton("Download",self)
        Download_Chat=QPushButton("Work with chats",self)
        Download_Chat.move(124,35)
        Download.move(30,35)
        Create_Token.move(30,7)
        Browse_Button.move(124,7)
        self.aboutButton.move(72,63) 
        Create_Token.clicked.connect(self.Create_Tok)
        Browse_Button.clicked.connect(self.File_path)
        self.aboutButton.clicked.connect(self.aboutBox)
        Download.clicked.connect(self.Download)
        Download_Chat.clicked.connect(self.Work_With_Chat)


    def Create_Tok(self): #получение токена кривое
        self.text, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Введите id приложения')
        if ok:
            webbrowser.open('https://oauth.vk.com/authorize?client_id='+str(self.text)+'&display=page&scope=photos,friends,messages&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.124&revoke=1', new=2)
            self.AT, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Введите access_token')
            if ok:
                QMessageBox.about(self, 'Уведомление', "Сейчас вам предложат указать папку для всех последующих сохранений альбомов")
                self.dialog = QFileDialog(self)
                self.path=self.dialog.getExistingDirectory()
                with open("config.txt","w",encoding="utf-8") as file:
                        file.write("ID_app"+" "+str(self.text)+"\n"+"AT"+" "+str(self.AT)+"\n"+"Path "+str(self.path))
                QMessageBox.about(self, 'Успешно', 'Файл успешно изменен/создан')
            else:
                QMessageBox.about(self, 'Ошибка', 'Файл не будет изменен/создан')
        else:
            QMessageBox.about(self, 'Ошибка', 'Файл не будет изменен/создан')


    def File_path(self):
        self.dialog = QFileDialog(self)
        self.path=self.dialog.getExistingDirectory()
        with open("config.txt","a",encoding="utf-8") as file:
            file.write("Path "+str(self.path))
        QMessageBox.about(self, 'Успешно', 'Папка для сохранения альбомов изменена')


    def Download (self):
        text=0
        link, ok = QInputDialog.getText(self, 'Input Dialog', 'Введите полную ссылку на альбом')
        try:
            self.thread.quit()
            self.thread.quit()
        except Exception:
            pass
        if ok and link!=0 and not self.thread.isRunning():
            offset=0;
            document=dict()
            list_of_posts=list()
    
            link=link.split("album")
            link_id=link[1].split("_")
            album_id=link_id[1].split("?")
            album_id=album_id[0]
            link_id=link_id[0]
            if album_id=='00':
                album_id='wall'
                string='wall'
            if album_id=='000':
                album_id='saved'
                string='saved'
            count=0
            offset=0
            j="https://api.vk.com/method/photos.get?owner_id="+str(link_id)+"&album_id="+str(album_id)+"&offset="+str(offset)+"&count=1000&access_token="+str(self.AT)+"&v=5.124"
            response=requests.get(j) 
            response=response.json()
            for key in response:
                if key=='error':
                    response=response[key]
                    j="error_msg "+str(response["error_msg"])
                    QMessageBox.about(self, 'Ошибка', str(j))
                if key=='response':
                    response=response[key]
                    for key in response:
                        if key=='count':
                            count=response[key]
            while offset<=count:
                response=requests.get("https://api.vk.com/method/photos.get?owner_id="+str(link_id)+"&album_id="+str(album_id)+"&offset="+str(offset)+"&count=1000&access_token="+str(self.AT)+"&v=5.124") 
                response=response.json()
                for key in response:
                    if key=='error':
                        response=response[key]
                        j="error_msg "+str(response["error_msg"])
                        QMessageBox.about(self, 'Ошибка', str(j))
                    if key=='response':
                        response=response[key]
                        for key in response:
                            if key=='items':
                                items=response[key]
                for i in items:
                    for key in i:
                        if key=="sizes":
                            size=i[key]
                            check=0
                            for i in size:
                                if check==0:
                                    document["height"]=i["height"]
                                    document["url"]=i["url"]
                                    document["width"]=i["width"]
                                    check+=1
                                else:
                                    if i["height"]>document["height"]:
                                        document["height"]=i["height"]
                                        document["url"]=i["url"]
                                        document["width"]=i["width"]
                            list_of_posts.append(document["url"])
                    offset+=1
                    if offset>=count:
                        break
                if offset>=count:
                    break
            response=requests.get("https://api.vk.com/method/photos.getAlbums?owner_id="+str(link_id)+"&album_ids="+str(album_id)+"&access_token="+self.AT+"&v=5.124")
            response=response.json()
            for key in response:
                if key=='error':
                    response=response[key]
                    j="error_msg "+str(response["error_msg"])
                    QMessageBox.about(self, 'Ошибка', str(j))
                if key=='response':
                    response=response[key]
                    for key in response:
                        if key=='items':
                            items=response[key]
                            for key in items:
                                for i in key:
                                    if i=="title":
                                        string=key[i]
            self.title=str()
            for i in string:
                if i=="/" or i=="\\" or i==":" or i=="*" or i=="?" or i=='"' or i==">" or i=="<" or i=="|" or i==" ":
                    self.title=self.title+"_"   
                else:
                    self.title=self.title+i
            try:
                os.mkdir(str(self.path_file)+"/"+str(self.title))
            except OSError:
                pass
            except Exception:
                pass
            msgBox=QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Обнаруженно "+str(count)+" элементов альбома. Их необходимо скачать  (Ok) или сохранить ссылки на каждый эллемент альбома (Cancel)?")
            msgBox.setWindowTitle("?")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            returnvalue=msgBox.exec()
            if returnvalue==QtWidgets.QMessageBox.Ok:
                files=[self.path_file,self.title,list_of_posts]
                self.worker = Worker(files)
                self.worker.moveToThread(self.thread)
                self.worker.finished.connect(self.thread.quit)
                self.thread.started.connect(self.worker.parsing)
                self.thread.finished.connect(self.worker.deleteLater)
                self.showProgress(
                    'Loading file(s)...', count, self.worker.stop)
                self.worker.loaded.connect(self.updateProgress)
                self.thread.start()
            else:
                j=1
                string=''
                for i in list_of_posts:
                    string=string+str(i)+"\n"
                    j+=1
                dir=self.path_file+"/"+str(self.title)+"/"+str(self.title)+" links"+".txt"
                with open(dir,'w',encoding='UTF-8') as file:
                    file.write(string)
                QMessageBox.about(self, 'Успешно', 'Ссылки записаны')  


    def Work_With_Chat(self):
        self.text, ok = QInputDialog.getText(self, 'Input Dialog',
                    'Введите id адресата. Если групповая беседа *2000000000 + id беседы*.\nДля пользователя *id пользователя*.\nДля сообщества *-id сообщества*. ')
        if ok:
            try:
                self.thread.quit()
                self.thread.quit()
            except Exception:
                pass
            if ok and self.text!=0 and not self.thread.isRunning():
                offset=0;
                document=dict()
                list_of_posts=list()
                count=0
                offset=0
                j="https://api.vk.com/method/messages.getHistoryAttachments?peer_id="+str(self.text)+"&media_type=photo&start_from=0&count=200&max_forwards_level=45&access_token="+str(self.AT)+"&v=5.124"
                response=requests.get(j) 
                response=response.json()
                for key in response:
                    if key=='error':
                        response=response[key]
                        j="error_msg "+str(response["error_msg"])
                        QMessageBox.about(self, 'Ошибка', str(j))
                    if key=='response':
                        response=response[key]
                        for key in response:
                            if key=='items':
                                items=response[key]
                if len(items)!=0:
                    for i in items:
                        for key in i:
                            if key=="attachment":
                                attachment=i[key]
                                for i in attachment:
                                    if i=="photo":
                                        photo=attachment[i]
                                        for element in photo:
                                            if element=="sizes":
                                                size=photo[element]
                                                check=0
                                                for i in size:
                                                    if check==0:
                                                        document["height"]=i["height"]
                                                        document["url"]=i["url"]
                                                        document["width"]=i["width"]
                                                        check+=1
                                                    else:
                                                        if i["height"]>document["height"]:
                                                            document["height"]=i["height"]
                                                            document["url"]=i["url"]
                                                            document["width"]=i["width"]
                                list_of_posts.append(document["url"])
                    self.title=self.text
                    try:
                        os.mkdir(str(self.path_file)+"/"+str(self.title))
                    except OSError:
                        pass
                    except Exception:
                        pass
                    msgBox=QtWidgets.QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Обнаруженно "+str(count)+" элементов. Их необходимо скачать (Ok) или сохранить ссылки на каждый эллемент (Cancel)?")
                    msgBox.setWindowTitle("?")
                    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                    returnvalue=msgBox.exec()
                    if returnvalue==QtWidgets.QMessageBox.Ok:
                        files=[self.path_file,self.title,list_of_posts]
                        self.worker = Worker(files)
                        self.worker.moveToThread(self.thread)
                        self.worker.finished.connect(self.thread.quit)
                        self.thread.started.connect(self.worker.parsing)
                        self.thread.finished.connect(self.worker.deleteLater)
                        self.showProgress(
                            'Loading file(s)...', count, self.worker.stop)
                        self.worker.loaded.connect(self.updateProgress)
                        self.thread.start()
                    else:
                        j=1
                        string=''
                        for i in list_of_posts:
                            string=string+str(i)+"\n"
                            j+=1
                        dir=self.path_file+"/"+str(self.title)+"/"+str(self.title)+" links"+".txt"
                        with open(dir,'w',encoding='UTF-8') as file:
                            file.write(string)
                        QMessageBox.about(self, 'Успешно', 'Ссылки записаны')
                else:
                    QMessageBox.about(self, 'Ошибка', 'Cервер вернул NONE')
        else:
            QMessageBox.about(self, 'Ошибка', 'id не указан\указан неверно')


    def updateProgress(self, count, name_file):
        if not self.progress.wasCanceled():
            self.progress.setLabelText(
                'Loaded: %s' % name_file)
            self.progress.setValue(count)

        else:
            QtWidgets.QMessageBox.warning(
                self, 'Load Files', 'Loading Aborted!')


    def showProgress(self, text, length, handler):
        self.progress = QtWidgets.QProgressDialog(
            text, "Abort", 0, length, self)
        self.length=length
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.canceled.connect(
            handler, type=QtCore.Qt.DirectConnection)
        self.progress.forceShow()


    def aboutBox(self):
        QMessageBox.about(self.aboutButton,"about menu","Reconfig - пересоздает файл настроек\nБольше информации по этому пункту в файле Read_me\n\nBrowse - позволяет сменить путь для сохранения альбомов\n\nDownload - кнопка активации скачивания альбомов\индексирования альбомов\n")
     

class Worker(QtCore.QObject):
    
    loaded=QtCore.Signal(int,str)
    finished=QtCore.Signal()


    def __init__(self,files):
        super().__init__()
        self._path_file = files[0]
        self._title = files[1]
        self._list_of_posts=files[2]


    def parsing(self):
        self._stop=False
        j=1
        for i in self._list_of_posts:
            try:
                response, content = h.request(i)
                out = open(str(self._path_file)+"/"+str(self._title)+'/Image'+'_'+str(j)+'.jpg', 'wb')
                out.write(content)
                out.close()
                self.loaded.emit(j, i)              
                if self._stop:
                    break
                j+=1
            except Exception:
                pass
        self._stop = True    
        self.finished.emit()


    def stop(self):
            self._stop = True
        


if __name__ == '__main__':
        
        response=requests.get("https://api.vk.com/method/users.get?owner_id=261645081&access_token=2caba8df74621bcdd4d8b5092a1e3f84f5d7cb6d9518dc0384f6406c788e9fb1865f6404abc0775ed43fa&v=5.124")
        response=response.json()
        myApp=QApplication(sys.argv)
        window=Window()
        window.show()
        myApp.exec_()
        print("Lol")
        i=input()
        sys.exit(0)



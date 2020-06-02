import os
import shutil
import Security
import client_socket as cl_s

def write_new_acc(loggin:str,new_password:str,way:str):
        try:
            Security.decode_sys_files(way)
        except FileNotFoundError:
            pass
        with open(way,'a',encoding='utf-8') as config_acc:
            string=''
            password_new=Security.hash_password(new_password)
            string=string+str(loggin)+' '+str(password_new)+'\n'
            config_acc.write(string)
        Security.security_sys_files(way)
    

def CreateAcc(way_for_sys_file:str):
    loggin_list=list()
    way=os.path.join(way_for_sys_file,"config_acc.conf")#way_for_sys_file+"\config_acc.conf"
    cl_s.private()
    try:
        Security.decode_sys_files(way)
        with open(way,'r',encoding='utf-8') as config_acc:
            for line in config_acc:
                line.replace("\n","")
                line_list=line.split()
                loggin_list.append(line_list[0])
    except FileNotFoundError:
        print("Записи о каких-либо аккаунтах не найдены, поздравляю "
              "- вы первый пользователь!\n"
              )
    flag=True
    i=0
    while flag:
        try:
            loggin=input("Pleas, write your loggin this >> ")
            if len(loggin)<1:
                print("Incorrect loggin (so small), pleas, create new loggin")
            elif len(loggin)>100:
                print("Incorrect loggin (so big), pleas, create new loggin")
            elif loggin_list.count(loggin)>0:
                print("Loggin was takken, pleas enter another loggin")
            elif len(loggin)>1 or len(loggin)==1 and loggin_list.count(loggin)<1:
                print("Loggin succesfull, next step")
                flag=False
        except BaseException:
            print("Problems with loggin")
            i+=1
            if i==3:
                flag=False
                Security.security_sys_files(way)
                break
    try:
        Security.security_sys_files(way)
    except FileNotFoundError:
        pass
    flag=True
    while flag:
        try:
            new_password=input("Pleas, write you new password >> ")
            if len(new_password)<=1:
                print("Password so easy, pleas, create new password")
            elif len(new_password)>30:
                print("Password so big, pleas, create new password")
            elif len(new_password)>1:
                write_new_acc(loggin,new_password,way)#.encode('utf-8')
                print("Account was succesfull create")
                try:
                    if not os.path.isdir(os.path.join(way_for_sys_file,loggin)): #way_for_sys_file+"\\"+loggin
                        os.mkdir(os.path.join(way_for_sys_file,loggin))
                except OSError:
                    print ("Создать директорию %s не удалось" %way_for_sys_file )
                try:
                    if not os.path.isdir(os.path.join(way_for_sys_file,loggin,"Notes")): #way_for_sys_file+"\\"+loggin+"\\"+"Notes"
                        os.mkdir(os.path.join(way_for_sys_file,loggin,"Notes"))
                except OSError:
                    print ("Создать директорию %s не удалось" %way_for_sys_file )
                try:
                    if not os.path.isdir(os.path.join(way_for_sys_file,loggin,"Keys")): #way_for_sys_file+"\\"+loggin+"\\"+"Keys"
                        os.mkdir(os.path.join(way_for_sys_file,loggin,"Keys"))
                except OSError:
                    print ("Создать директорию %s не удалось" %way_for_sys_file )
                Security.generate_keys(loggin,os.path.join(way_for_sys_file,loggin,"Keys")) #way_for_sys_file+"\\"+loggin+"\\"+"Keys"
                flag=False
        except ValueError:
            Security.security_sys_files(way)
            print("Problems with password")
            i+=1
            if i==3:
                flag=False
                break
           

def delete_acc(way_for_sys_file:str,loggin:str):
    way=os.path.join(way_for_sys_file,"config_acc.conf")#way_for_sys_file+"\config_acc.conf"
    Loggin_dict=dict()
    flag=True
    while flag:
        try:
            Security.decode_sys_files(way)
            with open(way,"r",encoding='utf-8') as config_file:
                for line in config_file:
                    time_list=line.split(' ',1)
                    Loggin_dict[time_list[0]]=time_list[1]
            with open(way,"w",encoding='utf-8') as config_file:
                for key in Loggin_dict:
                    string=''
                    if key!=loggin:
                        string=string+key+" "+Loggin_dict[key]
                        config_file.write(string)
            Security.security_sys_files(way)
            way=os.path.join(way_for_sys_file,loggin)#way_for_sys_file+"\\"+loggin
            shutil.rmtree(way)
            print("Account succesfull delete")
            flag=False
        except FileNotFoundError:
            print("File or directory not found, cant delete")
            Security.security_sys_files(way)






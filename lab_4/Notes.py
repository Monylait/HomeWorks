import os
import time
import Security

def acc_info(way:str,loggin:str):
    try:
        files_list=os.listdir(way+"\\"+"Notes")
        print("Loggin - %s\n"% loggin)
        print("Количество заметок - %s\n"% len(files_list))
        print("Ваши заметки:\n")
        for ellement in files_list:
            list=ellement.split(".")
            string=''
            for ellement in list:
                if ellement!='txt':
                    string=string+ellement
            if string=='':
                print("note without name")
            elif string!='':
                print(string)
        print('\n')
    except ValueError:
       print("Cant see acc information")

def create_notes(way:str,loggin:str):
    flag_1=True
    while flag_1:
        flag=True
        while flag:
            try:
                command=str(input("Enter name for new file with file extension(.txt)"))
                command=command.replace(' ','_')
                list=command.split(".")
                list.reverse()
                if list[0]=='txt':
                    for ch in command:
                        if ch=="\\" or ch=="/" or ch==":" or ch=="*" or ch=="?" or ch=="\"" or ch=="|" or ch=="<" or ch==">":
                            print("bad name for file - you use incorrect symbols")
                            break    
                    flag=False
                else:
                    print('Wrong file extension')
            except ValueError:
                print("Wrong input")
        way_new=way+"\\"+"Notes"+"\\"+command
        try:
            with open(way_new,'r',encoding='utf-8') as New_Note:
                print("Note with this name was created later")
        except FileNotFoundError:
            with open(way_new,'a',encoding='utf-8') as New_Note:
                print("Open file...")
            os.system(way_new) 
            Security.security_files(way,way_new)
            flag_1=False
        except OSError:
            print("enter correct way pleas")


def work_with_notes(way:str,loggin:str):
    flag_1=True
    while flag_1:
        try:
            flag=True
            while flag:
                try:
                    command=str(input("Enter name your notes with file extension(.txt) "))
                    command=command.replace(' ','_')
                    list=command.split(".")
                    list.reverse()
                    if list[0]=='txt':
                        for ch in command:
                            if ch=="\\" or ch=="/" or ch==":" or ch=="*" or ch=="?" or ch=="\"" or ch=="|" or ch=="<" or ch==">":
                                print("bad name for file - you use incorrect symbols")
                                break    
                        flag=False
                    else:
                        print('Wrong file extension')
                except ValueError:
                    print("Wrong input")
            way_new=way+"\\"+"Notes"+"\\"+command
            Security.decode_files(way,way_new)
            with open(way_new,'a',encoding='utf-8') as New_Note:
                print("Open file...")
            os.system(way_new)
            Security.security_files(way,way_new)
            flag_1=False
        except OSError:
            print("enter correct way pleas")


def delete_note(way:str,loggin:str):
    i=0
    flag=True
    command=input("Are you really need delete note? If yes, enter name of note for delete ")
    while flag:
        if i!=0:
            command=input("Enter correct name of note, pelase, with file extension(.txt)")
        list=command.split('.')
        list.reverse()
        if list[0]=='txt':
            try:
                os.remove(way+"\\"+"Notes"+'\\'+command)
                print("Note succesfull delete")
                flag=False
            except FileNotFoundError:
                print("Note not found")
                i+=1
            except OSError:
                print("Wrong way\you use incorrect symbols")
                i+=1
        else:
            command=command+'.txt'
            try:
                os.remove(way+'\\'+command)
                print("Note sucesfull delete")
                flag=False
            except FileNotFoundError:
                print("Note not found ")
                i+=1
            except OSError:
                print("Wrong way\you use incorrect symbols ")
                i+=1
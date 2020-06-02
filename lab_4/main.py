import os
import Autorizeid as Auto
import Work_with_Acc as Cr_A
import Notes
import Security

path_old=os.getcwd()
path_new=os.path.join(path_old,'Lab_4_Files') #path_old+"\Lab_4_Files"
try:
    if not os.path.isdir(path_new):
        os.mkdir(path_new)
except OSError:
    print ("Создать директорию %s не удалось" %path_new )


flag=True
loggin=''
while flag:
    try:
        flag_5=True
        while flag_5:
            try:
                command=int(input("Доступные действия:\n\t"
                                  "1) Авторизация\n\t"
                                  "2) Создание аккаунта\n\t"
                                  "3) Выход из программы\n"
                                  ))
                if command==1:
                    print(">> Авторизация <<\n")
                    loggin=Auto.read_sys_file(path_new)
                    if loggin=='':
                        print("Ошибка авторизации,возврат в главное меню\n")
                    elif loggin!='':
                        print("Авторизация успешно выполнена\n")
                        print("Account: %s"% loggin)
                        flag_2=True
                        while flag_2:
                            try:
                                command=int(input("Доступные действия:\n\t"
                                                  "1) Работа с заметками\n\t"
                                                  "2) Удаление аккаунта\n\t"
                                                  "3) Смена пользователя\n"
                                                  ))
                                if command==1:
                                    print(">> Работа с заметками <<\n")
                                    Notes.acc_info(os.path.join(path_new,loggin),loggin)  #path_new+"\\"+loggin,loggin
                                    flag_3=True
                                    while flag_3:
                                        try:
                                            command=int(input("Доступные действия:\n\t"
                                                              "1) Создание новых заметок\n\t"
                                                              "2) Редактирование старых заметок\n\t"
                                                              "3) Удаление заметок\n\t"
                                                              "4)Выход в меню управления аккаунтом\n"
                                                              ))
                                            way=os.path.join(path_new,loggin)#path_new+"\\"+loggin
                                            if command==1:
                                                print(">> Создание новых заметок <<")
                                                Notes.create_notes(way,loggin)
                                            elif command==2:
                                                Notes.work_with_notes(way,loggin)
                                            elif command==3:
                                                Notes.delete_note(way,loggin)
                                            elif command==4:
                                                flag_3=False
                                        except ValueError:
                                            print("Wrong input #5")
                                elif command==2:
                                    print(">> Удаление аккаунта <<")
                                    Cr_A.delete_acc(path_new,loggin)
                                    flag_2=False
                                elif command==3:
                                    print(">> Смена пользователя <<")
                                    loggin=''
                                    print(".>> Выход из аккаунта <<")
                                    flag_2=False
                                else:
                                    print("Wrong input #4")
                            except ValueError:
                                print("Wrong input #3")
                            except FileNotFoundError:
                                print("File not found")
                elif command==2:
                    print(">> Создание аккаунта <<")
                    Cr_A.CreateAcc(path_new)
                elif command==3:
                        flag=False
                        break
                else:
                    print("Wrong input")
            except ValueError:
                print("wrong input")
    except ValueError:
        Security.security_sys_files(os.path.join(path_new,"config_acc.conf")) #path_new+"\\"+"config_acc.conf")
        print("Local error, try please ")
    except ConnectionRefusedError:
        print("Server not working, error")
    except UnicodeDecodeError:
        print("Server not working, error")
    except FileNotFoundError:
        print("File not found")
    except BaseException:
         print("Error")
         Flag=False
         break

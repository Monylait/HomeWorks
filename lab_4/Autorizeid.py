import os
import Security


def read_sys_file(way_for_sys_file:str)->int and str:
    loggin_list=list()
    password_list=list()
    users_dict=dict()
    way=os.path.join(way_for_sys_file,"config_acc.conf") #way_for_sys_file+"\config_acc.conf"
    try:
        Security.decode_sys_files(way)
    except FileNotFoundError:
        print("havent accs yet ")

    with open(way,'r',encoding='utf-8') as acc_file:
       for line in acc_file:
           line.replace("\n","")
           line_list=line.split()
           users_dict[line_list[0]]=line_list[1]
    flag=True
    i=0
    while flag:
        loggin=input("Pleas, write you loggin \n")
        if loggin in users_dict:
            hashed_password=users_dict[loggin]
            flag=False
        else:
            print("User with this loggin not found \n")
            i+=1
            if i==3:
                print("You create more errors, back in main menu")
                Security.security_sys_files(way)
                flag=False
                return ''
    i=0    
    flag=True
    while flag:
        password=input("Enter password, please \n")
        if Security.check_password(hashed_password, password):
            flag=False
            Security.security_sys_files(way)
            return loggin # autorizeid
        else:
            print('Извините, но пароли не совпадают')
            i+=1
            if i==3:
                print("You create more errors, back in main menu")
                Security.security_sys_files(way)
                flag=False
                return '' #Not autorizaid
 
import os
import time
import datetime

def login_search(work_list_files:list,login:str) -> dict:
    result=dict()
    for file in work_list_files:
        time_result=list()
        print("Start work with file "+file+"\n")
        with open(file,"r") as txt:
            t=time.time()                       
            t=int(t)
            for i in txt:               
                string=i.split("\n")[0].split(",")                             
                if len(string)==24 and login==string[3]:   
                    time_result.append(i)                           
                if int(time.time())-t>3:                     
                    print("Программа на позиции "+str(string[0])+"\n")
                    print("Результатов обнаружено "+str(len(time_result))+"\n")
                    t=time.time()                               
                    t=int(t)
        print(len(time_result))
        result[file]=time_result
    return result


def date_search(work_list_files:list)-> dict:
    time_start=input("Введите временной диапазон в формате ДД ММ ГГ ЧЧ ММ СС  который будет точкой отсчета\n>> ")
    time_end=input("Введите временной диапазон в формате ДД ММ ГГ ЧЧ ММ СС до которого искать\n>> ")
    time_start=time_start.split()
    time_end=time_end.split()
    day_1=int(time_start[0])
    month_1=int(time_start[1])
    year_1=int(time_start[2])
    hour_1=int(time_start[3])
    min_1=int(time_start[4])
    sec_1=int(time_start[5])
    day_2_1=int(time_end[0])
    month_2_1=int(time_end[1])
    year_2_1=int(time_end[2])
    hour_2_1=int(time_end[3])
    min_2_1=int(time_end[4])
    sec_2_1=int(time_end[5])
    timer=0
    func_start=0
    Errors=0
    try:
           if int(day_1)<31 and int(day_1)>0 and int(day_2_1)<31 and int(day_2_1)>0:
               timer+=1
           else:
               print('Days - incorrect')
           if int(month_1)<13 and int(month_1)>0 and int(month_2_1)<13 and int(month_2_1)>0:
               timer+=1
           else:
               print('Month - incorrect')
           if int(year_1)<3000 and int(year_1)>1969 and int(year_2_1)<3000 and int(year_2_1)>1969 and int(year_1)>=int(year_2_1):
               timer+=1
           else:
               print('Years - incorrect')
           if int(hour_1)<25 and int(hour_1)>-1 and int(hour_2_1)<25 and int(hour_2_1)>-1:
               timer+=1
           else:
               print('Hours - incorrect')
           if int(min_1)<60 and int(min_1)>-1 and int(min_2_1)<60 and int(min_2_1)>-1:
               timer+=1
           else:
               print('Mins - incorrect')
           if int(sec_1)<60 and int(sec_1)>-1 and int(sec_2_1)<60 and int(sec_2_1)>-1:
               timer+=1
           else:
               print('Secs - incorrect')
           if timer==6:
               start=datetime.datetime(int(year_1),int(month_1),int(day_1), int(hour_1),int(min_1),int(sec_1)).timestamp()
               stop=datetime.datetime(int(year_2_1),int(month_2_1),int(day_2_1), int(hour_2_1),int(min_2_1),int(sec_2_1)).timestamp()
           else: 
               print('Rows - incorrect')
               Errors+=1       
    except FileNotFoundError:#Exception:
        print('Problem with time - incorrect')
        Errors+=1
    if Errors==0:
        if start>stop:
            print('Data wrong - start<stop - incorrect')
            Errors+=1
        if Errors==0:
            result=dict()
            for file in work_list_files:
                time_result=list()
                print("Start work with file "+file+"\n")
                with open(file,"r") as txt:
                    t=time.time()                       
                    t=int(t)
                    for i in txt:               
                        string=i.split("\n")[0].split(",")  
                        try:
                            if len(string)==24 and start<int(string[0]) and stop>int(string[1]):   
                                time_result.append(i)   
                        except Exception:
                            continue
                        if int(time.time())-t>3:                     
                            print("Программа на позиции "+str(string[0])+"\n")
                            print("Результатов обнаружено "+str(len(time_result))+"\n")
                            t=time.time()                               
                            t=int(t)
                print(len(time_result))
                result[file]=time_result
            return result



list_of_files=list()                                       
while True:
    directory=input("Enter file path pl\n>> ")
    try:
        list_of_files=os.listdir(directory)
        break
    except Exception:
        print("Error - path incorrect\n")
work_list_files=list()
print("Обнаруженны следующие файлы с расширением csv:\n")
for i in list_of_files:
    j=""
    try:
        j=i.split(".")[1]
    except IndexError:
        pass
    if j=="csv":
        work_list_files.append(os.path.join(directory,i))
        print(i)

flag=True
j=0
while flag:
    try:
        if j==0:
                choose=int(input("\nCreate choose:\nFind on login - 1\nFind on date - 2\nExit - 3\n>> "))
        if j!=0:
            choose=int(input("\nCreate choose:\nFind on login - 1\nFind on date - 2\nWork with results - 3\nExit - 4\n>> "))
        if choose==1:
            login=input("Please enter login\n>> ")
            result=login_search(work_list_files,login)
            print("end")
            j+=1
        elif choose==2:
            result=date_search(work_list_files)
            print("end")
            j+=1
        elif choose==3 and j==0:
            flag=False
            break
        elif choose==3 and j!=0:
            flag_2=True
            while flag_2:
                ch=input("Show information or save in file?\n>> Show - 1\n>> Save - 2\n>> ")
                if int(ch)==1:
                    for key in result:
                        print("\nIn "+key+"\n")
                        if len(result[key])==0:
                            print("Empty\n")
                        for strin in result[key]:
                            print(strin) 
                    flag_2=False
                    break
                elif int(ch)==2:
                    final_string=""
                    for key in result:
                        if len(result[key])==0:
                            final_string=final_string+"\n\n"+key+"\n"+"Nothing found"+"\n"
                        else:
                            final_string=final_string+"\n\n"+key+"\n"
                        for strin in result[key]:
                            final_string=final_string+"\n"+strin 
                    with open("Save_Results.txt","w") as file:
                        file.write(final_string)
                    flag_2=False
                    break
                else:
                    print("Bad input, try more please\n")
        elif choose==4 and j!=0:
            flag=False
            break
        else:
            pass
    except Exception:
        continue


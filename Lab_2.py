main_dict={}
flag=True
key_value=[]
data=[]
status=' ec!ec!ec!'
try:
    config=open("conf",'r')
    for str in config:
        if str[0]!='#' and str[0]!=';' and str[0]!='\n':           
            data.append(str)
    for index,string in enumerate(data):
         for ellement in string:
            if ellement==' ':
                str=string
                new_str=str.replace("\n","")
                data[index]=new_str
                break
            elif ellement=="\n":
                str=string
                new_str=str.replace("\n","")
                str=new_str+status
                data[index]=str
                break
    for index,string in enumerate(data):
                  key_value=string.split(' ',1)
                  main_dict[key_value[0]] = key_value[1]

    print("This parameters was found in you file >>\n")
    for key in main_dict.keys():
            print(key)
    print("\nHello!")
    while flag:
        print("Please, enter name of parameter after this words << get param ...>>")
        command=input("get param ")  
        try:
            print('Value ',main_dict[command])
        except BaseException as ex:
            print("Parameter not found")
        for i in range(3):
            command = input("continue? (Y/N) ")
            if command=="Y" or command== "y":
                break
            elif command=="N" or command=="n":
                flag=False 
                break
            else : 
                print('wrong input')
            if i==2:
                print('Too much errors')
                flag=False
                break
    config.close
except FileNotFoundError:
        print("File not found")
except PermissionError:
        print("Need more rights, file cant open")
except Exception:
        print("Program cant work. System error")


    

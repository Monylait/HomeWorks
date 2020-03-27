def chose(message):
 for i in range(3):
            command = input(message).lower()
            if command== "y":
                return True
            elif command=="n":
                break
            else : 
                print('wrong input')
            if i==2:
                print('Too much errors')
                break
 return False
    


main_dict={}
flag=True
key_value=[]
data=[]
status=' ec!ec!ec!'
try:
   # way=input("Enter road to file ")
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
    for index, key in enumerate(main_dict.keys()):    
        print(index+1," : ",key)
    print("\nHello!")
    while flag:
        print("Please, enter name of parameter after this words << get param ...>>")
        command=input("get param ")  
        try:
            print('Value ',main_dict[command])
        except BaseException as ex:
            print("Parameter not found ")
        if chose("Need upgrade param? Y/N "):
           main_dict[command]=input("Enter new value ")
        if chose("continue? (Y/N) "):
            pass
        else:
            flag=False
            break
    config.close()
except FileNotFoundError:
        print("File not found")
except PermissionError:
        print("Need more rights, file cant open")
except Exception:
        print("Program cant work. System error")


    

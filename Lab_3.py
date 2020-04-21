from abc import ABC, abstractmethod, abstractclassmethod

class Parent(ABC): #abstract class

    @abstractmethod
    def read_key():
        pass

    @abstractmethod
    def read_txt():
        pass

    @abstractmethod
    def read_alpha(way):
        pass

    @abstractmethod
    def read_encrypt(way):
        pass


class ex1(Parent):
    

    def __init__(self):
        self.key_dict=""
        self.file_txt=""
        self.file_alpha=""
        self.encrypt_file=""

    def create_data(self):
        self.key_dict=self.read_key()
        self.file_txt=self.read_txt()


    def alphabet(self):
         self.alpha_data=self.read_alpha()


    def create_date_encrypt(self):
        self.encrypt_file=self.read_encrypt()
        self.key_dict=self.read_key()

    #вводим путь до файла
    def enter_way(self):
        way=input("Write way to  file pleas ")
        return way

    #читаем ключ
    def read_key(self):
        main_dict=dict()
        print("Need way to key file")
        way=self.enter_way()
        key_value=[]
        data=[]
        key_file=open(way, "r", encoding='utf-8') 
        for str in key_file:
            if str[0]!='#' and str[0]!='\n':           
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
                    str=new_str
                    data[index]=str
                    break
        for index,string in enumerate(data):
                  key_value=string.split(' ',1)
                  main_dict[key_value[0]] = key_value[1]
        return main_dict

    #читаем текст
    def read_txt(self):
        print("Need way to file with text")
        way=self.enter_way()
        file_txt=open(way,"r", encoding='utf-8')
        return file_txt

    #читаем зашифрованный текст
    def read_encrypt(self):
        print("Need way to file with encrypt text")
        way=self.enter_way()
        encrypt_file=open(way,"r", encoding='utf-8')
        return encrypt_file
    
    #читаем алфавит
    def read_alpha(self):
        print("Need way to file with alphabet")
        way=self.enter_way()
        file_alpha=open(way,"r",encoding='utf-8')
        data=[]
        for str in file_alpha:
            if str[0]!='#' and str[0]!='\n':           
                data.append(str)
        for index,string in enumerate(data):
            for ellement in string:
                if ellement=='&':
                    str=string
                    str=str.replace("&","")
                    data[index]=str
                    break
                if ellement==' ':
                    str=string
                    new_str=str.replace("\n","")
                    data[index]=new_str
                    break
                elif ellement=="\n":
                    str=string
                    new_str=str.replace("\n","")
                    str=new_str
                    data[index]=str
                    break
        return data

    #зашифровываем текст
    def write_encrypt(self): #косячок с работой с пробелами, держится на костылях
        self.create_data()
        new_line=''
        flag=True
        with open("my_encrypt.encrypt",'a', encoding='utf-8') as encrypt_file:
            encrypt_file.write("method of encode: 1 - Replacement\n")
        for line in self.file_txt:  
            for ch in line.lower():
                for key,value in self.key_dict.items():
                    if ch==' ':    
                        ch=ch.replace(' ',"")   
                    if ch==key:         
                        ch_new=self.key_dict[key]
                        line=line.replace(ch,ch_new)
                        new_line=new_line+ch_new
                        flag=False
                        break
                if flag:
                   new_line=new_line+ch
                flag=True
            with open("my_encrypt.encrypt",'a', encoding='utf-8') as encrypt_file:
               
               encrypt_file.write(new_line)
            new_line='' 

    #восстановление текста
    def revers(self):  #зависит от работы write_encrypt
        self.create_date_encrypt()
        new_line=''
        flag=True
        for line in self.encrypt_file:  
            for ch in line.lower():
                for key,value in self.key_dict.items():
                    if ch=='':
                        ch=ch.replace(''," ")
                    if ch==value:    
                        ch_new=key
                        if ch_new=='':
                            ch_new=ch_new.replace(''," ")
                        line=line.replace(ch,ch_new)
                        new_line=new_line+ch_new
                        flag=False
                        break
                if flag:
                   new_line=new_line+ch
                flag=True
            with open("text_reverse.txt",'a') as encrypt_file:
                encrypt_file.write(new_line)
            new_line=''

    #генератор ключей
    def key_generator(self):
        self.alphabet()
        import random
        key=[]
        key_len=25
        old_data=self.alpha_data.copy()
        while True:
            index=random.randint(0, len(self.alpha_data)-1)
            new_val=self.alpha_data[index]
            key.append(new_val)
            del self.alpha_data[index]
            if len(self.alpha_data)==0:
                break
        with open("generate_key.key",'a',encoding='utf-8') as gen_key:
            i=0
            while i<len(old_data):
                string=old_data[i]+' '+key[i]+'\n'
                gen_key.write(string)
                i+=1 
        print("Key succesfull create")


obj=ex1()
obj2=ex1()

print(".>> Main menu")
print(".>> \t1) encode/decode")
print(".>> \t2) generate key")
command=int(input("create you choise "))
if command<1 or command>2:
    print("Wrong command #1")
if command==1:
        print(".>> encode/decode")
        print(".>> \t1) encode")
        print(".>> \t2) decode")
        command=int(input("create you choise "))
        if command<1 or command>2:
            print("Wrong command #2")
        if command==1:
                print(".>> Choose method of encode ")
                print(".>> \t1) replacement method")
                print(".>> \t2) Comming soon")
                print(".>> \t3) Comming soon")
                command=int(input("create you choise "))
                if command<1  or command>3:
                        print("Wrong command #3")                        
                if command==1:
                        obj.write_encrypt()
                if command==2 or command==3:
                        print(".>> i say comming soon!")
        elif command==2:
                print(".>> Choose method for decode ")
                print(".>> \t1) replacement method")
                print(".>> \t2) Comming soon")
                print(".>> \t3) Comming soon")
                command=int(input("create you choise "))
                if command<1 or command>3:
                        print("Wrong command #4")
                        
                if command==1:
                        obj.revers()
                if command==2 or command==3:
                        print(".>> i say comming soon!")
        else:
            print("Command not found #5")              
elif command==2:
        print(".>> Choose encode method:")
        print(".>> \t1) Замена")
        print(".>> \t2) Перестановка")
        command=int(input("create you choise "))
        if command<1 or command>2:
            print("Wrong command #6")
        if command==1:
                obj.key_generator()
        elif command==2:
                print("Comming soon")
        else:
            print("Command not found #7")



#print(obj.key_dict)
#print(obj.file_txt)
#for key,value in self.key_dict.items():
 #           print(key," : ",value)
 
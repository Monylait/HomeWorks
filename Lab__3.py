from abc import ABC, abstractmethod, abstractclassmethod
import random

class Parent(ABC):

    def _enter_way(self,str):
        flag=True
        while flag:
            way=input("Write way to  file pleas ")
            try:
                exampl=way.split('.')
                exampl.reverse()
                if exampl[0]==str:
                    return way
                raise Exception("Wrong file extension")
            except Exception:
                print("Wrong input / File not found")

   
    def read_key(self):
        print("Need way to key file")
        key_dict=dict()
        with open(self._enter_way("key"),'r', encoding='utf-8') as key_file:
            line=key_file.readline()
            while line:
                if line[0]!='\n':
                  key_dict[line[0]]=line[2]
                line=key_file.readline()
        return key_dict

    
    def read_txt(self):
        print("Need way to file with text")       
        file_txt=open(self._enter_way("txt"),"r", encoding='utf-8')
        return file_txt

    
    def read_encrypt(self):
        print("Need way to file with encrypt text")      
        encrypt_file=open(self._enter_way("encode"),"r", encoding='utf-8')
        return encrypt_file

     
    def read_alpha(self):   
        print("Need way to file with alphabet")
        alpha_list=[]
        with open(self._enter_way("alph"),"r",encoding='utf-8') as file_alpha:
            line=file_alpha.readline()
            while line:
                if line[0]!='\n':
                    if alpha_list.count(line[0])<1:
                        alpha_list.append(line[0])
                line=file_alpha.readline()
        return alpha_list


class REPLACE(Parent):
    
    def _create_data(self):
        self.key_dict=self.read_key()
        self.file_txt=self.read_txt()


    def _create_date_encrypt(self):
        self.encrypt_file=self.read_encrypt()
        self.key_dict=self.read_key()

  
    def Encrypt(self): 
        self._create_data()
        print("Enter name for file with encrypt text")
        way=self._enter_way("encode")
        new_line=''
        flag=True
        with open(way,'w', encoding='utf-8') as encrypt_file:
            encrypt_file.write("method of encryption: 1 - Replacement!\n")
        for line in self.file_txt:  
            for ch in line:
                for key,value in self.key_dict.items():   
                    if ch==key:         
                        ch_new=self.key_dict[key]
                        new_line=new_line+ch_new
                        flag=False
                        break
                if flag:
                   new_line=new_line+ch
                flag=True
            with open(way,'a', encoding='utf-8') as encrypt_file:
               encrypt_file.write(new_line)
            new_line='' 
        print("Operation succesfull completed")
    
    def revers(self):
        self._create_date_encrypt()
        line=self.encrypt_file.readline()
        new_line=''
        flag=True
        print("Enter name for file with decrypt text")
        with open(self._enter_way("txt"),'w') as decrypt_file:
            for line in self.encrypt_file:  
                for ch in line:
                    for letter_first,letter_second in self.key_dict.items():                            
                        if ch==letter_second:    
                            ch_new=letter_first
                            new_line=new_line+ch_new
                            flag=False
                            break
                    if flag:
                       new_line=new_line+ch
                    flag=True
                decrypt_file.write(new_line)
                new_line=''
        print("Operation succesfull completed")
   
    def key_generator(self):
        self.alpha_data=self.read_alpha()
        new_list=random.sample(self.alpha_data, len(self.alpha_data))
        print("Enter name for file with new key")
        with open(self._enter_way("key"),'w',encoding='utf-8') as gen_key:
            i=0
            while i<len(self.alpha_data):
                string=self.alpha_data[i]+' '+new_list[i]+'\n'
                gen_key.write(string)
                i+=1 
        print("Key succesfull create")

class TRANSPOS(Parent):

   
    def _read_key_text(self):
        self.key_list=self.read_key()
        self.file_txt=self.read_txt()
     

    def _read_key_encrypt(self):
        self.key_list=self.read_key()
        self.encrypt_file=self.read_encrypt()

  

    def read_key(self):
        print("Need way to key file")
        key_list=[]
        with open(self._enter_way("key"),'r', encoding='utf-8') as key_file:
            line=key_file.readline()
            key_list=line.split(' ')
        return key_list

   
    def gener_key(self):   
        try:
            length=int(input("Enter length of key "))+1
            key_list=[x for x in range(1, length)]
            random.shuffle(key_list)
            with open(self._enter_way("key"),'w',encoding='utf-8') as gen_key:
                i=0
                string=''
                while i<len(key_list):                   
                    string=string+str(key_list[i])+' '
                    i+=1 
                gen_key.write(string)
        except Exception:
            print("wrong input")

    def encrypt(self):    
        self._read_key_text()
        if self.key_list[-1]=='':
            self.key_list.pop()
        length=len(self.key_list)
        line=self.file_txt.read()
        list_block_length=[]
        i=0
        my_list=list()
        print("Pleas, enter way for file with encode text ")
        with open(self._enter_way("encode"),'w',encoding='utf-8') as encode_file:
            encode_file.write("method of encryption: 2 - Transpositions!\n")
            for index in range(0,len(line),length):
                if index<=len(line):
                    my_list=list(line[index:index+length])
                i=0
                list_none=[None]*len(self.key_list)
                for item in my_list:
                    if len(my_list)<length:
                        my_list.append("q")
                    list_none[int(self.key_list[i])-1]=item              
                    i+=1
                string=''
                for item in list_none:
                    string=string+item
                encode_file.write(string)

    def revers(self):
            self._read_key_encrypt()
            line=self.encrypt_file.readline()
            line=self.encrypt_file.read() 
            if self.key_list[-1]=='':
               self.key_list.pop()
            length=len(self.key_list)
            print("Pleas, enter way for file with decrypt text ")
            with open(self._enter_way("txt"),'a',encoding='utf-8') as decode_file:
                for index in range(0,len(line),length):
                    if index<=len(line):
                        my_list=list(line[index:index+length])
                    i=0
                    string=''
                    for item in my_list:
                        ch=my_list[int(self.key_list[i])-1]
                        i+=1
                        string=string+ch
                    decode_file.write(string)


class XOR(Parent):
    
    def _alphabet(self):
        list_alph=list()
        i=0
        list_second_line=list()
        print("Pleas, enter way for file with alphabit ")
        alphabet=open(self._enter_way("alph"),"r",encoding='utf-8')
        return alphabet
        
    def gen_key(self): 
        list_key=list()
        alphabet_file=self._alphabet()
        list_alph=alphabet_file.read()
        gamma=int(input("Pleas, enter gamma "))
        i=0
        while i<gamma:
            ellement=random.randint(1,32)
            count=list_key.count(ellement)
            if count==0:
                list_key.append(ellement)
                i+=1
        print("Pleas, enter way for key file")
        with open(self._enter_way("key"),"w", encoding='utf-8') as key_file:
            key_file.write(list_alph)
            key_file.write("\n\nKey\n")
            for ellement in list_key:
                key_file.write(str(ellement))
                key_file.write(' ')


    def encrypt(self):
        text_file=self.read_txt()

        list_alph=list()
        list_key=list()
        index=0
        i=0
        print("Pleas, enter way to key file")
        with open(self._enter_way("key"),'r',encoding='utf-8') as key_file:
             for line in key_file:
                 if line=='Key\n':
                     line=key_file.readline()
                     list_key=line.split()
                     break
                 if i==1 and line!='\n':
                     list_alph.append(line[0])
                 if i==0:
                     list_second_line=line.split()
                     list_alph.append(line[0])
                     if len(list_alph)>1:
                        index=int(list_second_line[1])
                     else:
                         index=0
                     del(list_second_line)
                     i+=1
        print("Pleas, enter way for encode file ")
        string_line=''
        index_encode=0
        encode_ellement=''
        exit=0
        with open(self._enter_way("encode"),'w',encoding='utf-8') as encode_file:
            encode_file.write("method of encryption: 3 - Гомункул!\n")
            while exit!=100:
                text=text_file.read(len(list_key))
                i=0
                string_block=''
                new_index=0
                if text=='':
                    exit+=1
                for ch in text:
                    if 0<list_alph.count(ch):
                        index_encode=list_alph.index(ch)+index
                        key_ellement=list_key[i]
                        encode_ellement=list_alph[(index_encode+int(key_ellement))%len(list_alph)]
                        i+=1
                        string_block=string_block+encode_ellement
                    else:
                        string_block=string_block+ch
                string_line=string_line+string_block
            encode_file.write(string_line)
        print("Succesfull")


    def revers(self):
        encrypt_file=self.read_encrypt()
        list_alph=list()
        list_key=list()
        index=0
        i=0
        print("Pleas, enter way to key file")
        with open(self._enter_way("key"),'r',encoding='utf-8') as key_file:
             for line in key_file:
                 if line=='Key\n':
                     line=key_file.readline()
                     list_key=line.split()
                     break
                 if i==1 and line!='\n':
                     list_alph.append(line[0])
                 if i==0:
                     list_second_line=line.split()
                     list_alph.append(line[0])
                     if len(list_alph)>1:
                        index=int(list_second_line[1])
                     else:
                         index=0
                     del(list_second_line)
                     i+=1
        string_line=''
        index_encode=0
        encode_ellement=''
        exit=0
        print("Pleas, enter way for file with decrypt text ")
        with open(self._enter_way("txt"),'w',encoding='utf-8') as decrypt_file:
            line=encrypt_file.readline()
            while exit!=100:
                text=encrypt_file.read(len(list_key))
                i=0
                string_block=''
                new_index=0
                if text=='':
                    exit+=1
                for ch in text:
                    if 0<list_alph.count(ch):
                        index_encode=list_alph.index(ch)+index
                        key_ellement=list_key[i]
                        encode_ellement=list_alph[(index_encode-int(key_ellement))%(len(list_alph)+index)]
                        i+=1
                        string_block=string_block+encode_ellement
                    else:
                        string_block=string_block+ch
                string_line=string_line+string_block
            decrypt_file.write(string_line)
        print("Succesfull")

obj=REPLACE()
obj2=TRANSPOS()
obj3=XOR()

flag=True
i=0
while flag:
    try:
        print(".>> Main menu")
        print(".>> \t1) Encryption/decode")
        print(".>> \t2) Generate key")
        print(".>> \t3) Exit")
        command=int(input("create you choise "))
        if command<1 or command>3:
            print("Wrong command")
            i+=1
            if i>2:
                print('Too much errors')
                flag=False
                break
        if command==1:
            i=0
            main_menu=0
            while flag and main_menu!=1:
                print(".>> encryption/decode")
                print(".>> \t1) Encryption")
                print(".>> \t2) Decode")
                print(".>> \t3) Return to main menu")
                command=int(input("create you choise "))
                if command<1 or command>3:
                    print("Wrong command")
                    i+=1
                    if i>2:
                        print('Too much errors')
                        flag=False
                        break
                    if command==4:
                        main_menu=1
                        break
                if command==1:
                        i=0
                        main_menu=0
                        while flag:
                            print(".>> Choose method of encryption ")
                            print(".>> \t1) Replacement method")
                            print(".>> \t2) Transposition method")
                            print(".>> \t3) XOR method")
                            print(".>> \t4) Return to main menu")
                            command=int(input("create you choise "))
                            if command<1  or command>4:
                                print("Wrong command")                        
                                i+=1
                                if i>2:
                                    print('Too much errors')
                                    flag=False
                                    break
                            if command==1:
                                obj.Encrypt()
                            if command==2:
                                obj2.encrypt()
                            if command==3:
                                obj3.encrypt()
                            if command==4:
                                main_menu=1
                                break
                elif command==2:
                        i=0
                        main_menu=0
                        while flag:
                            print(".>> Choose method for decode ")
                            print(".>> \t1) Replacement method")
                            print(".>> \t2) Transposition method")
                            print(".>> \t3) XOR method")
                            print(".>> \t4) Return to main menu")
                            command=int(input("create you choise "))
                            if command<1 or command>4:
                                print("Wrong command")
                                i+=1
                                if i>2:
                                    print('Too much errors')
                                    flag=False
                                break
                            if command==1:
                                obj.revers()
                            elif command==2: 
                                obj2.revers()
                            elif command==3:
                                obj3.revers()           
                            if command==4:
                                main_menu=1
                                break
                elif command==3:
                    main_menu=1
                    break
        elif command==2:
            i=0
            main_manu=1
            while flag:
                print(".>> Choose encode method:")
                print(".>> \t1) Replacement method")
                print(".>> \t2) Transposition method")
                print(".>> \t3) XOR method")
                print(".>> \t4) Return to main menu")
                command=int(input("create you choise "))
                if command<1 or command>4:
                    print("Wrong command")
                    i+=1
                    if i>2:
                        print('Too much errors')
                        flag=False
                        break
                if command==1:
                    obj.key_generator()
                elif command==2:
                    obj2.gener_key()
                elif command==3:
                    obj3.gen_key()
                elif command==4:
                    main_menu=1
                    break
        elif command==3:
            flag=False
            break
        if main_menu==0:
            command=input("Return to main menu? Y/N").lower()
            if command[0]=='n':
                flag=False
                break
    except SyntaxError:
        print("Wrong command")
    except ValueError:
       print("Wrong command/wrong data in file")
    except PermissionError:
        print("Need more rights, file cant open")
        flag=False
        break
    except FileNotFoundError:
                print("File not found")
    except Exception:
        print("Program cant work. System error")
        flag=False
        break

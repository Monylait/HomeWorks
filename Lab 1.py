flag=True
j=0
while flag:
    value_1=int(input("enter val_1 "))
    value_2=int(input("enter val_2 "))
    command=input("input operation (+,-,/,*) - ")
    if command=='+':
           print(int(value_1)+int(value_2))
    elif command=='-':
           print(int(value_1)-int(value_2))
    elif command=='*':
            print(int(value_1)*int(value_2))S
    elif command=='/':
            print(int(value_1)/int(value_2))
    else :
        print('error') 
        j+=1

    for i in range(3):
        if j==3:
            print('Too much erors')
            flag=False
            break
        command = input("continue? (Y/N) ")
        if command=='Y':
            break
        elif command=='y':
            break
        elif command=='n':
            flag=False 
            break
        elif command=='N': 
            flag=False
            break
        else : 
            print('wrong input')
        if i==2:
            print('Too much errors')
            flag=False
            break

print("hello world")
flag=True
while flag:
    value_1=int(input("enter val_1 "))
    value_2=int(input("enter val_2 "))
    command=input("input operation (+,-,/,*) - ")
    #command [ +, -, *, /]

    if command=='+':
            print(int(value_1)+int(value_2))
    elif command=='-':
            print(int(value_1)-int(value_2))
    elif command=='*':
            print(int(value_1)*int(value_2))
    elif command=='/':
            print(int(value_1)/int(value_2))
    else :
        print('error')
    for i in range(3):
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
import random

def generate():
    x=random.randrange(0,10,1)
    y=random.randrange(0,10,1)
    result_list=list()
    check=0
    for i in range(0,11):
        strin_x=""
        for i_x in range(0,11):
            if i!=y and i_x!=x:
                strin_x=strin_x+"0"
            elif i==y and i_x==x:
                while len(strin_x)!=x:
                    strin_x=strin_x+"0"
                strin_x=strin_x+"1"
                while len(strin_x)!=10:
                    strin_x=strin_x+"0"
        result_list.append(strin_x)
        result_list.append("\n")
    with open("1.txt","w") as txt:
        strin_x=""
        for i in result_list:
            strin_x=strin_x+i
        txt.write(strin_x)


def read_file():
    result_list=list()
    with open("1.txt","r") as txt:
        for i in txt:
            i=i.split("\n")[0]
            result_list.append(i)
    return result_list


def find(sx,sy):
    res_list=read_file()
    power=res_list[sy]
    power=power[sx]
    print(power)
    flag=True
    while flag:
        

find(random.randrange(0,10,1),random.randrange(0,10,1))


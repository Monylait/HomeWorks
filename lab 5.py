import os
import math
from sys import argv
from multiprocessing import Process, Pool, current_process, Queue
from time import time, sleep
import timeit


start = time()
procs = list()


def Atkins(limiit:int,s1:int,s2:int,s3:int):
    sieve = [0] * (limiit + 1)
    if s1==1:
        limits=limiit
        i=1
        way="first.txt"
        status="1"
        print(i," ",limits)
        for x in range(i,int(limits)+1):
            for y in range(i,int(limits)+1):
                n = 4*int(pow(x,2)) + int(pow(y,2))
                if n<=limiit and (n%12==1 or n%12==5): 
                    sieve[n] = 1 
    elif s2==1:
        limits=limiit
        i=1
        way="second.txt"
        status="2"
        print(i," ",limits)
        for x in range(i,int(limits)+1):
            for y in range(i,int(limits)+1):
                n =3*int(pow(x,2)) + int(pow(y,2))
                if n<= limiit and n%12==7: 
                    sieve[n] = 1 
    elif s3==1:
        limits=limiit
        i=1
        way="third.txt"
        status="3"
        print(i," ",limits)
        for x in range(i,int(limits)+1):
            for y in range(i,int(limits)+1):
                n =3*int(pow(x,2)) - int(pow(y,2))
                if x>y and n<=limiit and n%12==11: 
                    sieve[n] = 1 

    for x in range(5,int(limiit)):
        if sieve[x] is 1:
            k=int(pow(x,2))
            for y in range(k,limiit+1,k):
                print("y ",y)
                sieve[y] = 0
    print(status)
    with open(way,"w",encoding='utf-7') as first:
        for id,x in enumerate(sieve):
            if x==1:
                result=id
                if result%5==0:
                    pass
                else:
                    string=str(result)+'\n'
                    first.write(string)
   
def read(way:str):
    first_list=list()
    with open(way,"r",encoding='utf-7') as first:
        first_list=first.read()
        first_list=first_list.split("\n")
        second_list=[None]*len(first_list)
        for id,i in enumerate(first_list):
            if i=='':
                pass
            else:
                new_i=int(i)
                if second_list.count(new_i)==0:
                    print (id)
                    second_list[id]=new_i
    return second_list


def starts(limit:int):

    with Pool(processes=3) as my_pool:
        p1 = my_pool.starmap(Atkins,
                             iterable=[
                                       [limit,1,0,0],
                                       [limit,0,1,0],
                                       [limit,0,0,1]
                                      ],
                             )
     
        my_pool.close()


def start_r():
    with Pool(processes=3) as my_pool:
        p1 = my_pool.starmap(read,
                             iterable=[
                                       ["first.txt"],
                                       ["second.txt"],
                                       ["third.txt"]
                                      ],
                             )
        my_pool.close()
        return p1


def enter():
    flag=True
    while flag:
        try:
            limit = int(input("Введите верхний лимит ваших вычислений: "))
            if limit>1000000001 or limit<=5:
                print("Pleas, enter new number")
            else:
                return limit
        except BaseException:
            print("Error")


if __name__ == '__main__':
    flag=False
    limit=int(argv[1])
    a=timeit.default_timer()
    starts(limit)
    first_list=list()
    time_list=start_r()
    result_list=time_list[0]+time_list[1]+time_list[2]
    while None in result_list: result_list.remove(None)
    result_list.sort()

    with open("result.txt", "w",encoding='utf-8') as file:
        file.write("2\n3\n5\n")
        for p in result_list:
            string=""+str(p)+"\n"
            file.write(string)
    
    print("Алгоритм считал:", timeit.default_timer()-a, "секунд\nРезультат смотрите в файле result")

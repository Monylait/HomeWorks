import os
import math
from multiprocessing import Process, Pool, current_process, Queue
from time import time, sleep
import timeit


start = time()
procs = list()


def Atkins(limiit:int,s1:int,s2:int,s3:int):
    if s1==1:
        limit=int(limiit/3)
        limits=limit
        i=1
        way="first.txt"
        status="1"
    elif s2==1:
        limit=int(limiit/3)
        i=int(math.sqrt(limit))
        limits=limit*2
        way="second.txt"
        status="2"
    elif s3==1:
        limit=int(limiit/3)
        i=int(math.sqrt(limit*2))
        limits=limiit
        way="third.txt"
        status="3"
    sieve = [0] * (limit + 1)
    check=0
    for x in range(i,int(math.sqrt(limits))+1):
        for y in range(i,int(math.sqrt(limits))+1):
            n = 4*x*x + y*y
            if n<=limit and (n%12==1 or n%12==5): 
                sieve[n] = 1 
            n = 3*x*x + y*y
            if n<= limit and n%12==7: 
                sieve[n] = 1 
            n = 3*x*x - y*y
            if x>y and n<=limit and n%12==11: 
                sieve[n] = 1 
    toc=timeit.default_timer()
    for x in range(i*5,int(math.sqrt(limit))):
        if sieve[x] is 1:
            for y in range(x*x,limit+1,x*x):
                tic=timeit.default_timer()
                if tic-toc>=1:
                    print(y)
                    toc=timeit.default_timer()
                sieve[y] = 0
        else:
             tic=timeit.default_timer()
             if tic-toc>=1:
                   print(y)
                   toc=timeit.default_timer()
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
    return first_list


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


def monitor():
 pass   

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
    limit=enter()
   # moni=multiprocessing.Process(target=monitor)
  #  moni.start()
    a=timeit.default_timer()
  #  for x in range(10000000):
  #      for y in range(10000000000):
  #          z=timeit.default_timer()
  #          if z-a>=5:
  #              print("lol")
  #              a=timeit.default_timer()
  #          pass
    starts(limit)
    first_list=list()
    time_list=start_r()
    result_list=time_list[0]+time_list[1]+time_list[2]
    with open("result.txt", "w",encoding='utf-8') as file:
        file.write("2\n3\n5\n")
        for p in result_list:
            string=""+str(p)+"\n"
            file.write(string)
    
    print("Алгоритм считал:", timeit.default_timer()-a, "секунд\nРезультат смотрите в файле result")
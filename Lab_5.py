import os
import math
from sys import argv
import multiprocessing as mp
import time
import timeit

def Atkins(limit: int, s1: int, s2: int, s3: int):
    if s1 == 1:
        way = "first.txt"
        status = "1 процесс завершил работу"
        tick = 3
        i=1
    elif s2 == 1:
        way = "second.txt"
        status = "2 процесс завершил работу"
        tick = 3
        i=2
    elif s3 == 1:
        way = "third.txt"
        status = "3 процесс завершил работу"
        tick = 3
        i=3
    sieve = [False] * (limit+1)
    check = 0
    t=time.time()
    t=int(t)
    for x in range(i, int(math.sqrt(limit)) + 1, 3):
        for y in range(1, int(math.sqrt(limit)) + 1):
            j=0
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
            if int(time.time())-t==6:
                print(x)
                t=time.time()
                t=int()
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
            if int(time.time())-t==9:
                print(x)
                t=time.time()
                t=int(t)
    with open(way, "w", encoding='utf-7') as file_atk:
        for id, x in enumerate(sieve):
            string = str(x) + '\n'
            file_atk.write(string)
    print(status + '\n')


#def read(way: str,s1: int, s2: int, s3: int) -> list:
#    print("start read")
#    if s1 == 1:
#        status = "1 процесс"
#    elif s2 == 1:
#        status = "2 процесс"
#    elif s3 == 1:
#        status = "3 процесс"
#    t=time.time()
#    t=int(t)
#    with open(way, "r", encoding='utf-7') as first:
#        first_read = first.read()
#        first_list = first_read.split("\n")
#        second_list = [0]*len(first_list)
#        for id, i in enumerate(first_list):
#            if int(time.time())-t==9:
#                print(i)
#                t=time.time()
#                t=int(t)
#            if i == '':
#                pass
#            elif int(i)==91 or int(i)%91==0:
#                pass
#            else:
#                new_i = int(i)
#                count_list = first_list.count(i)
#                if count_list == 1:
#                    second_list[id] = new_i
#    second_list.remove(0)
#    return second_list



def read_files()->list:
    print("start read 1")
    with open('first.txt','r',encoding='utf-8') as file_1:
        first_read = file_1.read()
        list_1 = first_read.split("\n")
    print("start read 2")
    with open('second.txt','r',encoding='utf-8') as file_2:
            first_read = file_2.read()
            list_2 = first_read.split("\n")
    print("start read 3")
    with open('third.txt','r',encoding='utf-8') as file_3:
        first_read = file_3.read()
        list_3 = first_read.split("\n")
    #while 0 in list_1:
    #    list_1.remove(0)
    #while 0 in list_2:
    #    list_2.remove(0)
    #while 0 in list_3:
    #    list_3.remove(0)
    j=0
    #for id_1,x_1 in enumerate(list_1):
    #    for id_2,x_2 in enumerate(list_2):
    #        for id,x in enumerate(list_3):
    #            if list_1[id]==True:
    #                j+=1
    #            if list_2[id]==True:
    #                j+=1
    #            if list_3[id]==True:
    #                j+=1
    #            if j==2:
    #                if list_1[id]==True:
    #                    list_1[id]=not list_1[id]
    #                if list_2[id]==True:
    #                    list_2[id]=not list_2[id]
    #                if list_3[id]==True:
    #                    list_3[id]=not list_3[id]
    #            if j==3:
    #                if list_1[id]==True:
    #                    list_1[id]=not list_1[id]
    #                if list_2[id]==True:
    #                    list_2[id]=not list_2[id]
    #                if list_3[id]==True:
    #                    list_3[id]=not list_3[id]
    list_123=[False]*len(list_1)
    lens=len(list_1)
    for i in range(0,lens):
        if list_1[i]=="False":
            z=False
        else: z=True
        if list_2[i]=="False":
            zx=False
        else: zx=True
        if list_3[i]=="False":
            xz=False
        else: xz=True
        list_123[i]=(z+zx+xz)%2
    list_4=[False]*len(list_123)
    for id,x in enumerate(list_123):
        if x==1:
            if id%5==0:
                pass
            else:
                list_4[id]=id
    return list_4


def starts(limit: int):
    with mp.Pool(processes=3) as my_pool:
        p1 = my_pool.starmap(Atkins,
                             iterable=[
                                       [limit, 1, 0, 0],
                                       [limit, 0, 1, 0],
                                       [limit, 0, 0, 1]
                                      ],
                             )
        my_pool.close()


#def start_read():
#    with mp.Pool(processes=3) as my_pool:
#        p1 = my_pool.starmap(read,
#                             iterable=[
#                                       ["first.txt",1, 0, 0],
#                                       ["second.txt",0, 1, 0],
#                                       ["third.txt",0, 0, 1]
#                                      ],
#                             )
#        my_pool.close()
#        print("end read")
#        return p1


if __name__ == '__main__':
    try:
        if int(argv[1]) > 0:
            pass
        elif int(argv[1]) < 0:
            raise Exception
        elif int(argv[1]) == 0:
            raise Exception
        else:
            raise Exception
        limit = int(argv[1])
        a = timeit.default_timer()
        starts(limit)
        time_list = read_files()
        while len(time_list)>limit:
            time_list.pop()
        while False in time_list:
            time_list.remove(False)
        time_list.sort()
        with open("result.txt", "w", encoding='utf-8') as file:
            file.write("2\n3\n5\n")
            for p in time_list:
                string = ""+str(p)+"\n"
                file.write(string)
        print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")
   # except Exception:
   #     print("Неправильный аргумент")
   # except BaseException:
   #     print("Вы нажали на Ctrl + C")
    except FileNotFoundError:
        pass
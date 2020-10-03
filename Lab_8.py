import random


def Evklid(x,y):
    a2=1
    a1=0
    b2=0
    b1=1
    while(y!=0):
        q=int(x/y)
        r=(x-q*y)
        a=a2-q*a1
        b=b2-q*b1
        x=y
        y=r
        a2=a1
        a1=a
        b2=b1
        b1=b
    a=a2
    b=b2
    return x


def fast_pow(n):
    a=int(input("Enter a!=0\n>>> "))
    flag=True
    while(flag):
        if a!=0:
            break
        else:
            a=int(input("Enter normal a!=0\n>>> "))
    b=1
    if n%2!=0:
        b=a
        n=n-1
    while (n!=1):
        a=a*a
        n=int(n/2)
    a=a*b
    print (a)


def fast_fast_pow(a,s,n):
    y=1
    x=1
    j=n
    if s%2!=0:
        y=a
        s=s-1
    while (s!=1):
        a=a*a
        s=int(s/2)
    a=a*y
    x=a%n
    print (x)


def Jakobi(a,b):
    #while True:
        #g=1
        #if a==0:
        #    return 0
        #elif a==1:
        #    return g
        #k=0
        #while(a%2==0):
        #    a=a/2 
        #    k+=1
        #a1=int(a)
        #if k%2==0:
        #    s=1
        #elif k%2!=0 and ((n%8==1%8) or (n%8==7%8)):
        #    s=1
        #elif k%2!=0 and ((n%8==3%8) or (n%8==5%8)):
        #    s=-1
        #if a1==1:
        #    return g*s
        #if n%4==3%4 and a1%4==3%4:
        #    s=-s
        #n=a1
        #g=g*s #работает средне
    if Evklid(a,b)!=1:
        return 0
    r=1
    if a<0:
        a=-a
        if b%4==3:
            r=-r
    while a!=0:
        t=0
        while a%2==0:
            t+=1
            a=a/2
        if t%2!=0:
            if b%8==3 or b%8==5:
                r=-r
        if a%4==b and b%4==3:
            r=-r
        c=a
        a=b%c
        b=c
    return r


def Test_Ferma(n):
    a=int(input("Enter 2<=a<=n-2\n"))
    flag=True
    while(flag):
        if a<=n-2 and 2<=a:
            break
        a=int(input("Enter normal 2<=a<=n-2\n"))
    r=pow(a,(n-1))%n
    if r==1:
        print(n," Число вероятно простое")
    else:
        print(n," Число составное\n")


def Test_S_SH(n):
    a=random.randint(2,n-2)
    r= (pow(a,((n-1)/2))%n)
    if r!=1 and r!=n-1:
        print("Число ",n," составное")
        return 0
    s=Jakobi(a,n)
    if r%n==s%n:
        print("Число ",n,"вероятно, простое")
        return 0
    else:
        print("Число ",n," составное")
        return 0


def Test_M_R(n):
    w=n-1
    s=0
    r=1
    while w!=1:
        if w%2==0:
            w=w/2
            s=s+1
        else:
            r=w
            break
    a=random.randint(2,n-2)
    y=(pow(a,r))%n
    if y!=1 and y!=n-1:
        j=1
        if j<=s-1 and y!=n-1:
            y=(y*y)%n
            if y==1:
                return 0
            j=j+1
        if y!=n-1:
            return 0
    return 1


def convert_base(num, to_base=10, from_base=2):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def Gen_Easy_Num(k,t):
    flag=True
    while flag:
        j=k-1
        mass_p=list()
        mass_p.append(1)
        while j>1:
            x=random.randint(0,1)
            mass_p.append(x)
            j-=1
        mass_p.append(1)
        string=''
        for item in mass_p:
            string+=str(item)
        p=convert_base(string, 10, 2)
        i=1
        x=0
        while i<t:
            if int(p)%2==0:
                break
            x=Test_M_R(int(p))
            if x==1:
                i+=1
            if x==0:
                break
        if i==t:
            return p


def first_pow(m,b,a):
    d=Evklid(a,m)
    if b%d!=0:
        print("Решений нет")
        return 0
    elif d!=1:
        a1=int(a/d)
        b1=int(b/d)
        m1=int(m/d)
        c=(m1+1)/a1

    else:
        pass


flag=True
while(flag):
    try:
        touch=int(input("\t\t>>>choose function<<<\n"
               "1)    Обобщенный (расширенный) алгоритм Евклида\n"
               "2)    Алгоритм быстрого возведения в степень\n"
               "3)    Алгоритм быстрого возведения в степень по модулю\n"
               "4)    Вычисление символа Якоби\n5)    Тест Ферма\n"
               "6)    Тест Соловэя-Штрассена\n7)    Тест Миллера-Рабина\n"
               "8)    Генерация простого числа заданной размерности\n"
               "9)    Решение сравнения первой степени\n10)   Решение сравнения второй степени\n"
               "11)   Решение системы сравнений\n12)   Решение системы сравнений\n>>>>> "))
        if touch>0 and touch<14:
            if touch==1:
                x=int(input("Enter x\n>>> "))
                y=int(input("Enter y\n>>> "))
                flag_Evklid=True
                while(flag_Evklid):
                    if x>=y:
                        break
                    else:
                        x=int(input("Enter normal x>=y\n>>> "))
                        y=int(input("Enter normal y<=x\n>>> "))
                print(Evklid(x,y))
                next=input("Return program? Y/N\n>>> ").lower()
                if next=="y":
                    pass
                else:
                    flag=False
            if touch==2:
                n=int(input("Enter n>=2\n>>> "))
                flag_Ferma=True
                while(flag_Ferma):
                    if n>=2:
                        break
                    else:
                        n=int(input("Enter normal n>=2\n>>> "))
                fast_pow(n)
                next=input("Return program? Y/N\n>>> ").lower()
                if next=="y":
                    pass
                else:
                    flag=False
            if touch==3:
                print("a^s mod n\n")
                n=int(input("Enter n>=0\n>>> "))
                a=int(input("Enter a>=0\n>>> "))
                s=int(input("Enter s>=0\n>>> "))
                flag_Ferma=True
                while(flag_Ferma):
                    if n>=0 and a>=0 and s>=0:
                        break
                    else:
                        n=int(input("Enter normal n\n>>> "))
                        a=int(input("Enter normal a\n>>> "))
                        s=int(input("Enter normal s\n>>> "))
                fast_fast_pow(a,s,n)
                next=input("Return program? Y/N\n>>> ").lower()
                if next=="y":
                    pass
                else:
                    flag=False
            if touch==4:
                a=int(input("Enter a, 0<=a<n\n>>> "))
                n=int(input("Enter n, n>=3\n>>> "))
                flag_Evklid=True
                while(flag_Evklid):
                    if n>a and n>=3 and a>=0 and n%2!=0:
                        break
                    else:
                        a=int(input("Enter normal a, 0<=a<n\n>>> "))
                        n=int(input("Enter normal n, n>=3\n>>> "))
                g=Jakobi(a,n)
                print("Jakobi simbol = ",g)
                next=input("Return program? Y/N\n>>> ").lower()
                if next=="y":
                    pass
                else:
                    flag=False
            if touch==5:
                 n=int(input("Enter n>=5\n>>> "))
                 flag_Ferma=True
                 while(flag_Ferma):
                     if n>=5 and n%2!=0:
                         break
                     else:
                         n=int(input("Enter normal n>=5\n>>> "))
                 Test_Ferma(n)
                 next=input("Return program? Y/N\n>>> ").lower()
                 if next=="y":
                     pass
                 else:
                     flag=False
            if touch==6:
                 n=int(input("Enter n>=5\n>>> "))
                 flag_Ferma=True
                 while(flag_Ferma):
                     if n>=5 and n%2!=0:
                         break
                     else:
                         n=int(input("Enter normal n>=5\n>>> "))
                 Test_S_SH(n)
                 next=input("Return program? Y/N\n>>> ").lower()
                 if next=="y":
                     pass
                 else:
                     flag=False
            if touch==7:
                 n=int(input("Enter n>=5\n>>> "))
                 flag_Ferma=True
                 while(flag_Ferma):
                     if n>=5 and n%2!=0:
                         break
                     else:
                         n=int(input("Enter normal n>=5\n>>> "))
                 x=Test_M_R(n)
                 if x==0:
                     print("Число ",n,"составное")
                 elif x==1:
                     print("Число ",n,"вероятно простое")
                 next=input("Return program? Y/N\n>>> ").lower()
                 if next=="y":
                     pass
                 else:
                     flag=False
            if touch==8:
                k=int(input("Enter k>=1\n>>> "))
                t=int(input("Enter t>=1\n>>> "))
                flag_Ferma=True
                while(flag_Ferma):
                    if k>=1 and t>=1:
                        break
                    else:
                        k=int(input("Enter normal k>=1\n>>> "))
                        t=int(input("Enter normal t>=1\n>>> "))
                print("Create number p = ",Gen_Easy_Num(k,t))
                next=input("Return program? Y/N\n>>> ").lower()
                if next=="y":
                    pass
                else:
                    flag=False
            if touch==9:
                print("a*x =b mod m\n")
                m=int(input("Enter m>=0\n>>> "))
                b=int(input("Enter b>=0\n>>> "))
                a=int(input("Enter a>=0\n>>> "))
                flag_Ferma=True
                while(flag_Ferma):
                    if n>=0 and a>=0 and s>=0:
                        break
                    else:
                        m=int(input("Enter m>=0\n>>> "))
                        b=int(input("Enter b>=0\n>>> "))
                        a=int(input("Enter a>=0\n>>> "))
                first_pow(m,b,a)
                next=input("Return program? Y/N\n>>> ").lower()
                if next=="y":
                    pass
                else:
                    flag=False
            if touch==10:
                pass
            if touch==11:
                pass
            if touch==12:
                pass
            if touch==13:
                pass
        else:
            print("\n>>>Error, create normal choose<<<\n")
    except FileNotFoundError:
        print("Try more")



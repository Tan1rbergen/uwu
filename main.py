import math
'''a = float(input("kez kelgen san = "))
if a<20 and a>0:
    print(a,'griven')

A = float(input("san engiz = "))
if A%3==0:
    print('true')
else:
    print('false')

B = float(input("san engiz = "))
T = float(input("san tagy engiz = "))
f=B**2-T**2
k= abs(f)
if f>k:
    print('kvadrattardyn ayirymy ulken')
elif f==k:
    print('ten')
else :
    print('modul ulken')


x = float(input("san engiz = "))
y = float(input("san tagy engiz = "))
if x**2 +y**2<1 and x**2 + y**2>0 and x**2 +y**2<4:
    print('jatady')
else:
    print('jatpaidy')

m = 0
while True:
    a = int(input())
    if a == 0:
        break
    elif a%3==0:
        ен киши ортак еселик
        кос факториал
        сан табу керек
        жай сан табатын алгоритм

# for i in range(1,a+1):
#     if a%1==0 and a%i==0:
#         e+=1
#         if e==2:
#             print("zhai san")
#         else:
#             print("zhai san emes")

a =int(input("a = "))
b =int(input("b = "))
if a>0:
    c=a / 2
else:
    c = (a + b) / 2
print("c = ", c)

t = -3
if t<5:
    print("кун салкын, киініп алыныз")
else:
    print("кун ыстык, кыдыруга болады")

month = "karasha"
if month != "kantar":
    print("jana jyl toylanbaydy")
    print("shyrsha bezendirilmeydi")
else:
    print("jana jyl qutty bolsyn")

a=5
if a<10:
    print("{0} sany {1} sanynan kishi".format(a,10))
else:
    print("{0} sany {1} sanynan kishi".format(a,10))

a =5
b = 6
c =100
if a>4:
    if b>a:
        if c>b:
            print("%2d<%2d<%2d"%(a,b,c))

a = int(input("a = "))
b=  int(input("b = "))
if a>=50:
    print("siz %d bagasymen ottiniz"%a)
elif b>=80 and b<=100:
    print("emtihannan ozi otipti biraq dosynyn bagasy {} bolypty".format(a))
else:
    print("basqalarda myqty emes, byraq siz jazgy semestrge qaldynyz")'''
'''
s = 0
while True:
    a = int(input())
    if a == 0:
        break
    elif a%3==0:
        if s<a:
            s=a
print (s)

s = 0
for a in range(1, 1000):
    for i in range(1, 1000):
        if a%i==0:
            s+=1
        elif s==5:
            print(a)'''
# import random
# s=[]
# for i in range(len(s)):
#     s.append(s[i])

# from random import randint
# max=0
# min=0
# sum=0
# a = []
# s = int(input('s= '))
# for i in range(s):
#     a.append(randint(-100, 1000))
# print(*a)
# #
# for i in range(s):
#     if max<a[i]:
#         max=a[i]
#     elif min>a[i]:
#         min=a[i]
# n= max+min
# for i in range (s):
#
#      sum+=a[i]
# print(sum-n)

# t1 =()
# t2 =(5,)
# t3 =(1, "str", (3,4))
# t4 =1,"str", (3,4)
# print(t1, t2, t3,t4)



# 1shi teris sannan 2shi teris san arasyndagy sandardy bolek kortej
# from random import randint
#
# k =()
# s = int(input('s= '))
# for i in range(s):
#        k.insert(randint(-100, 1000))
# print(k)
# from random import*
# q = 0
# w = 0
# e = 0
# b=[]
# s = int(input('s= '))
# for i in range(s):
#     b.append(randint(-50, 100))
# a = tuple(b)
# print(a)
# t=[]
# for i in range(len(a)):
#     if a[i]<0:
#         q +=1
#     if q==1:
#         t.append(a[i+1])
#     if q==2:
#         break
# t.pop()
# s = tuple(t)
# print(s)

# import math
# from random import*
# min = 0
# q =int(input("s= "))
# w =int(input("d= "))
# a=[]
# for i in range(q):
#     a.append([])
#     for j in range(w):
#         a[i].append(randint(-100, 100))
#
# for i in range(len(a)):
#     print(sorted(a[i]))
# for j in range(len(a)):
#     for i in range(len(a)):
#          if min > a[j][i]:
#             min = a[j][i]
#             r=i
#             t=j
#
# print(min, "qatardagy indeks= ", t, "bagandagy indeks= ", r)
# import random
# m=[[random.randint(0,100) for i in range(3)] for j in range(3)]
#
# for i in m:
#     for j in i:
#         print(j,end="\t")
#     print()
#
# sum=0
#
# for j in range(3):
#     for i in range(3):
#         if i==j:
#             sum += m[j][i]
# print(sum)
# fib1 = 1
# fib2 = 2
# n=input("nomer ")
# n= int(n)-2
# while n>0:
#     fib1, fib2= fib2, fib1+fib2
#     n-=1
# print("n= ", fib2)
# count = 0
# s = input("s = ")
# print(s.index(' '))
#
# k=''
# for i in range(len(s)):
#     if i==3:
#         continue
#
#     else:
#         k=k+s[i]
#
#
# print(k)


# count = 0
# s = input('s=')
# b=list(s)
# for i in b:
#     if i==" ":
#         count += 1
#     if count == 1:
#         b.remove(i)
#         break
# e=''.join(b)
# print(e)
# b=list(s)
# print(b.remove(b.index(' ')))

# from random import*
#
# def func():
#     b=[]
#     s = int(input('s= '))
#     for i in range(s):
#         b.append(randint(1, 20))
#     print(b)
#     a = str(b[0])
#     c = str(b[1])
#     if len(a) > len(c):
#         print(b[0])
#     elif len(a) < len(c):
#         print(b[1])
#     else:
#         print("Ten")
# func()
#
# def func1():
#     b = []
#     s = int(input('s= '))
#     for i in range(s):
#         b.append(randint(-50, 200))
#     print(b)
#     print(max(b))
#
# func1()

# import random
# l = []
# max = 0
# indeks=0
# i = 0
# while i<6:
#     l.append(random.randint(1, 200))
#     i+=1
# print(l)
# for i in range(len(l)):
#     if max<l[i]:
#         max = l[i]
#         indeks = i
# print("max san =", max, "indeks = ", indeks)





# s = ["alma", "almurt", "juzim", "limon"]
# a = [random.randint(400, 1200)for i in range(4)]
# print(s)
# print (a)
# min = 1500
# mini=0
# for i in range(len(a)):
#     if min > a[i]:
#         min = a[i]
#         mini = i
# print(s[mini],' ',a[mini] )

# s = int(input("san engiz = "))
# sandar = [1,2,8,8,3,4,8,5]
# lst = []
# count = 0
# for i in range(len(sandar)):
#     if sandar[i] == s :
#         count += 1
#         lst.append(i)
# print(lst, count, 'ret kezdesedi')



# import operator
# import datetime
#
# class MyError(Exception):
#     def __init__(self,text):
#         self.text=text
#
# class Train:
#
#     def __init__(self, direction, number, time, place):
#
#         self.direction = direction
#         self.number = number
#         self.time = time
#         self.place = place
#         Student.emp_count += 1
#     id+=1
#     def display_count(self):
#         print('Всего сттудентов: %d' % Student.emp_count)
#
#     def display(self):
#         print('id:{}'
#               ' Имя: {} '
#               ' fac: {}'
#               ' course: {}'
#               ' born year:{} '.format(self.id,self.name,self.fac,self.course,self.born_year))
#
#     def sort_choice(self,Data,choice):
#         result = sorted(Data, key=operator.attrgetter(choice))  # Сортировка по атрибуту name
#         for i in result:
#             i.display()
#
#
#
# s1 = Student( "Aryn", "FIT", 4, 2004)
# s2 = Student( "Madina", "FEN", 2, 2005)
# s3 = Student( "Ainur", "FIT", 3, 2003)
# s4 = Student( "ARuzhan", "FIT", 1, 2003)
# e = [s1, s2, s3, s4]
#
#
#
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))  # Сортировка по атрибуту name
#     for i in result:
#         i.display()
#
# while True:
#     print('\n1.список студентов заданного факультета')
#     print('2.список студентов для каждого факультета и курса ')
#     print('3.список студентов, родившихся после заданного года ')
#     print('4.список студентов учебной группы ')
#     print('5.exit ')
#     n = (input())
#
#     try:
#         n=int
#         if(n<0):
#             raise MyError("Syz terys san engyndyn on engyz")
#         if (n == 1):
#             fac = input("Enter Facultet")
#
#             for i in e:
#                 if (fac.upper()).strip() == i.fac:
#                     i.display()
#
#         elif n == 2:
#             fac = input("Enter Facultet")
#             course = int(input("Enter course"))
#             for i in e:
#                 if fac == i.fac and course == i.course:
#                     i.display()
#         elif n==3:
#             k=int(input(("Sort time \n1. Name \n2. course" )))
#             if(k==1):
#                 result = sorted(e, key=operator.attrgetter('name'))  # Сортировка по атрибуту name
#                 for i in result:
#                     i.display()
#             elif k==2:
#                 sort_choice(e,'course')
#         elif n==5:
#             break
#
#         else:
#             print("Syz suragan akparat zhok")
#     except ValueError:
#         print("Mandy durys berynyz")
#     except MyError as mr:
#         print(mr)
# print("Всего студентов: %d" % Student.emp_count)

# class Train:
#
#     def __init__(self, direction, number, time, place):
#
#         self.direction = direction
#         self.number = number
#         self.time = time
#         self.place = place
#
#     def show(self):
#         print(self.direction, self.number, self.time, self.place)
#
# s1 = Train("Almaty", 15, "16:10", "kupe")
# s2 = Train("Astana", 15, "14:30", "kupe")
# s3 = Train("Taraz", 10, "16:10", "obshi")
# s4 = Train("Almaty", 12, "20:10", "luxe")
# s5 = Train("Karagandy", 18, "20:10", "luxe")
# s = [s1,s2,s3,s4,s5]
# q = input("kai punkt: ")
# for i in range(len(s)):
#     if q == s[i].direction:
#         print(s[i].show())
#
# w = input("kai uaqyt: ")
#
# for i in range(len(s)):
#     if w == i.time:
#         print(i.show)

# while True:
#     print("1.Cписок поездов, следующих до задонного пункта назначения")
#     print("2.Cписок поездов, следующих до задонного пункта назначения и отправляющихся после задонного часа")
#     print("3.Список поездов, отправляющего до заданного пункта и имеющихся общие места")
#     print("4.Выход")
#     n=int(input("Enter n: "))
#     if n==1:
#         q=input("пунт назначения")
#         for i in s:
#             if q==i.direction:
#                 i.show()
#     elif n==2:
#         q=input("Пункт назначения")
#         t=input("Время отправление")
#         for i in s:
#             if q==i.direction and t==i.time:
#                 i.show()
#     elif n==3:
#         q=input("Пункт назначения")
#         o="obshi"
#         for i in s:
#             if q==i.direction and o==i.place:
#                 i.show()
#     elif n==4:
#         break
# from random import randint
# #
# a = [[randint(-10 ,100) for i in range(4)]for j in range(4)]
# for i in a:
#     print(i)
# index = 0
# min = 1000
# for i in range(len(a)):
#     for j in range(len(a)):
#         if min > a[i][j]:
#             min = a[i][j]
#             index=i
# print()
# print(a[index])
# from random import randint
# N = int(input("кол столбцов"))
# M = int(input("кол строк"))
# lst=[[randint(1, 9) for i in range(N)] for i in range(M)]
# print(lst)
# for i in lst:
#     print()
#     for j in i:
#         print (j, end=" ")
# kol=0 #количество одинаковых элементов равно нулю
# num_str=0# индекс строки
# for i in range(M): #цикл по всем элементам матрицы
#     for j in range(N):
#         kol_new=lst[i].count(lst[i][j])# подсчитываю кол-во определённого [i][j] символа в i-строке
#         if kol_new>kol:
#             kol=kol_new
#             num_str=i
# print()
# print(num_str)
# print()
# sum = 0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i<j:
#             sum += a[i][j]
# print('сумма выш лев диог=',sum)

# s = {15,16,45,50,41,10,60,81}
# a = {45,14,52,50,15,20}
# s.add(2)
#
# print("s= ",s)
# print("union: ",s.union(a))
# print("intersection: ",s.intersection(a))
# print("difference: ",s.difference(a))
# print("issuperset: ",s.issuperset(a))
# print("symmetric: ",s.symmetric_difference(a))
# print("issubset: ",s.issubset(a))
# print("remove: ",s.remove(2))
# print("pop: ",s.pop())
# print("clear: ",a.clear())

# 15. Создать объект класса Дом, используя классы Окно, Дверь.
# Методы: закрыть на ключ, вывести на консоль количество окон, дверей.

# class Window:
#     def fun1(self):
#         print("открыть")
#
# class Door:
#     def fun2(self):
#         print("закрыть на ключ")
#
# class House:
#     def __init__(self, okna, dver):
#         self.okna = okna
#         self.dver = dver
#
#     def show(self):
#         print()
# import operator
# import datetime
#
# class MyError(Exception):
#     def _init_(self,text):
#         self.text=text
#
# class Student:
#     emp_count = 0
#     id=0
#
#     def _init_(self, name, fac, course, date):
#
#         self.name = name
#         self.fac = fac
#         self.course = course
#         self.born_year = date
#         Student.emp_count += 1
#     id+=1
#     def display_count(self):
#         print('Всего сттудентов: %d' % Student.emp_count)
#
#     def display(self):
#         print('id:{}'
#               ' Имя: {} '
#               ' fac: {}'
#               ' course: {}'
#               ' born year:{} '.format(self.id,self.name,self.fac,self.course,self.born_year))
#
#     def sort_choice(self,Data,choice):
#         result = sorted(Data, key=operator.attrgetter(choice))  # Сортировка по атрибуту name
#         for i in result:
#             i.display()
#
#
#
# s1 = Student( "Aryn", "FIT", 4, 2004)
# s2 = Student( "Madina", "FEN", 2, 2005)
# s3 = Student( "Ainur", "FIT", 3, 2003)
# s4 = Student( "ARuzhan", "FIT", 1, 2003)
# e = [s1, s2, s3, s4]
#
#
#
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))  # Сортировка по атрибуту name
#     for i in result:
#         i.display()
#
# while True:
#     print('\n1.список студентов заданного факультета')
#     print('2.список студентов для каждого факультета и курса ')
#     print('3.список студентов, родившихся после заданного года ')
#     print('4.список студентов учебной группы ')
#     print('5.exit ')
#     n = (input())
# class Manger:
#     def __init__(self,log,pas,name):
#         self.log = log
#         self.pas = pas
#         self.name = name
# def menedzher(e):
#     print("\nLogin : \nParol : ")
#     a = input("L:")
#     b = input("P:")
#     if a == m1.log and b == m1.pas:
#         print("siz AKk ka kirdiniz\n")
#         print("Kerekti klienttin nomerin tandanyz: ")
#         num_id = int(input())
#         for i in range(len(k)):
#             if num_id == k[i].id:
#                 print("Kredit: ", k[i].a)
#                 if k[i].a == "Yes":
#                     print("sent mes: kredit tole")
#                 elif k[i].a == "No":
#                     print("sent mes: kredit alasnba e")
#
# class Klient:
#     def __init__(self, id,kr):
#         self.id = id
#         self.a=kr
#
# m1 = Manger("as","11","at")
# k1 = Klient(123,"Yes")
# k2 = Klient(323,"No")
# k = [k1,k2]
#
# while True:
#     a = int(input())
#     menedzher(a)









#     try:
#         n=int
#         if(n<0):
#             raise MyError("Syz terys san engyndyn on engyz")
#         if (n == 1):
#             fac = input("Enter Facultet")
#
#             for i in e:
#                 if (fac.upper()).strip() == i.fac:
#                     i.display()
#
#         elif n == 2:
#             fac = input("Enter Facultet")
#             course = int(input("Enter course"))
#             for i in e:
#                 if fac == i.fac and course == i.course:
#                     i.display()
#         elif n==3:
#             k=int(input(("Sort time \n1. Name \n2. course" )))
#             if(k==1):
#                 result = sorted(e, key=operator.attrgetter('name'))  # Сортировка по атрибуту name
#                 for i in result:
#                     i.display()
#             elif k==2:
#                 sort_choice(e,'course')
#         elif n==5:
#             break
#
#         else:
#             print("Syz suragan akparat zhok")
#     except ValueError:
#         print("Mandy durys berynyz")
#     except MyError as mr:
#         print(mr)
# print("Всего студентов: %d" % Student.emp_count)


# 6. Камни. Определить иерархию драгоценных и полудрагоценных камней.
# Отобрать камни для ожерелья. Подсчитать общий вес (в каратах) и стоимость.
# Провести сортировку камней ожерелья на основе ценности. Найти камни в ожерелье,
# соответствующие заданному диапазону параметров прозрачности.

from random import randint

#
# class PreciousStone:
#     def __init__(self, name, weight, cost):
#         self.name = name
#         self.weight = weight
#         self.cost = cost
#
#     def get_info(self):
#         print(self.name, self.weight, self.cost)
#
# t1 = PreciousStone("Almaz", 1, 150000)
# t2 = PreciousStone("Rubin", 5, 100000)
# t3 = PreciousStone("Saphir", 3, 75000)
# t4 = PreciousStone("Izumrud", 6, 50000)
# t5 = PreciousStone("Gold", 2, 25000)
# t = [t1, t2, t3, t4, t5]
# def compute(a):
#     sumw = 0
#     sumc = 0
#     for i in range(a):
#         i = randint(0, 4)
#         print(t[i].name, "  ", t[i].weight, "  ", t[i].cost)
#         sumw += t[i].weight
#         sumc += t[i].cost
#     print("\nWeight: ", sumw, "\nCost: ", sumc)
#
# while True:
#     print("Alkaga kansha tas kerek tandanyz: "
#           "\n1)Almaz 2)Rubin 3)Saphir 4)Izumrud 5)Gold")
#     a = int(input("Engizu: "))
#
#     if a == 1:
#         compute(a)
#         break
#     elif a == 2:
#         compute(a)
#         break
#     elif a == 3:
#         compute(a)
#         break
#     elif a == 4:
#         compute(a)
#         break
#     elif a == 5:
#         compute(a)
#         break

# while True:
#     1
# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
import  random


class Collection:
    def __init__(self,a):
        self.a=a
    def collect(self,list):
        listInt=[]
        listFloat=[]
        listStr=[]
        listF=['0','1','2','3','4','5','6','7','8','9']



        for i in range(len(list)):

            if ('0' in list[i] or '1'in list[i] or '2' in list[i] or '3'in list[i] or '4'in list[i] or '5'in list[i] or\
                    '6' in list[i] or '7'in list[i] or "8" in list[i] or "9" in list[i]) and "." in list[i]:
                list[i]=float(list[i])
                listFloat.append(list[i])
            elif '0' in list[i] or '1'in list[i] or '2' in list[i] or '3'in list[i] or '4'in list[i] or '5'in list[i] or\
                    '6' in list[i] or '7'in list[i] or "8" in list[i] or "9" in list[i]:
                list[i]=int(list[i])
                listInt.append(list[i])
            else:
                listStr.append(list[i])
        print(listInt)
        print(listFloat)
        print(listStr)
        a.main(listInt,listFloat,listStr,1)



    def count(self,nCount,listInt,listFloat,listStr):

        if nCount==1:
            print(listInt)
            nInt=int(input("Enter int n: "))
            count=0
            for i in range(len(listInt)):
                if nInt==listInt[i]:
                    count+=1
            print(nInt," element ",count," raz ")
        elif nCount==2:
            print(listFloat)
            nFloat=float(input(("Enter float n: ")))
            count=0
            for i in range(len(listFloat)):
                if nFloat==listFloat[i]:
                    count+=1
            print(nFloat, " element ", count, " raz ")
        elif nCount==3:
            print(listStr)
            nStr=input("Enter str n: ")
            count=0
            for i in range(len(listStr)):
                if nStr==listStr[i]:
                    count+=1
            print(nStr, " element ", count, " raz ")
        a.main(listInt,listFloat,listStr,1)


    def index(self,nCountf, listInt, listFloat, listStr):
        if nCountf==1:
            print(listInt)
            nIndex=int(input("Enter element: "))
            for i in range(len(listInt)):
                if nIndex==listInt[i]:
                    print(listInt[i]," element ", i, " index")
        elif nCountf==2:
            print(listFloat)
            nIndex = float(input("Enter element: "))
            for i in range(len(listFloat)):
                if nIndex == listFloat[i]:
                    print(listFloat[i], " element ", i, " index")
        elif nCountf==3:
            print(listStr)
            nIndex = input("Enter element: ")
            for i in range(len(listStr)):
                if nIndex == listStr[i]:
                    print(listStr[i], " element ", i, " index")
        a.main(listInt, listFloat, listStr, 1)

    def copy(self,nCounts, listInt, listFloat, listStr):
        if nCounts==1:
            print(listInt)
            random.shuffle(listInt)
            print(listInt)
        elif nCounts==2:
            print(listFloat)
            random.shuffle(listFloat)
            print(listFloat)
        elif nCounts==3:
            print(listStr)
            random.shuffle(listStr)
            print(listStr)
        a.main(listInt, listFloat, listStr, 1)

    def main(self,listInt,listFloat,listStr,coun):
        if coun==0:
            n=int(input("Enter size of collection: "))
            list=[]
            for i in range(n):
                nElement=input("Enter element: ")
                list.append(nElement)

            a.collect(list)
        else:
            print("1.count\t2.index\n3.copy")
            nChoice=int(input("Enter n: "))
            if nChoice==1:
                print("1.collection of int\n2.collection of float\n3.collection of str")
                nCount=int(input("Your choice"))
                if nCount==1:
                    a.count(nCount,listInt,listFloat,listStr)
                elif nCount==2:
                    a.count(nCount,listInt,listFloat,listStr)
                elif nCount==3:
                    a.count(nCount, listInt, listFloat, listStr)
            elif nChoice==2:
                print("1.collection of int\n2.collection of float\n3.collection of str")
                nCountf = int(input("Your choice"))
                if nCountf == 1:
                    a.index(nCountf, listInt, listFloat, listStr)
                elif nCountf == 2:
                    a.index(nCountf, listInt, listFloat, listStr)
                elif nCountf == 3:
                    a.index(nCountf, listInt, listFloat, listStr)





            elif nChoice==3:
                print("1.collection of int\n2.collection of float\n3.collection of str")
                nCounts = int(input("Your choice"))
                if nCounts == 1:
                    a.copy(nCounts, listInt, listFloat, listStr)
                elif nCounts == 2:
                    a.copy(nCounts, listInt, listFloat, listStr)
                elif nCounts == 3:
                    a.copy(nCounts, listInt, listFloat, listStr)

a=Collection(2)

a.main(0,0,0,0)
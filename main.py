import math
# list=[]
# for x in range(0,10):
#     list.append(x**2)
#     print(list)
# a2 = [x**2 for x in range(0,10)]
# print(a2)


# b=[]
# for x in range(0,6):
#     b.append(x**3)
#     print(b)
#
#
# c=[x++1 for x in range(0,20)]
# print(c)

# d=[]
# for y in list :
#     if y%2==1:
#         d.append(y)
#     print(d)

# c2 =[x for x in list if x%2==1]
# print(c2)

# lista =[]
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a,b))
# print(lista)
#
# lista2 =[(a,b) for a in [1,2,3] for b in[4,5,6]]
# print(lista2)

# slownik = {"PZU":"panstwowy zaklad ubezpieczen",
#            "ZUS":"zaklad ubezpieczen spolecznych",
#            "PKO":"Panstwowa kasa spoleczna"}
# slownik_odwrocony={}
# for key,value in slownik_odwrocony():
#     slownik_odwrocony[value]=key
# print(slownik_odwrocony)


# def row_kwadratowe(a,b,c):
#     delta = b**2 -4*a*c
#     if delta <0:
#         print("brak rozwiazan")
#         return -1
#     elif delta==0:
#         print("jedno rozwiazanie")
#         x = (-b)/(2*a)
#         return x
#     else:
#         print("dwa rozwiazania")
#         x1 = ((-b)-math.sqrt(delta))/(2*a)
#         x2 = ((-b)+math.sqrt(delta))/(2*a)
#         return x1,x2
#
# print(row_kwadratowe(6,1,3))
# print(row_kwadratowe(1,2,1))
# print(row_kwadratowe(1,4,1))

# def kkk (a):
#     if a%2==1:
#      print('nieparzysta')
#     else:
#      print('parzysta')
#
# kkk(12)


# def dlugosc_odcinka(x1=0,y1=0,x2=0,y2=0):
#     return math.sqrt((x2-x1)**2+(y2-x2)**2)
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(1,2,3,5))
# print(dlugosc_odcinka(2,2,x2=3,y2=5))
# print(dlugosc_odcinka(y1=1,x1=2,y2=3,x2=5))
# print(dlugosc_odcinka(y2=3,x2=5))

# def ciag(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         suma =0
#         for i in liczby:
#             suma += i
#             return suma
#
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8,9))


def co_lubie(** rzeczy):
    for cos in rzeczy:
     print("to jest")
     print(cos)
     print("to lubie")
     print(rzeczy[cos])

co_lubie(slodycze="czekolada",gry="lol, cs")

# # coding=utf-8
#
# """
#
#     Degiskenlerin 'type' larini belirtmeye gerek yok.
#
# """
#
#
# ali = 5
# veli = 10
#
#
# print ali*veli
# print ali/veli
#
# """
#
#     bolumlerde int - int bolmemeye dikkat
#     type casting
#
# """
#
# print type(ali)
#
# ali = float(ali) # 5.0
#
# print type(ali)
#
# ali = 5.0
#
# print type(ali),type(veli)
#
# print ali/veli
#
#
# ali = "furkan "
#
# """
#     Stringler
#     Char diye bir sey yok
#     String carpmasi
# """
#
# print ali
# print ali*veli
#
# print "egemen ","furkan "*2, "sezgin ", "berk ", "ogun"
#
# """ Boolean """
#
#
# veli = False
# ali = True
#
# print ali and veli, ali or veli
#
#
# # integer float string boolean
# print "eegemen" + "furkan"
#

""" Tuple ve list farki """


ali = [1,2,3,31,69]

print ali

ali.append(True)
ali.insert(2,"Ogun")

print ali
#del ali[2]

#ali[i] = "Furkan"

# print ali
# veli = (4,5,6)
#
#
#
# def f(x):
#     return x
#
# yeni_liste = f([1,2,3])
#
#
#
#
#
# print (5,10,"egemen")
#
#
#
#
#
#
# print yeni_liste[0],yeni_liste[1],yeni_liste[2]
#
# yeni_liste = list((1,2,3))
#
# print yeni_liste

#
# ali.append(5)
#
#
# #veli.append(7)
#
#
# """ Multiple type list ve tuplelar """
# ali.append("egemen")
#
# veli = ("Furkan", 5, 3.14, True, ali)
#
# #print veli
#
# ali[1] ="Furkan"
#
# #print veli

#
# o = [i for i in range(10)]
#
# print o[2:], o[:2], o[5:7],o[:],o
#
# copy = o
#
#
#
# deepcopy = o[:]
#
#
# print o[::-1]
#
#
# print o[-len(o)]
#
#
#
#
#
# print len(o)
#
#
#
# o[3] = False

# print copy,deepcopy




#
# """ yoklama listesi yapalim """
#
#
# workshop = [
#     ["Furkan Kilic",0],
#     ["Furkan Koltuk",0],
#     ["Berk Sahin",0],
#     ["Sezgin Baloglu",0],
#     ["Ogun Tarakci",0],
#     ["Egemen Sert",0]
# ]
#
#
# """ listeye birini ekleyek """
#
# print workshop[2]
#
# workshop[2][1] += 1
#
# print workshop[2]
# #
# print workshop
#

# """ dictionary """
#
#
# workshop = {
#     "Afsin Peker":0,
#     "Orhan Pamukoglu":0
# }
#
# workshop["Furkan Kilic"] = 0
# workshop["Furkan Koltuk"] = 0
# workshop["Berk Sahin"] = 0
# workshop["Sezgin Baloglu"] = 0
# workshop["Ogun Tarakci"] = 0
# workshop["Egemen Sert"] = 0
#
#
# print  workshop
#
# workshop["Ogun Tarakci"] += 1
#
# print workshop
#


#
# """ if elif else """
#
#
#
# mantiksalIfade = True
# mantiksalIfade_2 = True
#
#
#
#
#
# if True:
#
#     if mantiksalIfade_2:
#         print "Her ikisi de dogru amk"
#     else:
#         print "ilk ifade dogru"
#
# elif mantiksalIfade_2:
#     print  "ilk ifade yanlis, ikinci dogru"
#
# else:
#     print "iki ifade de yanlis"
#
#



""" for lup vayl lup """




#
# for i in range(10):
#     print i**2


# alidesidero = [5,3,8,0,69,0,6]
#
#
#
#
# for eleman in alidesidero:
#     i = alidesidero.index(eleman)
#     alidesidero[i] = 0
#
# print alidesidero

# print i yapabilir miyiz?

#
# i = 0
#
# while i<=90:
#     print "Patates" , i
#     i += 30
#
# print i




# def square(sayi):
#     return sayi**2
#
# print square(7)

#
# def factorial(x):
#     a = 1
#     while x>0:
#         a *= x
#         x-=1
#
#     return a
#
#


# def recursive_factorial(x):
#     if x>1:
#         return x * recursive_factorial(x-1)
#     return 1
#
# """
#
#     return 5 * 4 * 3 * 2 * 1
#
# """
#
# print recursive_factorial(5)


def euclidian_distance(v1,v2):
    if len(v1) != len(v2):
        return "Vektorlerin boyutlari ayni degil it"

    s = 0
    for i in range(len(v1)):
        s += (v1[i] - v2[i])**2
    return s ** 0.5

#
def ed_sum(v1,v2):
    return sum((x1-x2)**2 for x1,x2 in zip(v1,v2))**0.5

#
print euclidian_distance((0,4),(3,0))
print ed_sum((0,4),(3,0))

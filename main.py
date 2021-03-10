#zad1
# lista=['tenis','piłka nożna','siatkówka']
# print(lista)
# lista.reverse()
# lista.append('żużel')
# lista.append('szachy')
# print(lista)

#zad2
# slownik={'itd':'i tak dalej','itp':'i tym podobne','ww':'wyżej wymieniony'}
# print(slownik)

#zad3
# slownik={'Cp':'Cyberpunk2077','Con':'Control','WIII':'Wiedźmin3'}
# print(slownik)
# print(len(slownik))

#zad4
# napis=input('Podaj jakieś zdanie: ')
# print(napis)
# print(napis.count('a'))

#zad5
# import sys as system
# from math import *
# system.stdout.write('podaj liczbe a: ')
# a=system.stdin.readline()
# system.stdout.write('podaj liczbe b: ')
# b=system.stdin.readline()
# system.stdout.write('podaj liczbe c: ')
# c=system.stdin.readline()
# a=int(a)
# b=int(b)
# c=int(c)
# print(pow(a,b)+c)

#zad6
# a= input('podaj liczbę a: ')
# b= input('podaj liczbę b: ')
# c= input('podaj liczbę c: ')
# a=int(a)
# b=int(b)
# c=int(c)
# if a>b:
#     if a>c:
#         print('liczba a jest największa')
#     else:
#         print('liczba c jest największa')
# elif a<b:
#     if b>c:
#         print('liczba b jest największa')
#     else:
#         print('liczba c jest największa')
# else:
#     if a>c:
#         print('liczba a i b są największe')
#     elif a<c:
#         print('liczba c jest największa')
#     else:
#         print('liczby a,b i c są równe')

#zad7
# lista=[2,3,6,2.1,4.7,8.9]
# for x in lista:
#     x**=2
#     print(x)
# else:
#     print('Koniec pętli')

#zad8
# lista=[]
# licznik=0
# while licznik<10:
#     liczba = input('podaj liczbę: ')
#     liczba=int(liczba)
#     if (liczba%2)==0:
#         lista.append(liczba)
#     licznik+=1
# print(lista)

#zad9
# lista=[1,2,3,4,5]
# for x in lista:
#     if x%2==0:
#         print('E')
#     else:
#         print('EEEEEE')

#zad10
# liczba = input('Dodaj dodatnią liczbę: ')
# liczba=int(liczba)
# if liczba<0:
#     print('Podałeś ujemną liczbę!!!!')
# else:
#     print(pow(liczba,1/2))
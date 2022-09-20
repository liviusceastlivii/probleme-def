import math

a=int(input('Dati a='))
b=int(input('Dati b='))
def suma(x,y):
    s=a+b
    return s
print('Suma: ', suma(a,b))

def prod(a,b):
    p=a*b
    return p
print('Produsul= ', prod(a,b))

def media_aritm(x,y):
    mar=(x+y)/2
    return mar
print('Media aritmetica=', media_aritm(a,b))

def dm(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print('cel mai mare divizor comun= ', dm(a,b))
print('cel mai mic multiplu comun= ', a*b//dm(a,b))

def maxim(a,b):
    maxx=max(a,b)
    return maxx
def minim(a,b):
    minim=min(a,b)
    return minim
print('numarul minim=', minim(a,b))
print('numarul maxim=', maxim(a,b))

def suma():
    s=a+b
    return s
print('Suma: ', suma())

def produs():
    prod=a*b
    return prod
print('Produsul: ', produs())

def divizori(a,b):
    dv=[]
    for i in range(1, min(a,b)+1):
        if a%i==b%i==0:
            dv.append(i)
    return dv
print('Divizorii comuni:', divizori(a,b))

def multipli():
    dov=[]
    for i in range(1,6):
        dov.append(i*a*b)
    return dov
print('5 multipli: ', multipli())

def ambele(a,b):
    mol=''
    for i in range(0,10):
        if str(i) in str(a) and str(i) in str(b):
            mol+=str(i)+" "
    return mol
print('Cifre ce se contin in ambele numere:',ambele(a,b))    

def cifa(a,b):
    far=''
    for i in range(0,10):
        if str(i) in str(a) and str(i) not in str(b):
            far+=str(i)+" "
    return far
print('a fara b:',cifa(a,b))      

def prieteni(a,b):
    divx=0
    divy=0

    for i in range(1,a+1):
        if a%i==0 :
            divx+=2
    for i in range(1,b+1):
        if b%i==0 :
            divy+=2   
    if divx==divy:
        h="Prieteni"  
    else:
        h="NU sunt prieteni"  
    return h
print(prieteni(a,b)) 
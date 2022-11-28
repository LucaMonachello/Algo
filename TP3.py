import time
import random

def ex1a():
    x=0
    y=0
    n=int(input("Entrez votre valeur de N :"))
    for i in range (n):
        y=y+1
        x=x+y
    print(x)

def ex1b():
    x=float(input("Entrez une valeur x :"))
    while x !=100:
        return ex1b()
    print(x)

def ex1c():
    l=0
    j=0
    k=0
    for i in range(10):
        a=int(input('Donnez une valeur : '))
        while a >20 or a <0:
             a=int(input('Donnez une valeur : '))
        if a < 10:
            l+=1
        if a>=10 and a<15:
            j=j+1
        if a>=15:
            k+=1
    print(f'Il y a :\n{l} valeurs strictement inférieur à 10\n{j} valeurs supérieur ou égale à 10 et inférieur strictement à 15\n{k} valeurs supérieur ou égale à 15')

def ex1d():
    n=int(input("Entrez votre valeur de N :"))
    y=0
    x=0
    while x<n:
        y=y+1
        x=x+y
    if x !=n:
        print("Impossible")
    else:
        print(y)

def ex2a():
    n=int(input("Entrez une valeur pour n :"))
    time.sleep(0.4)
    print(n)
    while n !=0:
        n=n-1
        time.sleep(0.4)
        print(n)

def ex2b():
    n=int(input("Entrez une valeur pour n :"))
    time.sleep(0.4)
    print(n)
    for i in range (n):
        n=n-1
        time.sleep(0.4)
        print(n)
        
def ex3():
    tr=0
    for i in range(1):
        x=random.randint(0,100)
        print(x)
    a=0
    while a !=x:
        tr+=1
        a=int(input("Devinez la valeur de x : "))
        if a == x:
            print('Trouvé !')
            print("Nombre de tours avant d'avoir trouvé : ",tr)
        elif a < x:
            print('Trop petit')
        else:
            print('Trop Grand')
            
def ex4():
    a=int(input("Choix 1 ou 2 : "))
    b=int(input("Choisissez votre entier pour la factorielle : "))
    x=1
    if a==1:
        for i in range(b):
            x=x*b
            b-=1
            print(x)
    if a==2:
        while b !=0:
            x=x*b
            b=b-1
            print(x)

def ex5():
    a=int(input("Donnez l'heure de début de la location (un entier) : "))
    b=int(input("Donnez l'heure de fin de la location (un entier) : "))
    heure=b-a
    prix1=0
    if a>24 or a<0 or b>24 or b<0:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return ex5()
    elif a==b:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
        return ex5()
    elif a>b:
        print("Attention ! le début de la location est après la fin ...\n")
        return ex5()
    if a>=0 and a<7 and b<=7:
        cout=1
        prix1=heure*cout
        print(f"Vous avez loué votre vélo pendant\n{heure} heure(s) au tarif horaire de 1.0 euro(s)\nLe montant total à payer est de {prix1} euro(s).")
    elif a>=7 and a<17 and b<=17:
        cout=2
        prix1=heure*cout
        print(f"Vous avez loué votre vélo pendant\n{heure} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {prix1} euro(s).")
    elif a>=17 and a<24 and b<=24:
        cout=1
        prix1=heure*cout
        print(f"Vous avez loué votre vélo pendant\n{heure} heure(s) au tarif horaire de 1.0 euro(s)\nLe montant total à payer est de {prix1} euro(s).")
    elif a>=0 and a<7 and b>=7 and b<=17:
        x=7-a
        c1=x*1
        y=b-7
        c2=y*2
        prix1=c1+c2
        print(f"Vous avez loué votre vélo pendant\n{x} heure(s) au tarif horaire de 1.0 euro(s)\n{y} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {prix1} euro(s).")
    elif a>=7 and a<17 and b>=17 and b<=24:
        x=17-a
        c1=x*2
        y=b-17
        c2=y*1
        prix1=c1+c2
        print(f"Vous avez loué votre vélo pendant\n{y} heure(s) au tarif horaire de 1.0 euro(s)\n{x} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {prix1} euro(s).")
    elif a>=0 and a<7 and b>=17 and b<=24:
        x=7-a
        c1=x*1
        y=b-17
        c2=y*1
        prix1=c1+c2+20
        print(f"Vous avez loué votre vélo pendant\n{x+y} heure(s) au tarif horaire de 1.0 euro(s)\n10 heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {prix1} euro(s).")

 
#ex1a()
#ex1b()
#ex1c()
#ex1d()
#ex2a()
#ex2b()
#ex3()
#ex4()
#ex5()
import random

def ex1():
    x = int(input("Entrez une valeur pour x :"))
    y = int(input("Entrez une valeur pour y :"))
    print(f"Avant permutation:\nx : {x}\ny : {y}")
    z = x
    x = y
    y = z
    print(f"Après permutation:\nx : {x}\ny : {y}")
   

def ex2():
    age = int(input("Donnez votre âge :\n"))
    annee = 2022-age
    print("Votre annee de naissance est donc :",annee)

def ex3():
    a = int(input("Entrez une premiere valeur a :"))
    b = int(input("Entrez une deuxieme valeur b :"))
    c = int(input("Entrez une troisieme valeur c :"))
    print(f"Les valeurs entrees sont : a = {a}, b = {b} et c = {c}")
    print("Permutation: a ==> b, b ==> c, c==> a")
    a,b,c=c,a,b
    print(f"Les valeurs permutees sont : a = {a}, b = {b} et c = {c}")

def ex4():
    base=4
    fromage=800
    eau=2
    ail=2
    pain=400
    nbpersonne=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
    fromage1=fromage*nbpersonne/base
    eau1=eau*nbpersonne/base
    ail1=ail*nbpersonne/base
    pain1=pain*nbpersonne/base
    print(f"Pour faire une fondue fribourgeoise pour {nbpersonne} personnes, il vous faut :\n- {fromage1}gr de fromage\n- {eau1}dl d'eau\n- {ail1}gousse(s) d'ail\n- {pain1}gr de pain")

def ex5():
    a=int(input('Entrez un chiffre : '))
    if a == 0:
        print('le chiffre vaut 0')
    elif a > 0:
        if a%2 != 0:
            print('le chiffre est positif et impaire')
        else:
            print('le chiffre est positif et paire')
    else:
        if a%2 != 0:
            print('le chiffre est négatif et impaire')
        else:
            print('le chiffre est négatif et paire')


def ex6():
    a= random.randint(1,100)
    if a < 50:
        print ('pile !')
    else:
        print('face ! ')

def ex7():
    a= random.randint(1,99)
    if a < 66:
        print ('pile !')
    else:
        print('face ! ')


def ex8():
    x=float(input("Entrez un nombre décimal : "))
    if  not x <2.0 and x<3.0:
        print("x appartient à I")
    elif not x <0.0 and not x==0.0 and x<1.0:
        print("x appartient à I")
    elif not x <-10.0 and x<-2.0 or x==-2:
        print("x appartient à I")
    else:
        print("x n'appartient pas à I")

    

    
#ex1()
#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
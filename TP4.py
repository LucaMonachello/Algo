import random

def ex1():
    a=float(input("Vous cherchez la table de multiplication de quel nombre ? : "))
    L=[]
    for i in range(0,11):
        x=a*i
        x=round(x,1)
        L.append(x)
        print(f'{a} * {i} = ',L[i])
        
def ex2():
    # Demande le nombre d'étudiants à l'utilisateur
    a = int(input("Donnez le nombre d'etudiants : "))
    moyenne = 0.0;
    notes = []
    for i in range(a):
        x=float(input(f"Note etudiant {i}: "))
        notes.append(x)
    if x>20 or x<0:
        print("Le note ne vont que de 0 à 20 !")
        return ex2()
    else:
        for i  in range(a):
            moyenne+=notes[i]/a
        print(f"\nMoyenne de classe : {moyenne}\n")
        print("Numéro de l'Etudiant | note | ecart a la moyenne")
        for i in range(a):
            ecart=notes[i]-moyenne
            print(f"{i} | {notes[i]} | {ecart}")

def ex3():
    nMax=3
    c=0
    v1=[]
    v2=[]
    n=int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? : "))
    if n>nMax or n<1:
        return ex3()
    else :
        print("\nSaisie du premier vecteur :")
        for i in range(n):
            a=int(input(f"v1[{i}] = "))
            v1.append(a)
        print("\nSaisie du seconde vecteur :")
        for j in range(n):
            b=int(input(f"v2[{j}] = "))
            v2.append(b)
        for k in range(n):
            c=c+(v1[k]*v2[k])
        print(f"Le produit scalaire de v1 par v2 vaut {c}")
    
def ex4a():
    x=1
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
    for i in range(L1):
        for j in range(L1):
            if i==j:
                x+=1
        print(j)
    
    
     
def ex6():
    L1 = [5, 2, 4, 8, 1, 3]
    for i in range(len(L1)-1):
        for j in range(len(L1)-1):
            if L1[j] > L1[j+1]:
                temp=L1[j]
                L1[j]=L1[j+1]
                L1[j+1]=temp
    print(L1)

#ex1()
#ex2()
#ex3()
ex4a()
#ex4b()
#ex5()
#ex6()
#ex7()
#ex8()
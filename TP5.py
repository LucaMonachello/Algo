def ex1():
    a=input("Entrez votre premier prénom : ")
    b=input("Entrez votre premier nom : ")
    c=input("Entrez votre deuxième prénom : ")
    d=input("Entrez votre deuxième nom : ")
    a=str.capitalize(a)
    b=str.upper(b)
    c=str.capitalize(c)
    d=str.upper(d)
    print(a,c)
    print(b,d)

def ex2():
    a=0
    b=0
    for i in range(5):
        S1=input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
        S2=S1.split()
        S3=int(S2[0])
        if S3>20:
            print("Une note entre 0 et 20!")
            return ex2()
        else:
            S4=float(S2[1])
        if S3<8:
              print("l'étudiant n'est pas admis")
              return ex2()
        else:
            S5=a+(S3*S4)
            S6=b+(S4)
    S7=S5/S6
    if S7>10:
        print(f"La moyenne générale est de {S7}, l'étudiant est admis")
    else:
        print(f"La moyenne générale est de {S7}, l'étudiant n'est donc pas admis")

def ex3():
    a=input("Entrez un mot ou une phrase : ")
    

      
        
        
    


#ex1()
#ex2()
ex3()
def ex1():
    nom='Jeanne'
    prenom='Marie'
    math=15
    anglais=10
    info=14
    promotion=2022
    moy=(math+anglais+info)/3
    print("L'étudiant" ,nom, prenom ,"de la promotion" ,promotion, "a une moyenne de " ,moy)
    
def ex2():
    jour=int(input('Jour du mois :'))
    heure=int(input('heure :'))
    minute=int(input('minute :'))
    while heure>24:
        jour=jour+1
        heure=heure-24
    while minute>60:
        heure=heure+1
        minute=minute-60
    if jour>31:
        return False
    te=(24*60*jour)+60*heure+minute
    print(te, "minutes")

#ex1()
#ex2()
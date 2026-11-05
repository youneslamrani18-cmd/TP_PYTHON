import math

a=float(input("Saisir a="))
b=float(input("Saisir b="))
c=float(input("Saisir c="))

if a==0 :
    if b==0:
        if c==0 :
            print("R")
        else: 
            print("l'équation n'a pas de solution")
    else :
        x=-c/b
        print(f"la solution de l'équation est:{x} ")
else:
    D=b**2-4*a*c
    print(f"Delta ={D}")
    if D>0: 
        x1=(-b-math.sqrt(D))/(2*a)
        x2=(-b+math.sqrt(D))/(2*a)
        print(f"il y a deux solutions distincts x1={x1} et x2={x2}")
    elif D==0 :
        x0=-b/(2*a)
        print(f"il y a une seule solution : x0={x0}")
    else :
        print("Pas de solution réelle (car D est négatif)")
        
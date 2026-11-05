nom1=input("Entrer le nom de la première personne:")
age1=int(input(" Entrer l'age de la première personne:"))
nom2=input("Entrer le nom de la deuxième personne:")
age2=int(input(" Entrer l'age de la deuxième personne:"))
nom3=input("Entrer le nom de la troisème personne:")
age3=int(input(" Entrer l'age de la troisième personne:"))

if  age1>=age2 and age1>=age3 :
    print(f"la personne la plus agée est :{nom1}")
elif age2>=age1 and age2>=age3 :
    print(f"la personne la plus agée est :{nom2}")
else :
    print(f"la personne la plus agée est :{nom3}")
    
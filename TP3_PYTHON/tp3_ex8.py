ch=input("Saisir une chaine :")
c=input("Saisir un caractère :")
i=0
for  n in ch :
    if n==c:
        i=i+1
print(f"le nombre d'occurrences de {c} dans la chaine est :{i}") 

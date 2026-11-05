chaine=input("Entrez une chaine de caractères :")
resultat=" "
for char in chaine :
    if char not in resultat :
        resultat+= char
print(f"Les caractères uniques : {resultat}")

n1=int(input("Saisir le 1er nombre entier:"))
n2=int(input("Saisir le 2ème nombre entier:"))

if n1<=n2 :
    n1=n2
n2=int(input("Saisir le 3ème nombre entier:"))
if n1<=n2 :
    n1=n2 
n2=int(input("Saisir le 4ème nombre entier:"))
if n1<=n2 :
    n1=n2
print(f"le plus grand nombre est:{n1}")

N=int(input("Entrer un nombre entier naturel N="))
S=0
if N>0 :
    for i in range(1,N):
        S=S+(1/i)
    print(f"la somme des N premier termes S={S}")
    
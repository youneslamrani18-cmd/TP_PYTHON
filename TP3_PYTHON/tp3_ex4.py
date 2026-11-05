n=int(input("Saisir un entier positif :"))
S=0
for i in range(1,n) :
    if n%i==0 :
        S=S+i
if S==n and n>0 :
    print("nombre parfait")
else :
    print("nombre non parfait")
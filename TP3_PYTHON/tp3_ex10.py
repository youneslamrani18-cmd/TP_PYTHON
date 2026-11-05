n=int(input("Saisir un entier positif :"))
M=1
S=0
for c in range(n) :
    for i in range(2,n):
        M=M*i
    S=S+M
print("S=",S)
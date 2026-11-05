N=int(input(" Sasir un entier N= "))
print(f"les nombres premiers entre 2 et {N} sont :")
for i in range (2,N+1) :
    est_premier = True
    for j in range(2,i) :
        if i%j==0 :
            est_premier = False 
            break
    if est_premier :
        print(i,end=" ")
        
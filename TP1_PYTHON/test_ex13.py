Q= int(input("Entrer la quantité achetée :"))
PU= float(input(" Entrer le prix unitaire :"))
P=Q*PU 
print(f"le prix totale est: {P}")
R= P*0.15
print(f"le montant de la réduction est: {R}")
print(f"le prix finale à payer est: {P-R}")

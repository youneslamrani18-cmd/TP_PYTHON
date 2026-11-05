ch=input("Saisir une chaine de caractère :")
st=""
for i in ch :
    st=i+st
print(st)
if st==ch :
    print("Palindrome")
else :
    print("n'est pas une Palindrome")

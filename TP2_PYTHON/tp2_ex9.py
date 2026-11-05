caractère=input("Veuillez saisir un caractère :")

if len(caractère)>0 :
    c=caractère[0]

    if 'A' <= c <= 'Z':
        print("lettre majuscule")
    elif 'a' <= c <='z':
        print("lettre minuscule")
    else: 
        print("Autre caractère")
else:
    print("vous n'avez rien saisi")
    
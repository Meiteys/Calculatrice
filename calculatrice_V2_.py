print("Bienvenue dans ma calculatrice 2.0")
A = input('Saisir le premier nombre ')

# Convertissons la saisie ( de l'utilisateur) A en entier
A_converted = int(A)
B = input('Saisir le second nombre ')
# Convertissons la saisie ( de l'utilisateur) B en entier
B_converted = int(B)

op = input("saisir l'opération souhaitée: -; +; x ou / ")

if op == "-":
    C = A_converted-B_converted
    print(C)
elif op == "+":
    C = A_converted+B_converted
    print(C)
elif op == "x":
    C = A_converted*B_converted
    print(C)
elif op == "/":
    C = A_converted/B_converted
    print(C)
else :
    print("operation invalide, veuiller saisir -; +; x ou / ")
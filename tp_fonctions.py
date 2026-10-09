notes = [12, 8, 15, 10, 17]

# 1 - Fonction qui affiche la liste
def afficher_notes(liste):
    print("Les notes sont :", liste)

# 2 - Fonction qui calcule la somme des éléments
def calculer_total(liste):
    total = 0
    for element in liste:
        total = total + element
    return total

# Utilisation des fonctions
afficher_notes(notes)

resultat = calculer_total(notes)
print("Le total des notes est :", resultat)
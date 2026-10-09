# etudiant1 = "Ibrahim"
# etudiant2 = "Mariam"
# etudiant3 = "Cheick"
# etudiant4 = "Nour"
# etudiant5 = "Malick"

# print (etudiant1)
 
# Création d'une liste d'etudiants
etudiants = ["Ibrahim", "Mariam", "Cheick", "Nour", "Malick"]
print(etudiants)

# print(le premier elt de la liste qui va corresponde à Ibrahim, qui a l'indexe 0)
print(etudiants[0])
print(etudiants[1])
print(etudiants[2])
print(etudiants[3])
print(etudiants[4])
print(etudiants[-1])

etudiants.append("Sakina")
print(etudiants)

etudiants.remove("Cheick")
print(etudiants)

print(len(etudiants))

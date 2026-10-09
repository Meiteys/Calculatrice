# Création d'une liste d'etudiants
etudiants = ["Ibrahim", "Mariam", "Cheick", "Nour", "Malick"]
# print(etudiants)

# # print(le premier elt de la liste qui va corresponde à Ibrahim, qui a l'indexe 0)
# print(etudiants[0])
# print(etudiants[1])
# print(etudiants[2])
# print(etudiants[3])
# print(etudiants[4])
# print(etudiants[-1])

for etudiant in etudiants:
    print( "boujour", etudiant)

# Création d'une liste de note
notes = [12, 15, 8, 17, 14]
print(notes)

total = 0
for note in notes:
    total = total+note
print (total)

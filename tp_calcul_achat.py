print("Bienvenue dans le calcul des achats")

# Demander le nom du client
nom_client = input("Saisir le nom du client : ")

# Demander le prix de l'article
prix = input("Saisir le prix de l'article : ")

# Convertissons le prix saisi en entier
# prix_converted = int(prix)

prix_converted = float(prix)

# Demander la quantité achetée
quantite = input("Saisir la quantité achetée : ")

# Convertissons la quantité saisie en entier
quantite_converted = int(quantite)

# Calculer le prix total
total = prix_converted * quantite_converted

# Vérifier si le client bénéficie de la remise
if total >= 100:
    montant_final = total - 10
else:
    montant_final = total

# Afficher le montant final
print(nom_client)
print(montant_final)
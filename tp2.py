# #Vérification de la majorité
age = int(input("Entrez votre age :"))

if age >= 18:
    print("vous tes majeur")
else:
    print("vous tes mineur")

#Réduction pour étudiants

reponse = input("Êtes-vous étudiant ? (oui/non) :")

if reponse.lower() == "oui":
    print("Vous avez droit à une réduction de 10%")
else:
    print("Vous n'avez pas droit à la réduction")

# #Prix d’un billet de cinéma

age = int(input("Entrez votre age :"))

if age < 12:
    print("le prix de vorte billet est 7") 
else:
    print("le prix de vortre billet est 10")

#Éligibilité à un prêt bancaire

salaire = float(input("Entrez votre salaire mensuel: "))
age = int(input("Entrez votre age: "))

if salaire > 1500 and age > 25:
    print("Vous êtes éligible à un prêt")
else:
    print("Vous n'êtes pas éligible à un prêt")

#Bonus de note

note = float(input("Entrez votre note sur 20 :"))

if note > 15:
    note = note + 1
elif note < 10:
    note = note - 0.5
else:
    note = note

print("Votre note finale est :", note)  
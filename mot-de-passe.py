import hashlib
import random
import string

caracteres_speciaux = "!@#$%^&*()-+"

def generer_sel(taille=16):
    #Génère une chaîne de caractères aléatoire pour le sel.
    caracteres = string.ascii_letters + string.digits + caracteres_speciaux
    return ''.join(random.choice(caracteres) for _ in range(taille))

def mot_de_passe():
    print("Le mot de passe doit:")
    print("- Avoir au moins 8 caractères")
    print("- Avoir au moins une lettre majuscule")
    print("- Avoir au moins une lettre minuscule")
    print("- Avoir au moins un chiffre")
    print("- Avoir au moins un caractère spécial parmi : !@#$%^&*()-+ ")

    while True:
        mdp = input("Choisissez votre mot de passe: ")
# char = charactere
        if len(mdp) < 8:
            print("Mot de passe trop court, réessayez.")
        elif not any(char.isupper() for char in mdp): # si aucune des charactére n'est pas en Majuscule dans la variable mdp
            print("Votre mot de passe ne contient pas au moins 1 majuscule.")
        elif not any(char.islower() for char in mdp): 
            print("Votre mot de passe ne contient pas au moins 1 minuscule.")
        elif not any(char.isdigit() for char in mdp):
            print("Votre mot de passe doit contenir au moins 1 chiffre.")
        elif not any(char in caracteres_speciaux for char in mdp):
            print("Votre mot de passe doit contenir au moins 1 caractère spécial parmi : !@#$%^&*()-+ ")
        else:
           #le "sel" est une chaîne aléatoire unique qui est utilisée pour renforcer la sécurité lors de la création de hachages de mots de passe =)
           
            sel = generer_sel() # Générer le sel

            # Ajouter le sel au mot de passe
            mdp_avec_sel = mdp + sel

            # Hacher le mot de passe avec le sel
            hasher = hashlib.sha256()
            hasher.update(mdp_avec_sel.encode('utf-8'))
            hashed_password = hasher.hexdigest()

            print("Mot de passe haché (SHA-256) avec sel:", hashed_password)
            print("Sel utilisé:", sel)

            return mdp

mot_de_passe()

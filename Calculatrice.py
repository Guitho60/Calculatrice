#Definition des constantes&variables
contact = "contact-calculatricePython@gmail.com"
icontinue = True

while icontinue:
    msgerror = False

    #Saisie de l'opération par l'utilisateur
    chaine = input("Veuillez saisir une opération de la forme a + b : ")
    print(chaine)

    chaine = chaine.split(" ")
    print(chaine)

    nombre1 = chaine[0]
    operation = chaine[1]
    nombre2 = chaine[2]

    if operation == "+":
        resultat = float(nombre1) + float(nombre2)
    elif operation == "-":
        resultat = float(nombre1) - float(nombre2)
    elif operation == "*":
        resultat = float(nombre1) * float(nombre2)
    elif operation == "/":
        resultat = float(nombre1) / float(nombre2)
    elif operation == "modulo":
        resultat = float(nombre1) % float(nombre2)
    elif operation == "//":
        resultat = float(nombre1) // float(nombre2)
    else:
        msgerror = True

    if not msgerror :
        print(f"Résultat = {resultat}")
    else:
        print("Erreur la chaine saisie ne correspond pas à une opération.")

    print(f"Merci d'avoir utilisé notre calculatrice !! Adresse de contact : {contact}")
    #icontinue = input("Souhaitez-vous réaliser une autre opération ? 1 = Oui sinon Non : ")
    icontinue = True if input("Souhaitez-vous réaliser une autre opération ? (1 = Oui) : ") == "1" else False
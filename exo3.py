def rechercher_note(dictionnaire_eleves, nom_recherche):
    if nom_recherche in dictionnaire_eleves:
        return dictionnaire_eleves[nom_recherche]
    else:
        return "erreur : eleve non trouve."


eleves = {"Ali": 14, "Fatou": 16, "Moussa": 12}

print(rechercher_note(eleves, "Fatou"))  
print(rechercher_note(eleves, "Jean"))   

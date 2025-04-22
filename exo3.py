def eleve():
    prenom = input("Entrez le prénom de l'élève : ")
    note = input("Entrez la note de l'élève : ")
    return (prenom, note)

def dictionnaire(eleve):
    prenom, note = eleve  
    if dictionnaire==prenom :
        return {
            "note": note
        }
    else:
        return "Erreur eleve non trouve"
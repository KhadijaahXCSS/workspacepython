#Gestion des étudiants
# Gestion des étudiants
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = []

    def ajouter_note(self, note):
        if note >0 and note <20:
            self.note.append(note)
            print(f"Note de {note} ajoutee pour l'etudiant {self.nom}.")
        else:
            print ("la note doit etre comprise entre 0 et 20")
    def calculer_moyenne(self):
        if len(self.note) == 0:
            return 0
        else:
            return sum(self.note) / len(self.note)
    def afficher_informations(self):
        print(f"Nom: {self.nom}, Age: {self.age}, Moyenne: {self.calculer_moyenne()}")  
    

etudiant1 = Etudiant("Fatou", 20)
etudiant1.ajouter_note(14)  
etudiant1.ajouter_note(26)
etudiant1.afficher_informations()
etudiant2 = Etudiant("Amina", 22, [12, 14])
etudiant2.ajouter_note(16)
etudiant2.ajouter_note(19)
etudiant2.afficher_informations()
etudiant3 = Etudiant("Moussa", 21, [10, 11])
etudiant3.ajouter_note(8)
etudiant3.ajouter_note(25)
etudiant3.afficher_informations()      
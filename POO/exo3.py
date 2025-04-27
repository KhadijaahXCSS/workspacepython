#Gestion d'une bibliothèque
class Livre:
    def __init__(self, auteur, titre, disponible):
        self.auteur = auteur
        self.titre = titre
        self.disponible = disponible
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre '{self.titre}' a ete emprunte")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible.")
    def rendre(self):
        self.disponible = True
        print(f"Le livre '{self.titre}' a ete rendu.")
    def afficher_details(self):
        print(f"Auteur: {self.auteur}, Titre: {self.titre}, Disponible: {'Oui' if self.disponible else 'Non'}")

livre1 = Livre("John Doe", "Python pour les nuls", True)
livre2 = Livre("Sun Tzu", "L'Art de la Guerre", True)

livre1.afficher_details()  
livre1.emprunter()  
livre1.emprunter()  
livre1.rendre()  
livre1.afficher_details()  
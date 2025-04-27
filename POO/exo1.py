#Gestion des comptes bancaires

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self,montant):
        self.solde += montant
        print(f"DEpot de {montant} FCFA effectue. Nouveau solde: {self.solde} FCFA")
    def retirer(self,montant):
        if montant > self.solde:
            print("solde insuffisant")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} FCFA effectue. Nouveau solde: {self.solde} FCFA")
    def afficher_solde(self):
        print(f"Le solde de {self.titulaire} est de {self.solde} FCFA")

compte=CompteBancaire("ali",100)
compte.deposer(50)  
compte.retirer(30)  
compte.afficher_solde()  
compte.retirer(200)  

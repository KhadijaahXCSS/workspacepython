#application gestion de taches 

from tinydb import TinyDB, Query
class todo:
    def __init__(self, db_file="db.json"):
        self.db = TinyDB(db_file)
        self.task_table = self.db.table("tasks")
        self.task = Query()
    
    def ajouter_tache(self, description):
        nouvelle_tache = {
            "description": description,
            "complete": False
        }
        self.task_table.insert(nouvelle_tache)
        print(f"Tache ajoutee : {description}")
    def afficher_taches(self):
        taches = self.task_table.all()
        if not taches:
            print("Aucune tache trouvee.")
        else:
            for tache in taches:
                statut = "Complete" if tache["complete"] else "Non complete"
                print(f"{tache.doc_id}: {tache['description']} - {statut}")
    def marquer_tache_complete(self, tache_id):
        tache= self.task_table.get(self.task.doc_id == tache_id)
        if  tache:
            self.task_table.update({"complete": True}, doc_ids=[tache_id])
            print(f"Tache {tache_id} marquee comme complete.")
        else:
            print(f"Tache {tache_id} non trouvee.")

    def supprimer_tache(self, tache_id):
        tache = self.task_table.get(self.task.doc_id == tache_id)
        if tache:
            self.task_table.delete(self.task.doc_id == tache_id)
            print(f"Tache  {tache_id} supprimee.")
            self.afficher_taches.update()
        else:
            print(f"Tache {tache_id} non trouvee.")
    

    
    
    

     




def main():
    todo_app = todo()
    print("Bienvenue dans l'application de gestion de taches")
    while True:
        print("1. Ajouter une tache")
        print("2. Afficher les taches")
        print("3. Supprimer une tache")
        print("4. Marquer une tache comme complete")
        print("5. Quitter")
        
        choix = input("Choisissez une option : ")
        if choix == "1":
            description = input("Entrez la description de la tache : ")
            todo_app.ajouter_tache(description)
        elif choix == "2":
            print("Liste des taches :")
            todo_app.afficher_taches()
        elif choix == "3":
            todo_app.afficher_taches()
            tache_id = int(input("Entrez l'ID de la tache a supprimer : "))
            todo_app.supprimer_tache(tache_id)
        elif choix == "4":
            todo_app.afficher_taches()
            tache_id = int(input("Entrez l'ID de la tache a marquer comme complete : "))
            todo_app.marquer_tache_complete(tache_id)   

    
        elif choix == "5":
            print("Au revoir!")
            break   
        else:
            print("Choix invalide") 

if __name__ == "__main__":
    main()
            
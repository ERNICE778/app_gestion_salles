from data.dao_salle import DataSalle 
from models.salle import Salle 

class ServiceSalle :
    def __init__(self):
        self.dao_salle =DataSalle()

    def ajouter_salle(self , salle):
        if not salle.code  or  not salle.description or not salle.categorie or not salle.capacite :
            print("Attention: toutes les donnees doivent etre presentes")
            return False
        if  int (salle.capacite) >= 1:
            self.dao_salle.insert_salle(salle)
            print(f"La salle {salle.code}  a ete ajoutee avec success")
            return True 
        else:
            return False , "la capacite doit etre au moins de 1"
        
    def modifier_salle(self,salle):
        if not salle.code  or  not salle.description or not salle.categorie or not salle.capacite :
            print("Attention: toutes les donnees doivent etre presentes")
            return False
        if int(salle.capacite) >= 1:
            self.dao_salle.update_salle(salle)
            print(f"la salle {salle.code} a ete modifie avec success")
            return True
        else:
            return "Erreur"


    def supprimer_salle(self,code):
        self.dao_salle.delete_salle(code)
        print(f"La salle {code} a ete supprimee avec succes")
        

    def rechercher_salle(self,code):
        return self.dao_salle.get_salle(code)
    
    def recuperer_salles(self):
        return self.dao_salle.get_salles()
            
    
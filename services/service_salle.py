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
            print("condition de la capacite verifiee")
            self.dao_salle.insert_salle(salle)
            return True
        else:
            print("la capacite doit etre au moins de 1")
            return False
        
    def modifier_salle(self,salle):
        if not salle.code  or  not salle.description or not salle.categorie or not salle.capacite :
            print("Attention: toutes les donnees doivent etre presentes")
            return False
        if int(salle.capacite) <1:
            self.dao_salle.update_salle(salle)
            return True
        else:
            return "Erreur"


    def supprimer_salle(self,code):
        self.dao_salle.delete_salle(code)
        

    def rechercher_salle(self,code):
        self.dao_salle.get_salle(code)
        return True , "la salle {code} a ete retrouvee avec success. "
            
    
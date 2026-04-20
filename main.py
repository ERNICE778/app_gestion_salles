from data.dao_salle import DataSalle 
from models.salle import Salle 
from services.service_salle import ServiceSalle



''' data=DataSalle()
try :
    conn =data.get_connection()
    print("Connexion reussi avec succes ")
    conn.close()

except Exception as e:
    print("erreur de connexion: ", e)  

print("\n")
# j' ai mis certaines lignes de commandes en commentaire pour eviter de creer des salles ayant le meme code 
s1=Salle("R207I","Salle de reseautique","laboratoire",36)
s2=Salle("A208S","Salle d'administration systeme ","laboratoire",36)
s3=Salle("P209I","Salle de programmation ","salle de classe ",50)
s4=Salle("B210I","BIBLIOTHEQUE ","salle  ",200)

try:
    data.insert_salle(s1)
    print (f"La Salle ayant le code  {s1.code}  a ete ajoutee avec success ")
    
    data.insert_salle(s2)
    print (f"La Salle ayant le code   {s2.code}  a ete ajoutee avec success ")
    
    data.insert_salle(s3)
    print (f"La Salle ayant le code  {s3.code}  a ete ajoutee avec success ")
    
    data.insert_salle(s4)
    print (f"La Salle ayant le code  {s4.code}  a ete ajoutee avec success ")
except Exception as e:
    print("erreur d'insertion: ", e)    



print("\n")
s2_mod=Salle("A208S","Salle de bureautique","laboratoire",70)
data.update_salle(s2_mod)
print(f"salle {s2_mod.code} modifiee avec success")

print("\n")
data.delete_salle("R207I")
print(f"la salle R207I a ete supprimee avec success")

print("\n")
recherche =data.get_salle("B210I")
if recherche:
    print("la salle B210I a ete trouve ")
    print(f"ses informations sont:" )
    recherche.afficher_infos()
else:
    print("la salle B210I n' exixte pas")  



print("\n Liste des salles")     
salles = data.get_salles()
for salle in salles:
    salle.afficher_infos() '''
'''
service=ServiceSalle()

print("\n 1. Liste des salles")
salles=service.recuperer_salles()
if salles:
    for s in salles:
        s.afficher_infos()
else:
    print("Aucune salle disponible dans la base de donnees")        


s5 =Salle("B211I","Salle de francais","classe ",100)
s7 =Salle("S232A","Salle de gymnastique","sport",105)
s7=Salle("S233A","Salle de gymnastique 2","sport",200)
print ("\n2.Ajout d une salle")
service.ajouter_salle(s7)

print("\n")
print("\n 2. Modification de la capacite de la (172--->110) salle de gymnastique ayant le code S232A ")
salle= service.rechercher_salle("S232A")
if salle:
    salle.description= "Salle de gymnastique"
    salle.categorie="sport"
    salle.capacite=110
    service.modifier_salle(salle)

else:
    print("la salle ayant le code S232A n'existe pas")



print("\n 3. Suppresion de la salle ayant le code S212A")
service.supprimer_salle("B211I")



print("\n 4. Recherche de la salle S232A")
recherche=service.rechercher_salle("S232A")
if recherche:
    print (f"la salle S232A a ete retrouvee avec success. ")
else:
    print("Cette salle n'existe pas ") '''



from views.view_salle import ViewSalle 
app=ViewSalle()
app.mainloop() 
# Validation et publication

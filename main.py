from data.dao_salle import DataSalle 
from models.salle import Salle 


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














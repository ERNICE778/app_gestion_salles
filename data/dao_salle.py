import mysql.connector
import json 
from models.salle import Salle



class Datasalle :
    def get_connection(self):
        with open("data/config.json" , "r") as f :
            config=json.loaf(f) 
        return mysql.connector.connect(mysql.connector.connect(
                                            host="localhost",
                                            user="user_python",
                                            password="Python2026",
                                            database="db_salles"
                                        ))    



def insert_salle(self,salle):
    conn=self.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO salle VALUES (%s,%s,%s,%s)",
        (salle.code,salle.description,salle.categorie,salle.capacite)
    )
    conn.commit()
    conn.close()


    



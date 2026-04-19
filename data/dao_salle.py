import mysql.connector
import json 
from models.salle import Salle



class DataSalle :
    def get_connection(self):
        with open("data/config.json" , "r") as f :
            config=json.load(f) 
        return mysql.connector.connect(
                                            host="localhost",
                                            user="user_python",
                                            password="Python2026",
                                            database="db_salles"
                                        )   



    def insert_salle(self,salle):
        conn=self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO salle VALUES (%s,%s,%s,%s)",
        (salle.code,salle.description,salle.categorie,salle.capacite)
        )
        conn.commit()
        conn.close()

 

    def update_salle(self, salle ):
        conn= self.get_connection()
        cursor=conn.cursor ()
        cursor.execute(
         "UPDATE  salle SET description= %s,categorie=%s,capacite=%s WHERE  code=%s "  ,
        (salle.description,salle.categorie,salle.capacite, salle.code)
        )
        conn.commit()
        conn.close()

    def delete_salle(self,code):
        conn=self.get_connection()
        cursor =conn.cursor ()
        cursor.execute("DELETE  FROM salle  WHERE code=%s",(code,))
        conn.commit()
        conn.close()


    def get_salle(self,code): 
        conn=self.get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from salle where code=%s", (code,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Salle(*row ) 

        else:
            return None      
 


    def get_salles(self):
        conn=self.get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from salle")
        rows=cursor.fetchall()               
        conn.close()
        salles=[]
        for r in rows:
            code=r[0]
            description=r[1]
            categorie=r[2]
            capacite=r[3]
            salle =Salle(r[0],r[1],r[2],r[3])
            salles.append(salle)
        return salles    
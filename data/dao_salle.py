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
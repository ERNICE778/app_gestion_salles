from data.dao_salle import DataSalle
from models.salle import Salle 
from services.service_salle import ServiceSalle
import customtkinter as ctk 


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GESTION DES SALLES")
        self.geometry("900*1000")
        self.service_salle=ServiceSalle()
    
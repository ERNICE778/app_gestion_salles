from data.dao_salle import DataSalle
from models.salle import Salle 
from services.service_salle import ServiceSalle
import customtkinter as ctk 


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GESTION DES SALLES")
        self.geometry("900x1000")
        self.service_salle=ServiceSalle()


        self.frame_InfoSalle =  ctk.CTkFrame(self)
        self.frame_InfoSalle.pack(pady=10)

        self.label_code=ctk.CTkLabel(self.frame_InfoSalle ,text ="Code:")
        self.label_code.grid(row =0,column=0,pady=5)
        self.entry_code = ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_code.grid(row=0, column=1)


        self.label_desc=ctk.CTkLabel(self.frame_InfoSalle,text="Description:")
        self.label_desc.grid(row=1,column=0,pady=5)
        self.entry_desc=ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_desc.grid(row=1,column=1,pady=5)


        self.label_cat= ctk.CTkLabel(self.frame_InfoSalle,text="Categorie:")
        self.label_cat.grid(row=2,column=0,pady=5)
        self.entry_cat= ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_cat.grid(row=2, column=1, pady=5) 


        self.label_cap =ctk.CTkLabel(self.frame_InfoSalle,text="Capacite:")
        self.label_cap.grid(row=3,column=0,  pady=5)
        self.entry_cap =ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_cap.grid(row=3,column=1, pady=5)



        self.frame_Actions=ctk.CTkFrame(self)
        self.frame_Actions.pack(pady=10)
        self.btn_ajouter = ctk.CTkButton(self.frame_Actions, text="Ajouter",command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0,column=0, padx=10)

        self.btn_modifier =ctk.CTkButton(self.frame_Actions, text="Modifier",command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1,padx=10)

        self.btn_supprimer=ctk.CTkButton(self.frame_Actions, text="Supprimer",command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0,column=2, padx=10)

        self.btn_rechercher =ctk.CTkButton(self.frame_Actions, text="Rechercher")
        self.btn_rechercher.grid(row=0,column=3,padx=10)


    def ajouter_salle(self):
        code=self.entry_code.get()
        desc=self.entry_desc.get()
        cat= self.entry_cat.get()
        cap=self.entry_cap.get()

        Ajout_salle=Salle(code,desc,cat,cap)
        self.service_salle.ajouter_salle(Ajout_salle)

    def modifier_salle(self):
        code=self.entry_code.get()
        desc=self.entry_desc.get()
        cat= self.entry_cat.get()
        cap=self.entry_cap.get()

        salle=Salle(code,desc,cat,cap)
        self.service_salle.modifier_salle( salle)



    def supprimer_salle(self):
        code=self.entry_code.get()
        self.service_salle.supprimer_salle(code)






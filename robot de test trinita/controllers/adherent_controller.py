import pandas as pd
from models.adherent import Adherent

class AdherentController:
    def __init__(self, excel_path, sheet_adherent):
        self.sheet_adherent = sheet_adherent
        self.excel_path = excel_path
        self.data = self.load_data()

    def load_data(self):
        """Load adherent data from Excel"""
        return pd.read_excel(self.excel_path, sheet_name=self.sheet_adherent , dtype={'numero_telephone': str})

    def get_adherent_info(self):
        adherents_data = self.data.to_dict(orient='records')   # Conversion des données en dictionnaires
        adherents = [Adherent.from_dict(data) for data in adherents_data]  # Création des objets Adherent
        return adherents  #  Retourner la liste des objets Adherent

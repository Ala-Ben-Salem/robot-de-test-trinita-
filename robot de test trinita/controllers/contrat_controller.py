import pandas as pd
from models.contrat import Contrat



class ContratController:
    def __init__(self, excel_path, sheet_contrat):
        self.sheet_contrat = sheet_contrat
        self.excel_path = excel_path
        self.data = self.load_data()

    def load_data(self):
        return pd.read_excel(self.excel_path, sheet_name=self.sheet_contrat , dtype={'jour_prelevement': str})

    def get_contrat_info(self):
        contrats_data = self.data.to_dict(orient='records')   # Conversion des données en dictionnaires
        contrats = [Contrat.from_dict(data) for data in contrats_data]  # Création des objets Contrat
        return contrats  #  Retourner la liste des objets Contrat

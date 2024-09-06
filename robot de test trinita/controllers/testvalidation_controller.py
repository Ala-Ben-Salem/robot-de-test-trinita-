import pandas as pd
from models.testvalidation import Testvalidation


class TestvalidationController:
    def __init__(self, excel_path, sheet_testvalidation):
        self.sheet_testvalidation = sheet_testvalidation
        self.excel_path = excel_path
        self.data = self.load_data()

    def load_data(self):
        """Load testvalidation data from Excel"""
        return pd.read_excel(self.excel_path, sheet_name=self.sheet_testvalidation , dtype={'numero_contrat': str})

    def get_testvalidation_info(self):
        testvalidations_data = self.data.to_dict(orient='records')   # Conversion des données en dictionnaires
        testvalidations = [Testvalidation.from_dict(data) for data in testvalidations_data]  # Création des objets testvalidations
        return testvalidations  #  Retourner la liste des objets testvalidations
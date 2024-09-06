import pandas as pd
from models.param import Param


class ParamController:
    def __init__(self, excel_path, sheet_param):
        self.sheet_param = sheet_param
        self.excel_path = excel_path
        self.data = self.load_data()

    def load_data(self):
        """Load param data from Excel"""
        return pd.read_excel(self.excel_path, sheet_name=self.sheet_param , dtype={'psw': str, 'login': str, 'option': str})

    def get_param_info(self):
        params_data = self.data.to_dict(orient='records')   # Conversion des données en dictionnaires
        params = [Param.from_dict(data) for data in params_data]  # Création des objets Param
        return params  #  Retourner la liste des objets Param
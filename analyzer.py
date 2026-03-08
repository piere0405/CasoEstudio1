import pandas as pd

class DataAnalyzer:
    def __init__(self,df):
        self.df=df

    def info_dataset(self):
        return self.df.info()
    
    def tipos_variables(self):
         numericas = self.df.select_dtypes(include=['int64','float64']).columns
         categoricas = self.df.select_dtypes(include=['object']).columns
         return numericas, categoricas
    
    def estadisticas(self):
        return self.df.describe()
    
    def valoresNulos (self):
        return self.df.isnull().sum()

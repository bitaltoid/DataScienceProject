import pandas as pd


class ImportCSV:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        return pd.read_csv(self.file_name)







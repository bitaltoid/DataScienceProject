from data_import import DataImportWebsite
import numpy as np


class ModelParameters:
    def __init__(self, url):
        self.url = url

    def get_params(self):
        price_data = DataImportWebsite(self.url).get_data()[2]
        number_of_rows = len(DataImportWebsite(self.url).get_data()[2])

        # Y variable for lstsq method
        y = np.array(price_data, dtype=float).reshape(number_of_rows, 1)

        # X var
        t = np.arange(start=1, stop=number_of_rows + 1).reshape(number_of_rows, 1)
        const = np.ones(number_of_rows, dtype=int)
        x = np.column_stack((t, const))

        return np.linalg.lstsq(x, y, rcond=None)[0], len(y)


class Forecast:
    def __init__(self, model_coefs, prediction_index):
        self.model_coefs = model_coefs
        self.prediction_index = prediction_index

    def get_forecasted_data(self):
        vfun = np.vectorize(lambda x: self.model_coefs[0][0] * x + self.model_coefs[1][0])

        return (vfun(np.arange(start=self.prediction_index + 1, stop=self.prediction_index + 6))).\
            reshape(1, (self.prediction_index + 6 - (self.prediction_index + 1)))

from data_import_module import DataImportWebsite
import numpy as np
from matplotlib import pyplot


class ModelParameters:

    def __init__(self, url):
        self.url = url

    def get_params(self):
        price_data = DataImportWebsite(self.url).get_data()[2]
        number_of_rows = len(DataImportWebsite(self.url).get_data()[2])

        # Y variable for lsqt method
        y = np.array(price_data, dtype=float).reshape(number_of_rows, 1)

        # X var
        t = np.arange(start=1, stop=number_of_rows + 1).reshape(number_of_rows, 1)
        const = np.ones(number_of_rows, dtype=int)
        x = np.column_stack((t, const))

        return np.linalg.lstsq(x, y, rcond=None)


print(ModelParameters('https://www.investing.com/equities/tesla-motors-historical-data').get_params())

# (array([[ -2.84605872],
#        [704.83558442]]), array([7774.50562676]), 2, array([61.74050057,  2.26066118]))

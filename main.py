import import_module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

test_object = import_module.ImportCSV("btc.csv")
test_data = test_object.get_data()

for column_name in ['24h Open (USD)', '24h High (USD)', '24h Low (USD)']:
    del test_data[column_name]  # deleting useless data

test_data["Date"] = pd.to_datetime(test_data["Date"])
test_data["Date"] = test_data["Date"].dt.strftime("%d/%m")


class TrendCheck:

    def __init__(self, row_number, data):  # [31297.10297669   216.57629318]
        self.row_number = row_number
        self.data = data

    def least_squares_method(self):  # y - btc price, x - date
        self.data["const"] = [1 for x in range(1, self.row_number + 1)]  # const column creation
        self.data["t"] = [x for x in range(1, self.row_number + 1)]  # period numeration
        x = self.data[["const", "t"]].to_numpy()
        y = self.data["Closing Price (USD)"].to_numpy()
        return np.linalg.lstsq(x, y, rcond=None)[0]


object2 = TrendCheck(len(test_data), test_data)
plt.figure(figsize=[10, 7])
ax = plt.axes()
ax.scatter(test_data["Date"], test_data["Closing Price (USD)"])
test_data["test"] = [x for x in range(1, len(test_data) + 1)]
ax.plot(test_data["Date"], test_data["test"] * object2.least_squares_method()[1] + object2.least_squares_method()[0],
        'r')
plt.show()

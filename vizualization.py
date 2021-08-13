from forecast import ModelParameters, Forecast
from data_import import DataImportWebsite
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import matplotlib.dates as mdates
import matplotlib.ticker as tck

url = str(input("Give a link: "))
plot_title = url.replace("https://www.investing.com/equities/", "")
url = url + "-historical-data"

headers = DataImportWebsite(url).get_data()[0]
source_data = pd.DataFrame({headers[0]: DataImportWebsite(url).get_data()[1],
                            headers[1]: DataImportWebsite(url).get_data()[2]}) \
    .astype({headers[0]: 'datetime64', headers[1]: 'float64'})

forecast_function_coefficients = ModelParameters(url).get_params()[0]
forecast_start_index = ModelParameters(url).get_params()[1]

forecasted_prices = Forecast(forecast_function_coefficients, forecast_start_index).get_forecasted_data()
forecasted_prices = [item for sublist in forecasted_prices for item in sublist]

full_data = pd.DataFrame(
    {headers[0]: pd.date_range(date.today() + timedelta(1), periods=len(forecasted_prices), freq='B'),
     headers[1]: forecasted_prices}, index=[x for x in range(22, 27)])
full_data = pd.concat([source_data, full_data])

if forecast_function_coefficients[0][0] < 0:
    line_color = 'red'
elif forecast_function_coefficients[0][0] == 0:
    line_color = 'blue'
else:
    line_color = 'green'

plt.figure(figsize=[10, 7])
ax = plt.axes()

ax.plot(full_data['date'].head(24), full_data['price'].head(24), color='#277abe', linewidth=2)
ax.plot(full_data['date'].tail(5), full_data['price'].tail(5),
        color=line_color, linestyle='dashed', linewidth=3)

plt.xlabel('Date')
plt.ylabel("USD$ Price")
plt.title(plot_title)
plt.fill_between(full_data['date'], full_data['price'], min(full_data['price']), alpha=.15)

ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.yaxis.set_major_formatter(tck.FormatStrFormatter('%.f$'))

plt.show()


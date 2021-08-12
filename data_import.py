import requests
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Tested and developed on investing.com, get data from /historical-data


class DataImportWebsite:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        r = requests.get(self.url,
                         headers={
                             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) '
                                           'AppleWebKit/537.36 (KHTML, '
                                           'like Gecko) '
                                           'Chrome/92.0.4515.131 Safari/537.36 Edge/44.18363.8131'})

        soup = BeautifulSoup(r.text, features='lxml')

        table = soup.find('table', {'class': "genTbl closedTbl historicalTbl"})

        headers = [tx.get('data-col-name') for tx in soup.find_all('th') if tx.get('data-col-name') is not None]

        data = []

        for row in table.find_all('tr')[1:]:
            # Scraping only the Date and Price column
            columns = [element.text.strip() for element in row.find_all('td')[:2]]
            data.append([element for element in columns if element])

        return headers[:2], [x[0] for x in data][::-1], [locale.atof(x[1]) for x in data][::-1]

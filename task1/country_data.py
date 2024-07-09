import requests
from prettytable import PrettyTable


class DataFetcher:
    def fetch_data(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


class CountryData:
    def __init__(self, data_fetcher):
        self.data_fetcher = data_fetcher
        self.response = self.data_fetcher.fetch_data('https://restcountries.com/v3.1/all')

    def create_table(self):
        table = PrettyTable()
        table.field_names = self.get_table_headers()
        self.fill_table(table)
        return table

    def get_table_headers(self):
        return ["Назва країни", "Назва столиці", "Посилання на зображення прапору (PNG)"]

    def fill_table(self, table):
        for country in self.response:
            name = self.get_country_name(country)
            capital = self.get_country_capital(country)
            flag_url = self.get_country_flag_url(country)
            table.add_row([name, capital, flag_url])

    def get_country_name(self, country):
        return country.get('name', {}).get('common', 'N/A')

    def get_country_capital(self, country):
        return country.get('capital', ['N/A'])[0] if 'capital' in country else 'N/A'

    def get_country_flag_url(self, country):
        return country.get('flags', {}).get('png', 'N/A')

    def display_data(self):
        table = self.create_table()
        print(table)


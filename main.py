import sys
from task2.ebay_scraper import EbayScraper
from task1.country_data import CountryData, DataFetcher


def run_ebay_scraper():
    url = "https://www.ebay.com/itm/204877386775?itmmeta=01J2CHYTZK4Y86W3FB5KSAZ9X9&hash=item2fb3a4d417:g:7sIAAOSwQWFmi-6E&amdata=enc%3AAQAJAAAA4ChVHBWOvXQD9uwyvTGhb%2FuFD6IofLewJGkzp1cE2v6Bt4ol1bPyF43mLzKQT66asW2%2FcsJjQhX%2F7wYcus8SXVNf7SrrvnymqwWVB43nUMd9H1d%2FkCpI6N5iuFcT%2Ff%2BglVq00vHBZSjoCr3QtXPOquW9tL9J4A%2FYbt3OI4RTed4%2FK4dm6%2F1dsssGJ57wgcsHRb%2BhuDv%2FageYE9GZ9ZWgcdVL8f6ZUqhv1U2rDhTZOKaYsAgTKNE34O9CCWeNd9nfccSRwFlNlHXJGNMWPOtUHKrH55UIIHO6RP9I81cdjMpZ%7Ctkp%3ABFBM8K_7kZNk"
    scraper = EbayScraper(url)
    data = scraper.scrape_data()
    scraper.print_data()
    scraper.save_to_file('ebay_item_data.json')


def run_country_data():
    data_fetcher = DataFetcher()
    country_data = CountryData(data_fetcher)
    country_data.display_data()


def main(task):
    if task == 'ebay':
        run_ebay_scraper()
    elif task == 'country':
        run_country_data()
    elif task == 'both':
        run_ebay_scraper()
        run_country_data()
    else:
        print("Invalid task. Choose 'ebay', 'country', or 'both'.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <task>")
        print("Tasks: ebay, country, both")
    else:
        main(sys.argv[1])

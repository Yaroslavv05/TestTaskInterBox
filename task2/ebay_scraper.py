import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class EbayScraper:
    def __init__(self, url):
        self.url = url
        self.data = {
            "назва": None,
            "посилання на фото": None,
            "посилання на товар": url,
            "ціна": None,
            "продавець": None,
            "ціна доставки": None
        }
        self.driver = self._setup_driver()

    def _setup_driver(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Чтобы браузер запускался в фоновом режиме
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def scrape_data(self):
        self.driver.get(self.url)

        # Извлечение данных с помощью Selenium
        self.data["назва"] = self._get_element_text('//h1[@class="x-item-title__mainTitle"]')
        self.data["посилання на фото"] = self._get_element_attribute(
            '//div[@class="ux-image-carousel-item image-treatment active  image"]/img', 'src')
        self.data["ціна"] = self._get_element_text('//div[@class="x-price-primary"]')
        self.data["продавець"] = self._get_element_attribute('//div[@class="x-sellercard-atf__info__about-seller"]',
                                                             'title')
        self.data["ціна доставки"] = self._get_shipping_cost()

        self.driver.quit()
        return self.data

    def _get_element_text(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element.text
        except Exception as e:
            print(f"Ошибка при получении текста элемента по XPath {xpath}: {e}")
            return "N/A"

    def _get_element_attribute(self, xpath, attribute):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element.get_attribute(attribute)
        except Exception as e:
            print(f"Ошибка при получении атрибута элемента по XPath {xpath}: {e}")
            return "N/A"

    def _get_shipping_cost(self):
        try:
            shipping_elements = self.driver.find_elements(By.XPATH, '//div[@class="ux-labels-values__values-content"]')
            if len(shipping_elements) > 1:
                return shipping_elements[1].text
            else:
                return "N/A"
        except Exception as e:
            print(f"Ошибка при получении цены доставки: {e}")
            return "N/A"

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def print_data(self):
        print(json.dumps(self.data, ensure_ascii=False, indent=4))

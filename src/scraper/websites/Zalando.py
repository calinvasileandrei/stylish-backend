from bs4 import BeautifulSoup

from src.scraper.websites.Website import Website


class Zalando(Website):
    soup = None;

    def __init__(self, _soup):
        super().__init__(_soup)

    def scrapePrice(self):
        price = self.soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP"})
        if (not price == None):
            return price.text
        else:
            price = self.soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi dgII7d z-oVg8 _88STHx cMfkVL"})
            if (not price == None):
                return price.text
            else:
                return "nodata"

    def scrapeImage(self):
        return ("no implementatio")

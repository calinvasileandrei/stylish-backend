from bs4 import BeautifulSoup
from src.scraper.websites.Website import Website


class Zalando(Website):
    soup = None;

    def __init__(self, _soup):
        super().__init__(_soup)

    def work(self):
        data={
            "brand": self.__scrapeBrand(),
            "title": self.__scrapeTitle(),
            "price": self.__scrapePrice(),
            "image": self.__scrapeImage()
              }
        return data

    def __scrapeBrand(self):
        brand = self.soup.find("span",attrs={"class":"_7Cm1F9 ka2E9k uMhVZi dgII7d z-oVg8 pVrzNP BDUtDm GhPDv6 q-6yg2 e5adJm _9bYLON CJVJQ4 _2LebSa"})
        if(not brand == None):
            return brand.text
        else:
            return "nodata"

    def __scrapeTitle(self):
        title = self.soup.find("h1", attrs={"class": "OEhtt9 ka2E9k uMhVZi z-oVg8 pVrzNP w5w9i_ _1PY7tW _9YcI4f"})
        if (not title == None):
            return title.text
        else:
            return "nodata"

    def __scrapePrice(self):
        price = self.soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP"})
        if (not price == None):
            return price.text
        else:
            price = self.soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi dgII7d z-oVg8 _88STHx cMfkVL"})
            if (not price == None):
                return price.text
            else:
                return "nodata"

    def __scrapeImage(self):
        image = self.soup.find("img", attrs={
            "class": "_6uf91T z-oVg8 u-6V88 ka2E9k uMhVZi FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF PZ5eVw"})
        if (not image == None):
            return image["src"].split("?", 1)[0]
        else:
            return "nodata"

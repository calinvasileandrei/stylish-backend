from bs4 import BeautifulSoup
import requests

headers = {
    'Host': 'www.zalando.it',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection' : 'close',
    'Upgrade-Insecure-Requests': '1'
}

link = ""
rs = requests.Session()
rs.headers.update(headers)
req = rs.get(link)
soup = BeautifulSoup(req.text, 'html.parser')

def scrapeBrand(soup):
    title = soup.find("spanc", attrs={
        "class": "_7Cm1F9 ka2E9k uMhVZi dgII7d z-oVg8 pVrzNP BDUtDm GhPDv6 q-6yg2 e5adJm _9bYLON CJVJQ4 _2LebSa"})
    if (not title == None):
        return title.text
    else:
        return "nodata"


def scrapePrice(soup):
    price = soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP"})
    if (not price == None):
        return price.text
    else:
        price = soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi dgII7d z-oVg8 _88STHx cMfkVL"})
        if (not price == None):
            return price.text
        else:
            return "nodata"


def scrapeImage(soup):
    image = soup.find("img" ,attrs={"class" :"_6uf91T z-oVg8 u-6V88 ka2E9k uMhVZi FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF PZ5eVw"})
    if(not image == None):
        return image["src"].split("?",1)[0]
    else:
        return "nodata"


def scrapeTitle(soup):
    title = soup.find("h1",attrs={"class":"OEhtt9 ka2E9k uMhVZi z-oVg8 pVrzNP w5w9i_ _1PY7tW _9YcI4f"})
    if(not title == None):
        return title.text
    else:
        return "nodata"


print(scrapeTitle(soup))
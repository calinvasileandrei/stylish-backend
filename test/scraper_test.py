from bs4 import BeautifulSoup
from lxml import etree
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

link = "https://www.zalando.it/vitaly-transit-collana-silver-coloured-vig54l001-d11.html"
rs = requests.Session()
rs.headers.update(headers)
req = rs.get(link)
soup = BeautifulSoup(req.text, 'html.parser')

price = soup.find("span",attrs={"class":"uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP"})
if(not price == None):
    print(price.text)
else :
    price = soup.find("span", attrs={"class": "uqkIZw ka2E9k uMhVZi dgII7d z-oVg8 _88STHx cMfkVL"})
    if(not price == None):
        print(price.text)
    else:
        print("no data")



'''
#print(soup.prettify())
dom = etree.HTML(str(soup))
print(dom.xpath('/html/body/div[4]/div/div[1]/div/div[2]/x-wrapper-re-1-3'))
'''

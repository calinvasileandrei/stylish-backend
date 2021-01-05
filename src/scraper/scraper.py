from bs4 import BeautifulSoup
import requests
import importlib

class Scraper:
    link =''
    supported_sites= ["Zalando"]
    rs = None
    headers = {
        'Host': 'www.zalando.it',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }

    def __init__(self, _link):
        self.link = _link
        #init request session with headers
        self.rs = requests.Session()
        self.rs.headers.update(self.headers)

    def set_link(self,link):
        self.link = link

    def scrape_link(self):
        cls = self.__check_site()
        if( not cls == False and not self.link ==None and not self.link =='' ):
            return self.__worker(cls);
        else:
            return {"status":"Error" , "msg":"Unsupported Link"}


    def __worker(self,cls):
        req = self.rs.get(self.link)
        soup = BeautifulSoup(req.text, 'html.parser')
        data = {"price":"","title":"","description":"","image":""}
        try:
            site = cls(soup)
            data["price"] = site.scrapePrice()
        except Exception as e:
            print("error: ",e)

        return {"status":"Ok", "msg":"Operation Completed!", "data":data}

    def __check_site(self):
        for site in self.supported_sites:
            if(site.lower() in self.link ):
                return self.factoryClassInstance(site)
            else:
                return False

    def factoryClassInstance(self,class_name):
        # load the module, will raise ImportError if module cannot be loaded
        m = importlib.import_module("scraper.websites."+class_name)
        # get the class, will raise AttributeError if class cannot be found
        c = getattr(m, class_name)
        return c
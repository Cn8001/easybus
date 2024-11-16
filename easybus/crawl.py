from bs4 import BeautifulSoup
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import Firefox
from get_gecko_driver import GetGeckoDriver
import pathlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebData(object):
    """
    Scrap data and find elements

    """
    def __init__(self,from_city,to_city,date,url=None):
        
        self.from_city = from_city
        self.to_city = to_city
        self.date = date
        self.url = f"https://www.enuygun.com/otobus-bileti/arama/{from_city}-{to_city}/?gidis={date}"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'Accept-Language': 'en-US, en;q=0.5'}
    
    def _get_page_source(self):
        """
        Scraps the data according to self.url
        :returns: Page source, None if response is null.
        :raises: ConnectionError if server do not respond
        """
        source = None
        
        try:

            self._get_driver()
            options = FirefoxOptions()
            options.add_argument("--headless")
            webDriver = Firefox(options=options)
            response = webDriver.get(self.url)
            try:
                wait = WebDriverWait(webDriver, 20)
                wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".prov-3"))
                )
                source = webDriver.page_source
            except:
                print("No element")
        except:
            raise ConnectionError()
        return source
    
    def _get_driver(self):
        """
        Installs gecko driver
        """

        gecko = GetGeckoDriver()
        if not pathlib.Path('../tools/geckodriver.exe').exists():
            gecko.install(output_path="../tools")

    def get_data(self):

        response = self._get_page_source()
        busList = []
        if not response:
            return busList
        try:
            soup = BeautifulSoup(response,'html.parser')

            journeybase = soup.find_all('div',{'class':'prov-3'})
            for journey in journeys:
                busList.append(journey) 
        except ValueError:
            pass
        return busList

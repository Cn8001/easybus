from bs4 import BeautifulSoup
import dateutil.tz
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import Firefox
from get_gecko_driver import GetGeckoDriver
import pathlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os,sys
from easybus.models.BusJourney import BusJourney
import datetime
import dateutil

class WebData:
    """
    Scrap data and find elements

    """
    def __init__(self,from_city,to_city,date,url=None):
        
        self.from_city = from_city
        self.to_city = to_city
        self.date = date
        self.url = f"https://www.enuygun.com/otobus-bileti/arama/{from_city}-{to_city}/?gidis={date}"
    
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

    def _generate_value(self,name,hour,price : str,route,duration : str,seat_type):
        """
        Generates BusJourney objects based on scraped values
        Datetime timezone is Europe/Istanbul
        """
        
        tz = dateutil.tz.gettz("Europe/Istanbul")
        hour = datetime.datetime.strptime(self.date + " " + hour.strip(),"%d.%m.%Y %H:%M") #Generate datetime object
        hour.replace(tzinfo=tz) #Replace tzdata with UTC+3

        price = float(price.rstrip(" TL").strip().replace(',','.'))
        durationL = duration.strip().split(" ")

        #Calculate duration via hour*60+minutes
        duration = int(duration[0])*60

        if len(durationL) > 2:
            duration += int(durationL[2])
        return BusJourney(name=name,price=price,route=route,duration=duration,seat_type=seat_type,hour=hour)

    def get_data(self):
        """
        Scraps the data with BeautifulSoup

        :returns: BusJourney object list (Empty list on error)
        """
        response = self._get_page_source()
        busList = []
        if not response:
            return busList
        soup = BeautifulSoup(response,'html.parser')

        journeys = soup.find_all('div',{'class':'prov-3'})
        
        for bus in journeys:
            hour = bus.find('div',{'class':'hour-text'})
            price = bus.find('strong',{'class':'priceFractionDigitsContainer'})
            route = bus.find('span',{'class':'journey-route align-center'})
            duration = bus.find('div',{'class':'journey-time-diff align-center'})
            seat_type = bus.find('div',{'class':'bus-seat-type align-center'})
            img_alt = bus.find('div',{'class':'company-image-container'}).find('img').get('alt') #Extract name

            journeyobj = self._generate_value(img_alt,hour.text,price.text,
                                                route.text,duration.text,seat_type.text)
            busList.append(journeyobj)
        return busList

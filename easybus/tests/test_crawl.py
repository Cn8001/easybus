import sys
import os

sys.path.append(os.path.abspath('../easybus'))
import crawl

from models.BusJourney import BusJourney
import datetime

crawler = crawl.WebData('izmir-otogari','ankara-otogari','17.11.2024')
    

def test_bus_journey():
    data = BusJourney(name="test",price=12.7,route="izmirankara",duration=720,seat_type="2+1",
                      hour=datetime.datetime.now())
    
def test_generate_value():
    crawler = crawl.WebData('izmir-otogari','ankara-otogari','17.11.2024')
    data = crawler._generate_value("Test","19:00","127.2","AnkaraIzmir","480","2+1")
    assert data.hour == datetime.datetime.strptime("17.11.2024 19:00","%d.%m.%Y %H:%M")
test_generate_value()
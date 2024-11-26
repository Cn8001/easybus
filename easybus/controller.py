from fastapi import FastAPI
from easybus.models.BusJourney import BusJourney
from easybus import crawl

app = FastAPI()

@app.get('/v2/api/{from_city}/{to_city}/{date}')
async def get_journeys(from_city: str, to_city: str, date: str) -> list[BusJourney]:
    """
    Controller for journey crawling

    :param from_city: Departure city
    :param to_city: Where to go
    :param date: Date string formatted as d.M.Y
    :returns: BaseJourney list (Empty list on error)
    """
    crawler = crawl.WebData(from_city=from_city,to_city=to_city,date=date)
    dataList : list[BusJourney] = crawler.get_data()
    return dataList
    



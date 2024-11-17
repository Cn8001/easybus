from datetime import datetime
from pydantic import BaseModel
class BusJourney(BaseModel):
    """
    BusJourney base class
    :param name: Bus company name
    :param price: Price in TL (Turkish liras) : float
    :param route: Route data
    :param duration: Duration in minutes
    :param seat_type: Seat type of the bus (2+1 / 2+2)
    :param hour: Departure time
    """

    name: str
    price: float
    route: str
    duration: int
    seat_type: str
    hour: datetime
from datetime import datetime
from pydantic import BaseModel
class BusJourney(BaseModel):

    name: str
    price: float
    route: str
    duration: int
    seat_type: str
    hour: datetime
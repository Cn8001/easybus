class BusJourney(object):
    """
    BusJourney base class
    :param name: Bus company name
    :param price: Price in TL (Turkish liras) : float
    :param route: Route data
    :param duration: Duration in minutes
    :param seat_type: Seat type of the bus (2+1 / 2+2)
    :param hour: Departure time
    """

    def __init__(self,name,price,route,duration,seat_type,hour):

        self.name = name
        self.price = price
        self.route = route
        self.duration = duration
        self.seat_type = seat_type
        self.hour = hour
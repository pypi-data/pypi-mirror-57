from enum import Enum

class FNBRequestObject:
    def __init__(self):
        self.action = ""
        self.endpoint = ""
        self.airport = ""
        self.aircraft_id = ""
        self.carrier = ""
        self.flight_number = ""
        self.year = ""
        self.month = ""
        self.day = ""
        self.time = ""


    def __str__(self):
        action = "" if not self.action.value in ['register', 'unregister'] else "{}/".format(self.action.value)
        endpoint = "" if not self.endpoint.value in ['arrival', 'departure'] else "{}/".format(self.endpoint.value)
        airport = "" if self.airport == "" else "{}/".format(self.airport)
        aircraft_id = "" if self.aircraft_id == "" else "ACID/{}/".format(self.aircraft_id)
        carrier = "" if self.carrier == "" else "{}/".format(self.carrier)
        flight_number = "" if self.flight_number == "" else "{}/".format(self.flight_number)
        year = "" if self.year == "" else "{}/".format(self.year)
        month = "" if self.month == "" else "{}/".format(self.month)
        date = "" if self.day == "" else "{}/".format(self.day)
        time = "" if self.time == "" else "{}/".format(self.time)

        return "{}{}{}{}{}{}{}{}{}{}".format(action, endpoint, airport, aircraft_id, carrier, flight_number, year,
                                             month, date, time)


class ActionType(Enum):
    REGISTER = 'register'
    UNREGISTER = 'unregister'

class EndpointType(Enum):
    ARRIVAL = 'arrival'
    DEPARTURE = 'departure'
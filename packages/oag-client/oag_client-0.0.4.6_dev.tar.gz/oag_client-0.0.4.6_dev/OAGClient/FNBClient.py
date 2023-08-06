import requests
import json
from .flight_view_helper import convert_oag_status_to_normal_form

class FNBClient:
    def __init__(self, app_id, app_key):
        self.URL = "https://fnb.flightview.com/"
        self.app_id = app_id
        self.app_key = app_key

    def make_request(self, fnb_request_object):
        post_bosy = {
            "RequestParameters": {
                "appid": self.app_id,
                "appkey": self.app_key
            }
        }
        request_url = self.URL + str(fnb_request_object)

        response = requests.post(url=request_url, data=json.dumps(post_bosy))
        content = json.loads(response.content)

        if response.status_code == 200 and content['Success']:
            return response
        else:
            return {"error": response.status_code, "content": content}

    def parse_update(self, update_dict):
        flight = {
            'FlightIdentifier': update_dict['FlightIdentifier'],
            'Alert': update_dict['Alert'],
            'Flight': {
                'FvFlightId': update_dict['Flight']['FvFlightId'],
                'airline_iata': update_dict['Flight']['AirlineCode'],
                'number': update_dict['Flight']['FlightNumber'],
                'origin_airport_code': update_dict['Flight']['SchedDepartureAirportCode'],
                'dest_airport_code': update_dict['Flight']['SchedArrivalAirportCode'],
                'status': convert_oag_status_to_normal_form(update_dict['Flight']['Status'].lower()),
                'origin_scheduled_dep': update_dict['Flight']['SchedDepartureLocal'],
                'dest_scheduled_arrival': update_dict['Flight']['SchedArrivalLocal'],
                'origin_scheduled_dep_utc': update_dict['Flight']['SchedDepartureUtc'],
                'dest_scheduled_arrival_utc': update_dict['Flight']['SchedArrivalUtc'],
                'estimated_departure_accuracy': update_dict['Flight']['LatestDeparture']['Accuracy'],
                'estimated_departure_utc': update_dict['Flight']['LatestDeparture']['DateTimeUtc'],
                'estimated_departure': update_dict['Flight']['LatestDeparture']['DateTimeLocal'],
                'estimated_arrival_accuracy': update_dict['Flight']['LatestArrival']['Accuracy'],
                'estimated_arrival_utc': update_dict['Flight']['LatestArrival']['DateTimeUtc'],
                'estimated_arrival': update_dict['Flight']['LatestArrival']['DateTimeLocal'],
                'origin_terminal': update_dict['Flight']['DepartureTerminal'],
                'dest_terminal': update_dict['Flight']['ArrivalTerminal'],
                'origin_gate':  update_dict['Flight']['DepartureGate'],
                'dest_gate': update_dict['Flight']['ArrivalGate'],
                'dest_baggage': update_dict['Flight']['Baggage'],
                'aircraft_type': update_dict['Flight']['AircraftType'],
                'origin_country':  update_dict['Flight']['DepAirportCountryId'],
                'dest_country': update_dict['Flight']['ArrAirportCountryId'],
                'tail_number': update_dict['Flight']['TailNumber'],
            },
            "AlertIdentifier": update_dict['AlertIdentifier'],
        }

        return flight


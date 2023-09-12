import requests
from pprint import pprint
API_KEY = "YOUR API KEY"
END_POINT = 'https://api.tequila.kiwi.com/locations/query'
KEYS = {"apikey": API_KEY}
class FlightSearch:
    def get_destination_code(self,city):
        body = {"term" : city}
        response = requests.get(url=END_POINT,
                                params=body,
                                headers=KEYS)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

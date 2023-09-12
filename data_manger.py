import requests
from requests.auth import HTTPBasicAuth
import os

USER = os.environ["GOOGLE_SHEETS_USER"]
PASSWORD = os.environ["GOOGLE_SHEETS_PASS"]
LINK =  "https://api.sheety.co/YOUR LINK"

class DataManger:
    def __init__(self):
        self.basic = HTTPBasicAuth(USER,PASSWORD)

    def get_info(self):
        response = requests.get(url=LINK,auth=self.basic)
        sheet_data = response.json()
        return sheet_data
    def put_info(self,body):
        for city in body['prices']:
            value_body = {
                "price": {
                    'iataCode':city["iataCode"],
                    'lowestPrice': city['lowestPrice']
                    }
                    } 
            print(value_body)
            response = requests.put(
                url=f"{LINK}/{city['id']}", 
                json=value_body,
                auth=self.basic)
            response.raise_for_status()
            print(response.json)








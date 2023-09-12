import requests
from datetime import datetime, timedelta
API_KEY = "YOUR API KEY"
END_POINT = 'https://api.tequila.kiwi.com'
HEADER = {"apikey" : API_KEY}
class FlightData:
    LINK = END_POINT+"/v2/search"
    def __init__(self,departure_airport_code,departure_city):
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.tomorrow = None
        self.next_six_months = None
        self.time_info()
    def construct_body(self):
         body = {"fly_from" : "ICN",
                "fly_to" : self.departure_airport_code, 
                "date_from" : self.tomorrow,
                "date_to" : self.next_six_months ,
                "adults" : 1,
                "adult_hold_bag": "1", 
                "adult_hand_bag":"1",
                "curr":  "KRW"}
         return body
    def search_for_ticket(self):
        body = self.construct_body()
        response = requests.get(url=self.LINK,params=body,headers=HEADER)
        response.raise_for_status()
        try:
            ticket_price = response.json()['data'][0]
            return {self.departure_city:ticket_price}
        except:
            return {self.departure_city:"No data"}
        
    def time_info(self):
        #Create time class
        tomorrow_datetime = datetime.now() + timedelta(days=1)
        next_six_months = datetime.now() + timedelta(days=180)
        self.tomorrow = tomorrow_datetime.strftime("%d/%m/%Y")
        self.next_six_months =  next_six_months.strftime("%d/%m/%Y")

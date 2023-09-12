from twilio.rest import Client
account_sid = "AC0297b20d0406a5c16cee090742491697"
auth_token = "824c35473f8c1f5c715e0ea5c8314b53"

class NotificationManager:
    def __init__(self,price,dep_city,dep_iata,
                 arrival_city,arrival_iata,
                 outbound_data,inbound_data,deep_link):
        self.client = Client(account_sid, auth_token)
        self.price = price
        self.dep_city = dep_city
        self.dep_city_iata = dep_iata
        self.arrival_city = arrival_city
        self.arrival_iata = arrival_iata
        self.outbound_data = outbound_data
        self.inbound_data = inbound_data
        self.deep_link = deep_link

    def message_to_client(self):
            content = f"""
                Price: {self.price}
                Departure City Name: {self.dep_city}
                Departure Airport IATA Code: {self.dep_city_iata}
                Arrival City Name: {self.arrival_city}
                Arrival Airport IATA Code: {self.arrival_iata}
                Outbound Date: {self.outbound_data}
                Inbound Date: {self.inbound_data}
                Link: {self.deep_link}
                    """
            message = self.client.messages.create(
                    body=content,
                    from_='+17622486351',
                    to='+821056827198'
                 )
            print(message.sid)

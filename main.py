from data_manger import DataManger
from pprint import pprint
from flight_data_search import FlightSearch
from flight_data import FlightData
from notification import NotificationManager
data = DataManger()
sheet_data = data.get_info()
ex_sheet_data = sheet_data
pprint(sheet_data)
iter_order = 0
print("\n\n")
iata_codes = []
tickets = [] 
all_info_abt_tickets = []
p = FlightSearch()

for city in sheet_data["prices"]:
    which_city =city['city']
    code = p.get_destination_code(which_city)
    iata_codes.append(code)

print(iata_codes)    

for dic_value in sheet_data["prices"]:
    if dic_value["iataCode"] == "":
        sheet_data["prices"][iter_order]["iataCode"] = iata_codes[iter_order]
    ticket_info = FlightData(dic_value["iataCode"],dic_value['city'])
    all_data = ticket_info.search_for_ticket()
    new_ticket_info = {all_data[dic_value['city']]['cityTo']:all_data[dic_value['city']]['price']}
    tickets.append(new_ticket_info)
    all_info_abt_tickets.append(all_data)
    if dic_value["lowestPrice"] > tickets[iter_order][dic_value['city']]:
        sheet_data["prices"][iter_order]["lowestPrice"] = tickets[iter_order][dic_value['city']]
    iter_order +=1
print("\n\n")
print(tickets,"\n")
print("AFTER UPDATE")
pprint(sheet_data)

data.put_info(sheet_data)

#Twilio part!
iter_order = 0
for dic_value in sheet_data["prices"]:
    if ex_sheet_data['prices'][iter_order]['lowestPrice'] > dic_value["lowestPrice"]:
        #This logic must be taken to action!
        city= dic_value['city']
        my_info = all_info_abt_tickets[iter_order]
        tw = NotificationManager(
            price=my_info[city]['price'],
            dep_city=my_info[city]['cityFrom'],
            dep_iata= my_info[city]['flyFrom'],
            arrival_city= my_info[city]["cityTo"],
            arrival_iata= my_info[city]['flyTo'],
            outbound_data= my_info[city]['route'][0]['cityFrom'],
            inbound_data= my_info[city]['route'][0]['cityTo'],
            deep_link=my_info[city]['deep_link'])
        tw.message_to_client()
    iter_order +=1

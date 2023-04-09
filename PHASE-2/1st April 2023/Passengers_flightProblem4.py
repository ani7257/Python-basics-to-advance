#Problem4
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name):
    passengers = []
    for ticket in ticket_list:
        flight_no = ticket.split(":")[0]
        if flight_no.startswith(airline_name):
            passengers.append(ticket.split(":")[-1])
    return passengers

def find_passengers_destination(destination):
    passengers = []
    for ticket in ticket_list:
        if ticket.split(":")[2] == destination:
            passengers.append(ticket.split(":")[-1])
    return passengers

def find_passengers_per_flight():
    passengers_per_flight = {}
    for ticket in ticket_list:
        flight_no = ticket.split(":")[0]
        if flight_no not in passengers_per_flight:
            passengers_per_flight[flight_no] = 1
        else:
            passengers_per_flight[flight_no] += 1
    for flight_no, count in passengers_per_flight.items():
        print(f"Flight {flight_no} has {count} passengers.")

def sort_passenger_list():
    return sorted(ticket.split(":")[-1] for ticket in ticket_list)

print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
find_passengers_per_flight()
print(sort_passenger_list())


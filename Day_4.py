flights = {
    "F101": ["Chennai", "Delhi", 5, 4500],
    "F102": ["Delhi", "Mumbai", 4, 5000],
    "F103": ["Bangalore", "Hyderabad", 6, 3500],
    "F104": ["Kolkata", "Chennai", 3, 4200]
}

def show_flights():
    print("\nAvailable Flights")
    for flight_no, details in flights.items():
        print(flight_no, "-", details[0], "to", details[1])

def book_flight(flight_no):
    if flight_no in flights:
        print("\nFlight Number :", flight_no)
        print("Source :", flights[flight_no][0])
        print("Destination :", flights[flight_no][1])
        print("Available Seats :", flights[flight_no][2])
        print("Ticket Price :", flights[flight_no][3])

        seats = int(input("\nEnter seats to book: "))

        if seats <= flights[flight_no][2]:
            flights[flight_no][2] -= seats

            print("\nBooking Successful")
            print("Passenger Name : Elakiya")
            print("Seats Booked :", seats)
            print("Remaining Seats :", flights[flight_no][2])
        else:
            print("\nNot enough seats available")
    else:
        print("Invalid Flight Number")


show_flights()

flight_no = input("\nEnter Flight Number: ")

book_flight(flight_no)

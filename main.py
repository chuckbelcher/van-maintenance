import datetime
import database

menu = """Please select one of the following options: 
 1) Add new Vehicle
 2) Add Maintenance Event
 3) View all Vehicles
 4) View all Maintenance Events
 5) View Maintenance Events for a Vehicle
 6) Exit

 Your Selection: """

welcome_message = "Sudzypets Van Maintenance Log"


def add_vehicle():
    vehicle_year = input("What is the year for the vehicle: ")
    vehicle_make = input("What is the make for the vehicle: ")
    vehicle_model = input("What is the model for the vehicle: ")
    vehicle_garage = input("Where is the vehicle stored: ")
    vehicle_garage = input("Is Vehicle active: ")
    database.add_vehicle(
                         vehicle_year,
                         vehicle_make,
                         vehicle_model,
                         vehicle_garage)


def add_maintenance():
    vehicle_id = input("What is the id of the vehicle receiving maintenance: ")
    maintenance_location = input("Where was the vehicle serviced: ")
    service_performed = input("What service was performed: ")
    maintenance_cost = input("How much was the maintenance: ")
    vehicle_miles = input("How many miles are on the vehicle: ")
    maintenance_date = input(
        "What date was the maintenance performed (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(maintenance_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_maintenance(vehicle_id,
                             maintenance_location,
                             service_performed,
                             maintenance_cost,
                             vehicle_miles,
                             timestamp)


def display_maintenance(vehicle_maintenance_list):
    print(f"{heading} Maintenance List")
    for vehicle_id, maintenance_localtion, service_performed, maintenance_cost, vehicle_miles, timestamp, in vehicle_maintenance_list:
        maintenance_date = datetime.datetime.fromtimestamp(
            timestamp).strftime("%b %d %Y")
        print(f"{vehicle_id}: {maintenance_localtion} {service_performed} {maintenance_cost} {vehicle_miles} - performed on {maintenance_date}")
    print("---\n")


def display_vehicles(vehicles):
    print(" Vehicle List")
    for _id, year, make, model, garage, active in vehicles:
        if active == 'Y':
            currentUse = 'In use'
        else:
            currentUse = "Not in use"
        print(f"{_id}: {year} {make} {model} {currentUse} located at {garage}")
    #print (vehicles)
    print("---\n")


print(welcome_message)
database.create_tables()

while (user_input := input(menu)) != '6':
    if user_input == "1":
        add_vehicle()
    elif user_input == "2":
        add_maintenance()
    elif user_input == "3":
        vehicles = database.get_vehicles()
        display_vehicles(vehicles)
    elif user_input == "4":
        watch_movie()
    elif user_input == "5":
        username = input('Username: ')
        movies = database.get_watched_movies(username)
        if movies:
            display_movies(f'{username}\'s', movies)
        else:
            print(f'{username} has not watched any movies\n---\n')
    elif user_input == "6":
        add_user()
    elif user_input == "7":
        title = input('What movie would you like to search for? ')
        print(f'Searching for {title}\n')
        movies = database.search_movies(title)
        if movies:
            display_movies("Found", movies)
        else:
            print(f'No movies with {title} found in database\n')
    else:
        print("You did not enter a valid selection")

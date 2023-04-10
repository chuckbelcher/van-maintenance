"""Module providingFunction for datetime conversionspython version."""
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

welcome_message = "Sudzy Pets Van Maintenance Log"

def add_vehicle():
    vehicle_year = input("What is the year for the vehicle: ")
    vehicle_make = input("What is the make for the vehicle: ")
    vehicle_model = input("What is the model for the vehicle: ")
    vehicle_garage = input("Where is the vehicle stored: ")
    vehicle_active = input("Is Vehicle active Y for yes or N for no: ")
    database.add_vehicle(
        vehicle_year,
        vehicle_make,
        vehicle_model,
        vehicle_garage,
        vehicle_active)


def add_maintenance():
    display_vehicles(database.get_vehicles())

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


def display_maintenance_events(maintenance_list):
    """Function for displaying maintenance events for all vehicles"""
    print("Maintenance List")
    for maintenance_id, vehicle_id, maintenance_location, service_performed, vehicle_miles, maintenance_cost, timestamp, in maintenance_list:
        maintenance_date = datetime.datetime.fromtimestamp(
            timestamp).strftime("%b %d %Y")
        print(f"{vehicle_id}: {maintenance_id} {maintenance_location} {service_performed} {maintenance_cost} {vehicle_miles} - performed on {maintenance_date}")
    print("---\n")


def display_maintenance_for_vehicle(vehicle_maintenance):
    """Function for displaying maintenance events for a specific vehicle"""
    for year, make, model, garage, milage, maintenance_location, service_performed, maintenance_cost, service_date in vehicle_maintenance:
        maintenance_date = datetime.datetime.fromtimestamp(
            service_date).strftime("%b %d %Y")
        print(f"{maintenance_date} - {year} {make} {model} housed at {garage} with {milage} miles was service at {maintenance_location} receiving {service_performed} for ${maintenance_cost}")
    print("---\n")


def display_vehicles(vehicles):
    print(" Vehicle List")
    for _id, year, make, model, garage, active in vehicles:
        if active == 'Y':
            currentUse = 'In use'
        else:
            currentUse = "Not in use"
        print(vehicles)
        print(f"{_id}: {year} {make} {model} {currentUse} located at {garage}")
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
        maintenance = database.get_all_maintenance()
        display_maintenance_events(maintenance)
    elif user_input == "5":
        vehicle_id = input("What is the id of the vehicle: ")
        maintenance = database.get_maintenance_for_vehicle(vehicle_id)
        display_maintenance_for_vehicle(maintenance)
    else:
        print("You did not enter a valid selection")

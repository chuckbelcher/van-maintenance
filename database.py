import datetime
import sqlite3

CREATE_MAINTENANCE_TABLE = """CREATE TABLE IF NOT EXISTS maintenance (
   id INTEGER PRIMARY KEY,
   vehicle_id INTEGER,
   location TEXT,
   service_performed TEXT,
   vehicle_miles INTEGER,
   price FLOAT,
   service_date REAL,
   FOREIGN KEY (vehicle_id) references vehicles(id)
);"""

CREATE_VEHICLE_TABLE = """CREATE TABLE IF NOT EXISTS vehicles (
   id INTEGER PRIMARY KEY,
   vehicle_year,
   vehicle_make,
   vehicle_model,
   vehicle_garage,
   active
);"""

INSERT_MAINTENANCE = "INSERT INTO maintenance (vehicle_id, location, service_performed, price, vehicle_miles, service_date) VALUES (?, ?, ?, ?, ?, ?)"

INSERT_VEHICLE = "INSERT INTO vehicles (vehicle_year, vehicle_make, vehicle_model, vehicle_garage, active) VALUES (?, ?, ?, ?, ?)"
SELECT_ALL_VEHICLES = "SELECT * FROM vehicles;"
SELECT_ALL_MAINTENANCE = "SELECT * FROM maintenance;"
SELECT_MAINTENANCE_FOR_VEHICLE = """select v.vehicle_year,
	                                    v.vehicle_make,
	                                    v.vehicle_model,
	                                    v.vehicle_garage,
	                                    m.vehicle_miles,
	                                    m.location,
	                                    m.service_performed,
	                                    m.price
                                    from vehicles v
                                    join maintenance m on v.id = m.vehicle_id
                                    where v.id = ?;"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MAINTENANCE_TABLE)
        connection.execute(CREATE_VEHICLE_TABLE)


def add_vehicle(vehicle_year, vehicle_make, vehicle_model, vehicle_garage, active):
    with connection:
        connection.execute(INSERT_VEHICLE, (vehicle_year,
                           vehicle_make, vehicle_model, vehicle_garage, active))


def add_maintenance(vehicle_id, location, service_performed, price, vehicle_miles, service_date):
    print(vehicle_id, location, service_performed,
          price, vehicle_miles, service_date)
    with connection:
        connection.execute(INSERT_MAINTENANCE, (vehicle_id, location,
                           service_performed, price, vehicle_miles, service_date))


def get_vehicles():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_VEHICLES)
        return cursor.fetchall()


def get_all_maintenance():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_MAINTENANCE)
        return cursor.fetchall()


def get_maintenance_for_vehicle(vehicle_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_MAINTENANCE_FOR_VEHICLE, (vehicle_id))
        return cursor.fetchall()

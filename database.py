import datetime
import sqlite3

CREATE_MAINTENANCE_TABLE = """CREATE TABLE IF NOT EXISTS maintenance (
   id INTEGER PRIMARY KEY,
   location TEXT,
   service_performed TEXT,
   vehicle_miles
   service_date REAL
);"""

CREATE_VEHICLE_TABLE = """CREATE TABLE IF NOT EXISTS vehicles (
   id INTEGER PRIMARY KEY,
   vehicle_year,
   vehicle_make,
   vehicle_model,
   vehicle_garage,
   active
);"""

INSERT_MAINTENANCE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
INSERT_VEHICLE = "INSERT INTO vehicles (vehicle_year, vehicle_make, vehicle_model, vehicle_garage) VALUES (?, ?, ?, ?)"
SEARCH_MAINTENANCE = "SELECT * FROM movies WHERE title like ?;"
SELECT_ALL_MAINTENANCE = "SELECT * FROM movies;"
SELECT_MAINTENANCE_FOR_VEHICLE = """SELECT movies.*
                            FROM movies
                            JOIN watched ON movies.id = watched.movie_id
                            JOIN users ON users.username = watched.user_username
                            WHERE users.username = ?;"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MAINTENANCE_TABLE)
        connection.execute(CREATE_VEHICLE_TABLE)


def add_vehicle(vehicle_year, vehicle_make, vehicle_model, vehicle_garage):
    with connection:
        connection.execute(INSERT_VEHICLE, (vehicle_year, vehicle_make, vehicle_model, vehicle_garage))


def add_maintenance(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MAINTENANCE, (title, release_timestamp))


def search_maintenance():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MAINTENANCE, (f'%{movie}%',))
        return cursor.fetchall()


def get_all_maintenance():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_MAINTENANCE, (username,))
        return cursor.fetchall()


def get_maintenance_for_vehicle():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_MAINTENANCE, (username,))
        return cursor.fetchall()

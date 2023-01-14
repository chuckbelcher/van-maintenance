import datetime
import database

menu = """Please select one of the following options: 
 1) Add new Vehicle
 2) Add Maintenance Event
 3) View all Mainenance Events
 4) View Maintenance Events for a Vehicle
 5) Exit

 Your Selection: """
 
welcome_message = "Sudzypets Van Maintenance Log"

def add_movie():
    title = input("What is the name of the movie: ")
    release_date = input("What is the release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    
    database.add_movie(title, timestamp)

def display_movies(heading, movies):
    print(f"{heading} Movies List")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date).strftime("%b %d %Y")
        print(f"{_id}: {title} - released on {movie_date}")
    print("---\n")


def watch_movie():
    username = input("Username: ")
    movie_id = input("What movie id do you want to watch? ")
    database.watch_movie(username, movie_id)

def add_user():
    username = input("What is the name of the new user? ")
    database.add_user(username)

print(welcome_message)
database.create_tables()

while (user_input := input(menu)) !='8':
    if user_input == "1":
        add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        display_movies("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        display_movies("All", movies)
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
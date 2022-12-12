from connect import *
from time import sleep
import datetime
from read import *

# Creates a function


def addFilm():
    # Creates an empty list to store the added film details. in and then add that into the database.
    films = []

    title = input(
        "\nPlease enter the title of the film you want to add or press 0 to exit: ")

    if title == "0":
        sleep(1)

    else:
        # This takes the user input and converts it into the Day-Month-Year format.
        yearReleasedInput = input(
            "Please enter the year of the release date of the film in DD-MM-YYYY format: ")
        yearReleased = datetime.datetime.strptime(
            yearReleasedInput, "%d-%m-%Y")
        yearReleased = yearReleased.strftime("%d-%m-%Y")

        rating = input("Please enter the rating of the film: ")

        # This takes the user input and converts it into the hour:minute:second format, then will pass it into the table as a string.
        durationInput = input(
            "Please enter the duration of the film in HH:MM:SS format: ")
        duration = datetime.datetime.strptime(durationInput, "%H:%M:%S")
        duration = duration.strftime("%H:%M:%S")

        genre = input("Please enter the genre of the film: ")

        # Appends the user inputs to the empty list.
        films.append(title)
        films.append(yearReleased)
        films.append(rating)
        films.append(duration)
        films.append(genre)

        # Insert the data from the films list into the table tblFilms
        cursor.execute("INSERT INTO tblfilms VALUES(NULL,?,?,?,?,?)", films)

        # Commits any pending transactions into the database.
        connect.commit()

        print(f"Film: {title} added to the films table.")

        sleep(1)


# This is used to check if this file is the one being run and not an import, and if it is the function is called.
if __name__ == "__main__":
    addFilm()

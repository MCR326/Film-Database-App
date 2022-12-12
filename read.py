from connect import *
from time import sleep

# Creates a function that returns


def readFilms():
    selection = 0
    while selection not in ["1", "2", "3", "4", "5"]:
        selection = input("\nWhat would you like to print?\n1. Print details of all films\n2.Print all films of a particular genre\n3.Print all films from a particular year\n4.Print all films of a particular rating\n5.Exit\nEnter: ")

        if selection not in ["1", "2", "3", "4", "5"]:
            print(f"{selection} is not a valid choice.")
            sleep(2)

        elif selection == "1":
            readAllFunc()
            sleep(1)

        elif selection == "2":
            genreFunc()
            sleep(1)

        elif selection == "3":
            yearFunc()
            sleep(1)

        elif selection == "4":
            ratingFunc()
            sleep(1)

        else:
            sleep(1)


def genreFunc():
    genreSelect = input("What genre of film would you like to select: ")
    #genreSelect = "'" + genreSelect + "'"
    cursor.execute(f"SELECT * FROM tblfilms WHERE genre = '{genreSelect}'")
    genreResult = cursor.fetchall()
    for record in genreResult:
        print(record)


def yearFunc():
    yearSelect = input("What year would you like to find films for: ")

    # I use the LIKE keyword with the % to find the films based on release year without having to put in the month and day as well.
    cursor.execute(
        f"SELECT * FROM tblfilms WHERE yearReleased LIKE '%{yearSelect}'")
    yearResult = cursor.fetchall()

    for record in yearResult:
        print(record)


def ratingFunc():
    ratingSelect = input("What rating would you like to find films for: ")

    cursor.execute(
        f"SELECT * FROM tblfilms WHERE rating LIKE '{ratingSelect}%'")
    ratingResult = cursor.fetchall()

    for record in ratingResult:
        print(record)


def readAllFunc():
    cursor.execute("SELECT * FROM tblfilms")
    # fetchall method fetches all the rows from the last executed statement.
    rows = cursor.fetchall()
    # prints every record in rows.
    for record in rows:
        print(record)


if __name__ == "__main__":
    readFilms()

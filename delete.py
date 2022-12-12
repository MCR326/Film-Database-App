from connect import *
from time import sleep
from read import readFilms

# I create a variable that is true or false so that the function will run whilst it is true but will exit once it is set to false.
# deleteLoop = True
# while deleteLoop == True:


def deleteFilm():
    idField = input(
        "\nEnter the id of the film to be deleted, or input 0 to exit: ")
    if idField == "0":
        sleep(1)

    else:
        # This fetches the title of the film that the user wants to delete using the inputted id and makes sure they want to delete it.
        cursor.execute(
            f"SELECT title FROM tblfilms WHERE filmID = {idField}")
        title = cursor.fetchall()
        delQuestion = input(
            f"Are you sure you want to delete {title}? Y/N: ")

        if delQuestion.upper() == "Y":
            cursor.execute(
                f"DELETE FROM tblfilms WHERE filmID = {idField}")

            connect.commit()
            print(f"Record {idField}, {title}, Deleted from the table.")

            sleep(1)

        elif delQuestion.upper() == "N":
            print("This record shall not be deleted.")
            sleep(2)
            deleteFilm()

        else:
            print("Please enter a valid value.")
            sleep(2)
            deleteFilm()


if __name__ == "__main__":
    deleteFilm()

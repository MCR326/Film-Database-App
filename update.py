from connect import *
from time import sleep
from read import readFilms


def updateFilm():

    idField = input(
        "\nPlease enter the ID of the film you want to update or press 0 to exit: ")

    if idField == "0":
        sleep(1)

    else:
        # This selects the title of the film using the inputted ID, and stores the title in the result variable using cursor.fetchall.
        cursor.execute(
            f"SELECT title FROM tblfilms WHERE filmID = {idField}")
        title = cursor.fetchall()

        fieldName = input(
            f"Which field do you want to update from record {idField}, {title}? Please enter the field as shown here. (title / yearReleased / rating / duration / genre): ")

        newFieldValue = input(
            f"What would you like the new value of {fieldName} in {title} to be: ")
        print(f"The new Field value is: {newFieldValue}")

        # The song table uses tuples, so you need to pass in the value in an acceptable data format by putting single quotation marks around it.
        newFieldValue = "'" + newFieldValue + "'"
        # Or you can just put the single quotes around newFieldValue, but since its being used multiple times here i'll leave it like this.
        print(f"The amended {fieldName} for {title} is: {newFieldValue}")

        cursor.execute(
            f"UPDATE tblfilms SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")
        connect.commit()

        sleep(1)


if __name__ == "__main__":
    updateFilm()

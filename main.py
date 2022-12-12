from read import readFilms, readAllFunc
from insert import addFilm
from delete import deleteFilm
from update import updateFilm
from time import sleep


def menuOptions():
    options = 0  # Giving a default value to the variable.
    while options not in ["1", "2", "3", "4", "5"]:
        print("\nFilm Menu Options\nEnter:\n1. To Print a selection of films.\n2. To Add a film.\n3. To Update a film.\n4. To Delete a film.\n5. To Exit")

        options = input("\nEnter any one of the options above: ")

        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice")

        return options


mainProgram = True  # flag variable
while mainProgram:
    # call the function and returns the input value ofd options to the main menu variable
    mainmMenu = menuOptions()
    if mainmMenu == "1":
        readFilms()  # call /invoke the readSongs subroutine from read file/app
        sleep(2)
    elif mainmMenu == "2":
        addFilm()
        sleep(2)
    elif mainmMenu == "3":
        readAllFunc()
        updateFilm()
        sleep(2)
    elif mainmMenu == "4":
        readAllFunc()
        deleteFilm()
        sleep(2)
    elif mainmMenu == "5":
        # reassign the value for the flag variable
        mainProgram = False

    else:
        sleep(2)
input("Press enter to exit")

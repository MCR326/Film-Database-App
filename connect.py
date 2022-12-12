import sqlite3 as sql

# Creates an object called connect that establishes a connection with the database file.
connect = sql.connect("filmflix.db")

# Creates a cursor object which is used to execute SQL commands and queries
cursor = connect.cursor()

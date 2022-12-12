from connect import *

cursor.execute(
    """

    CREATE TABLE "tblfilms" (
        "filmID" INTEGER NOT NULL UNIQUE,
        "title" TEXT,
        "yearReleased" TEXT,
        "rating" FLOAT,
        "duration" TEXT,
        "genre" TEXT,
        PRIMARY KEY("filmID" AUTOINCREMENT)
    )

    """
)

print("Table Created.")

import sqlite3
from sqlite3 import Connection

connection = sqlite3.connect("storage/database.db")


def getDB() -> Connection:
    return connection

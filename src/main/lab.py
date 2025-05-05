"""
This lab will explore establishing a database connection via Python and SQLite.
"""
import sqlite3


class Lab:

    # TODO: Complete the try block in connect_to_database(), returning a Database Connection object
    def connect_to_database(self):

        try:
            database = "test.db"
            print("Connecting to database...")
            conn = sqlite3.connect(database)
            #print("Connected to database")
            return conn
        except Exception as e:
            print(f"Failed to connect to database, with Exception: {e}")
            return None

# app.py
import sqlite3

from lab import Lab


def main():

    lab_instance = Lab()

    conn = lab_instance.connect_to_database()

    # If conn is type of Database Connection...
    if isinstance(conn, sqlite3.Connection):
        print(f"Database Connection Established: {conn}")
        conn.close()  # Clean up
    else:
        print("Failed to create database connection.")

if __name__ == "__main__":
    main()

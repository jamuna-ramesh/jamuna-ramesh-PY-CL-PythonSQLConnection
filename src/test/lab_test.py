import sqlite3
import unittest
from src.main.lab import Lab


class TestLab(unittest.TestCase):

    def test_connect_to_database(self):
        lab = Lab()

        conn = lab.connect_to_database()
        
        # Assert that the connection was successful
        self.assertTrue(isinstance(conn, sqlite3.Connection), "conn is not of type sqlite3.Connection.")

        # Clean up: close the connection
        conn.close()


if __name__ == "__main__":
    unittest.main()

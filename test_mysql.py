#!/usr/bin/python3

"""
Task:
Unit test for verifying the functionality of inserting a new record into the states table of a MySQL database.

All SQL keywords are in uppercase (SELECT, WHERE...)
"""

import unittest
import MySQLdb

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Connect to the test database
        self.connection = MySQLdb.connect(
            host="localhost",
            user="test_user",
            password="password",
            database="test_database"
        )
        self.cursor = self.connection.cursor()

    def tearDown(self):
        # Clean up by closing the database connection
        self.cursor.close()
        self.connection.close()

    def test_insert_state(self):
        # Get the initial record count
        self.cursor.execute("SELECT COUNT(*) FROM states")  # QUERY TO GET INITIAL RECORD COUNT
        initial_count = self.cursor.fetchone()[0]

        # Execute the console command (for example, a SQL query to insert a new state)
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")  # INSERTING A NEW STATE
        self.connection.commit()

        # Get the updated record count
        self.cursor.execute("SELECT COUNT(*) FROM states")  # QUERY TO GET UPDATED RECORD COUNT
        updated_count = self.cursor.fetchone()[0]

        # Assertion: Check if the difference is +1
        self.assertEqual(updated_count, initial_count + 1, "New record not inserted")

if __name__ == '__main__':
    unittest.main()


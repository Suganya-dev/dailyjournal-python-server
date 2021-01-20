import sqlite3
import json
from models import Moods

def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM moods m
        """)

        # Initialize an empty list to hold all entriy representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entriy instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entriy class above.
            mood = Moods(row['id'], row['label'])

            moods.append(mood.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(moods)
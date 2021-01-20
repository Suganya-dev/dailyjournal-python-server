import sqlite3
import json
from models import JournalEntries

def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.timestamp,
            e.moodsId
        FROM journalentry e
        """)

        # Initialize an empty list to hold all entriy representations
        journalentries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entriy instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entriy class above.
            journalentry = JournalEntries(row['id'], row['date'], row['concept'],
                            row['timestamp'], row['moodsId'])

            journalentries.append(journalentry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(journalentries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.timestamp,
            e.moodsId
        FROM journalentry e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        journalentry = JournalEntries(data['id'], data['date'], data['concept'],
                            data['timestamp'], data['moodsId'])

        return json.dumps(journalentry.__dict__)
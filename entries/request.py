import sqlite3
import json
from models import JournalEntries,Moods

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
            e.moodsId,
            m.label moods_label
        FROM journalentries e
        JOIN moods m
            ON m.id = e.moodsId
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

            # Create a mood instance from the current row
            mood = Moods(row['moodsId'], row['moods_label'])

             # Add the dictionary representation of the location to the animal
            journalentry.mood = mood.__dict__

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
            e.moodsId,
            m.label moods_label
        FROM journalentries e
        JOIN moods m
            ON m.id = e.moodsId
         WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        journalentry = JournalEntries(data['id'], data['date'], data['concept'],
                            data['timestamp'], data['moodsId'])

        # Create a mood instance from the current row
        mood = Moods(data['moodsId'], data['moods_label'])

        # Add the dictionary representation of the location to the animal
        journalentry.mood = mood.__dict__

    return json.dumps(journalentry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM journalentries
        WHERE id = ?
        """, (id, ))
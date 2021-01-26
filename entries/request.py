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
            e.entry,
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
                            row['entry'], row['moodsId'])

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
            e.entry,
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
                        data['entry'], data['moodsId'])

        # Create a mood instance from the current row
        mood = Moods(data['moodsId'], data['moods_label'])

        # Add the dictionary representation of the location to the animal
        journalentry.mood = mood.__dict__

    return json.dumps(journalentry.__dict__)

def get_entries_by_search(search_term):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.moodsId,
            m.label
        FROM JournalEntries e
        JOIN moods m
            ON m.id =  e.moodsId
        WHERE e.entry Like ?
        """, ("%" + search_term + "%"))

        journalentries=[]
        dataset= db_cursor.fetchall()
        
        # Create an animal instance from the current row
        for row in dataset:
            entries = JournalEntries(row['id'], row['date'], row['concept'],
                            row['entry'], row['moodsId'])
            journalentries.append(entries.__dict__)

    return json.dumps(journalentries)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM journalentries
        WHERE id = ?
        """, (id, ))

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO JournalEntries
            ( date,concept, timestamp, moodsId)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry["date"], new_entry["concept"],
              new_entry["timestamp"], new_entry["moodsId"], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry) 

def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE JournalEntries
            SET
                date = ?,
                concept = ?,
                timestamp = ?,
                moodsId = ?
        WHERE id = ?
        """, (new_entry['date'], new_entry['concept'],
              new_entry['timestamp'], new_entry['moodsId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
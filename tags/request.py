import sqlite3
import json
from models import Tags

def get_all_tags():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.name
        FROM tag t
        """)

        # Initialize an empty list to hold all entriy representations
        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entriy instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entriy class above.
            tag = Tags(row['id'], row['name'])

            tags.append(tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(tags)

def get_single_tag(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            t.id,
            t.name
        FROM tag t
        WHERE t.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        tag = Tags(data['id'], data['name'])

    return json.dumps(tag.__dict__)

def create_tag(new_tag):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tag
            (name)
        VALUES
            (?);
        """, (new_tag['name'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the tag dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_tag['id'] = id


    return json.dumps(new_tag) 
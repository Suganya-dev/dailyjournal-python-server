import sqlite3
import json
from models import Tags


def create_tag(new_tag):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( name)
        VALUES
            ( ?);
        """, (new_tag["name"], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the tag dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_tag['id'] = id


    return json.dumps(new_tag) 
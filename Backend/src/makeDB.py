import sqlite3
from nameData import *

db = sqlite3.connect("src/DB/LastNames__UK.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS names (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
)
;
""")
for name in LastNames__UK:
    db.execute("""

    INSERT INTO names (name) VALUES (:nameData)
    ;
    """, {"nameData" : name})

db.commit()
db.close()

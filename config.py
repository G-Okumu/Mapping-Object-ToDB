import sqlite3

CONN = sqlite3.connect('DB/inventory.sqlite3') # connecting to db
CURSOR = CONN.cursor()

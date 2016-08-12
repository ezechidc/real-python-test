import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE inventory(make TEXT, 
	            Model NUMERIC, Quantity INT)""")

conn.close()
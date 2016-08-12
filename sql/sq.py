import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE population SET population = 9000230 WHERE city='New York City'")
	cities = [
             ('Boston', 'MA', 600000),
             ('Chicago', 'IL', 2700000),
             ('Houston', 'TX', 2100000),
             ('Phoenix', 'AZ', 1500000)
             ]
c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
c.execute("SELECT * FROM population")
rows = c.fetchall()
for r in rows:
	print(r[0],r[1],r[2])
import sqlite3

with sqlite3.connect("cars.db") as connection:
   c = connection.cursor()

   car = [
           ('Ford', 'Ms52', 2006),
           ('Ford', 'as25', 2001),
           ('Honda', 'Ms52', 2006),
           ('Honda', 'as25', 2001),
   ]
c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', car)
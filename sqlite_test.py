import sqlite3

# conn = sqlite3.connect("bookings.db")

# conn.execute('''CREATE TABLE IF NOT EXISTS bookings
#              (email TEXT PRIMARY KEY NOT NULL,
#              time TEXT NOT NULL);
#              ''')

# conn.execute("INSERT INTO bookings (email,time) \
#              VALUES ('g.wiklander@gmail.com', '12-13-10:00')")

# conn.commit()

# conn.close()

conn = sqlite3.connect("bookings.db")

cursor = conn.execute("SELECT * FROM bookings")

for row in cursor:
    print("Email: ", row[0], "Time: ", row[1])

conn.close()
#code prototype

import re
import sqlite3

# conn = sqlite3.connect("bookings.db")
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS bookings
#              (email TEXT PRIMARY KEY NOT NULL,
#              time TEXT NOT NULL);
#              ''')
# conn.commit()
# conn.close()

def connect_db():
    return sqlite3.connect("bookings.db")

def show_all_bookings():
    conn = connect_db() #skapar uppkoppling till db
    cursor = conn.cursor() #skapar 'pekar'-objekt
    cursor.execute("SELECT time FROM bookings") #'pekar' på alla tider i db-tabell 
    bookings = cursor.fetchall() #variablen 'bookings' innehåller nu en lista med tider
    if len(bookings) == 0:
        print("Det finns inga tider bokade.")
    else:
        print("Följande tider är bokade:")
        for booking in bookings:
            print(booking[0])
    cursor.close()
    conn.close()

def show_my_bookings():
    email = input("Ange epost: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT time FROM bookings WHERE email = ?", (email,))
    bookings = cursor.fetchall()
    if len(bookings) > 0:
        print("Du har följande bokningar:")
        for booking in bookings:
            print(booking[0])
    else:
        print("Du har inga bokningar.")
    cursor.close()
    conn.close()

def time_is_occupied(time):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT time FROM bookings WHERE time = ?", (time,)) 
    booking = cursor.fetchall()
    if len(booking) > 0:
        cursor.close()
        conn.close()
        return True
    else:
        cursor.close()
        conn.close()
        return False

def validate_time(time):
    if re.match(r"^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-(0\d|1\d|2[0-3]):00$", time):
        return True
    else:
        return False
    
def validate_email(email):
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return True
    else:
        return False

def add_booking():
    while True:
        time = input("Vilken tid önskar du boka? Ange på följande format: mm-dd-HH:MM")
        if not validate_time(time):
            print("Ogiltigt format. Ange: mm-dd-HH:MM")
            continue
        if time_is_occupied(time):
            print("Tiden redan bokad.")
            continue
        break
    while True:
        email = input("Ange e-post för bokningen: ")
        if not validate_email(email):
            print("Felaktigt format. Ange e-post på nytt.")
            continue
        break
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (email, time) VALUES (?, ?)", (email, time))
    conn.commit()
    cursor.close()
    conn.close()
    print("Tiden är bokad!")

def delete_booking():
    email = input("Ange epost för bokningen:")
    time = input("Ange tidpunkt för bokningen:")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE email = ? AND time = ?", (email, time))
    conn.commit()
    if cursor.rowcount == 0:
        print("Du har inga bokningar att ta bort.")
    else:
        print("Din bokning är nu borttagen.")
    cursor.close()
    conn.close()
        
def menu_text():
    print("Visa alla bokningar - tryck 'S'")
    print("Visa dina bokningar - tryck 'M'")
    print("Boka - tryck 'A'")
    print("Avboka - tryck 'D'")
    print("Avsluta - tryck 'E'")
    choice = input().upper()
    return choice

def menu():
    choice = menu_text() 
    while True:
        if choice == "S":
            show_all_bookings()
        elif choice == "M":
            show_my_bookings()
        elif choice == "A":
            add_booking()
        elif choice == "D":
            delete_booking()
        elif choice == "E":
            break
        else:
            print("Felaktigt val.")
        choice = menu_text() 

def main():
    menu()

main()
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
    cursor = connect_db()
    bookings = cursor.execute(SELECT time FROM bookings)
    for row in bookings:
        if row[0] == time:
            return True
    return False

def validate_time(time):
    if re.match("^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-(0\d|1\d|2[0-3]):00$", time):
        return True
    else:
        return False

def add_booking():
    while True:
        time = input("Vilken tid önskar du boka? mm-dd-HH:MM")
        if not validate_time(time):
            print("Ogiltigt format.")
            continue
        if time_is_occupied(time):
            print("Tiden redan bokad.")
            continue
        email = input("Ange e-post för bokningen.")
        cursor = connect_db()
        cursor.execute("INSERT email, time TO bookings")
        print("Tiden är bokad!")
        break

def delete_booking():
    email = input("Ange epost för bokningen:")
    time = input("Ange tidpunkt för bokningen:")
    cursor = connect_db()
    cursor.execute(DELETE FROM bookings WHERE email = ? AND time = ?, (email, time))
    cursor.commit()
    if len(cursor) == 0:
        print("Du har inga bokningar att ta bort.")
    else:
        print("Din bokning är nu borttagen.")
        
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
#code prototype

import re
import sqlite3

conn = sqlite3.connect("bookings.db")
conn.execute('''CREATE TABLE IF NOT EXISTS bookings
             (email TEXT PRIMARY KEY NOT NULL,
             time TEXT NOT NULL);
             ''')
conn.commit()
conn.close()

class Booking:

    def __init__(self, time, email):
        self.time = time
        self.email = email
    
    def __str__(self):
        return self.time

class Repository:

    def __init__(self):
        self.bookings = []
    
    def __lt__(self, other):
        if self.time < other.time:
            return True
        else:
            return False
    
    def show_all_bookings(self):
        print("Föjande tider är bokade:")
        for booking in self.bookings:
            print(booking)
    
    def show_my_bookings(self):
        email = input("Ange epost.")
        print("Du har följande bokningar:")
        for booking in self.bookings:
            if booking.email == email:
                print (booking)
    
    def time_is_occupied(self, time):
        for booking in self.bookings:
            if booking.time == time:
                return True
        return False
    
    def validate_time(self, time):
        if re.match("^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-(0\d|1\d|2[0-3]):00$", time):
            return True
        else:
            return False
    
    def add_booking(self):
        while True:
            time = input("Vilken tid önskar du boka? mm-dd-HH:MM")
            if not self.validate_time(time):
                print("Ogiltigt format.")
                continue
            if self.time_is_occupied(time):
                print("Tiden redan bokad.")
                continue
            email = input("Ange e-post för bokningen.")
            self.bookings.append(Booking(time, email))
            print("Tiden är bokad!")
            break
    
    def delete_booking(self):
        email = input("Ange epost för bokningen:")
        time = input("Ange tidpunkt för bokningen:")
        for booking in self.bookings:
            if booking.email == email and booking.time == time:
                self.bookings.remove(booking)
                print("Din bokning", booking.time, "är nu borttagen.")
            else:
                print("Du har inga bokningar att ta bort.")

def menu_text():
    print("Visa alla bokningar - tryck 'S'")
    print("Visa dina bokningar - tryck 'M'")
    print("Boka - tryck 'A'")
    print("Avboka - tryck 'D'")
    print("Avsluta - tryck 'E'")
    choice = input().upper()
    return choice

def menu(repository):
    choice = menu_text() 
    while True:
        if choice == "S":
            repository.show_all_bookings()
        elif choice == "M":
            repository.show_my_bookings()
        elif choice == "A":
            repository.add_booking()
        elif choice == "D":
            repository.delete_booking()
        elif choice == "E":
            break
        else:
            print("Felaktigt val.")
        choice = menu_text() 

def read_file(repository):
    try:
        with open('bookings.txt', 'r', encoding = 'utf-8') as file:
            time = file.readline().strip()
            while time != "":
                email = file.readline().strip()
                repository.bookings.append(Booking(time, email))
                time = file.readline().strip()
    except FileNotFoundError:
        print("Ingen fil hittades. Start med ny fil.")

def write_file(repository):
    with open('bookings.txt.', 'w', encoding = 'utf-8') as file:
        repository.bookings.sort()
        for booking in repository.bookings:
            file.write(booking.time + "\n")
            file.write(booking.email + "\n")

def main():
    repository = Repository()
    read_file(repository)
    menu(repository)
    write_file(repository)

main()
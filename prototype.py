#code prototyp

class Booking:

    def __init__(self, time, email):
        self.time = time
        self.email = email

class Repository:

    def __init__(self):
        self.bookings = []
    
    def __str__(self):
        return self.time
    
    def __lt__(self, other):
        if self < other:
            return True
        else:
            return False
    
    def show_bookings(self):
        for booking in self.bookings:
            print(booking)
    
    def add_booking(self):
        time = input("Vilken tid önskar du boka?")
        email = input("Ange e-post för bokningen.")
        

'''Algorithm:
1. Read file
2. Present meny
3. Save to file'''
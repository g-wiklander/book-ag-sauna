from flask import Flask, render_template
from prototype import show_all_bookings
app = Flask(__name__)

@app.route("/")
def welcome_to_page():
    return "Välkommen till bokningssidan!"

@app.route("/show_all_bookings", methods=["GET"])
def display_bookings():
    bookings = show_all_bookings()  # Anta att denna funktion returnerar data snarare än att printa direkt
    return render_template("show_all_bookings.html", bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)


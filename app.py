from flask import Flask, render_template
from prototype import show_all_bookings
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book")
def book():
    return "Här kommer bokningsformuläret att visas."

@app.route("/my_bookings")
def my_bookings():
    return "Här kommer användarens bokningar att visas."

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/show_all_bookings", methods=["GET"])
def display_bookings():
    bookings = show_all_bookings()  # Anta att denna funktion returnerar data snarare än att printa direkt
    return render_template("show_all_bookings.html", bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)


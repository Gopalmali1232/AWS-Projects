from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# DB connection (for now local, later RDS)
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="busdb"
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    source = request.form['source']
    destination = request.form['destination']

    cursor = db.cursor()
    cursor.execute("SELECT * FROM buses WHERE source=%s AND destination=%s", (source, destination))
    buses = cursor.fetchall()

    return render_template("search.html", buses=buses)

@app.route('/book/<int:bus_id>')
def book(bus_id):
    cursor = db.cursor()
    cursor.execute("INSERT INTO bookings (user_id, bus_id, seat_no) VALUES (1, %s, 1)", (bus_id,))
    db.commit()
    return "Booking Successful!"

if __name__ == '__main__':
    app.run(debug=True)
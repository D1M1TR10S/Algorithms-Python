from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)

slots = {}

@app.route("/trips/timeOpenings", methods=['GET'])
'''
    Returns a list of all available timeOpenings for the current week.
'''
def openings():
    now = datetime.datetime.now()
    '''Getting datetime of GET request'''
    hour = now.hour
    day = now.day
    year = now.year
    month = now.month
    week = now.week
    ride = now
    while 1:
        slots[ride] = True
        ride = datetime.datetime.now() + datetime.timedelta(hours=1)
        ride = ride.replace(minute=10)
    return jsonify({
                
            })

@app.route("/trips/requests", methods=['POST'])
'''
    Creates a trip request for a time opening, mode, and time range.
'''
def create():

@app.route("/trips/requests/:requestId", methods=['PUT'])
'''
    Modifies a request to cancel or delete. Must be before deadline.
'''
def change():


if __name__ == '__main__':
    app.run(debug=True)

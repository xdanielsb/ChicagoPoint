"""This module control the application."""

from flask import Flask, render_template, jsonify
from request import *

app = Flask(__name__)

"""
    Create no heavy request at the init of the application
"""

request_object = Request()


@app.route('/')
def browser ():
    return render_template('browser.html')

@app.route('/about/')
def index():
    return render_template('about.html')

@app.route('/content/')
def content():
    return render_template('content.html')

@app.route('/charts/')
def charts():
    return render_template('charts.html')



"""
    Methods for the custom API
"""

@app.route('/location_houses/')
def location_houses():
    locs = request_object.get_locations_houses()
    return locs

@app.route('/health/')
def health():
    return jsonify(request_object.health_data)

@app.route("/weather/")
def weather():
    weather_data = request_object.get_weather()
    return jsonify(weather_data)


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

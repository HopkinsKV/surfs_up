# Imports
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create engine to access SQLite db
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the db into our classes
Base = automap_base()
# Reflect the db
Base.prepare(engine, reflect=True)
# Create a variable for each class
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link 
session = Session(engine)

# New instance of flask called app
app = Flask(__name__)
# Define welcome route
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Define /precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    ## Calculate a year as date 8/23/17 to one year before
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    ## Query date and precip for prev_year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    ## Jsonify it
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Define /stations
@app.route("/api/v1.0/stations")
def stations():    
    ## Get all stations
    results = session.query(Station.station).all()
    ## unravel results into 1D array, convert to list, jsonify it
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Define Monthly Temp Obs
@app.route("/api/v1.0/tobs")
def temp_monthly():
    ## Calculate a year as date 8/23/17 to one year before
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    ## Query chosen station for all tobs last year
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Define Statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
## Add params to stats function
def stats(start=None, end=None):
    ##Select min/avg/max temp from db
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
   
    ## Determine starting and ending date - query db with prior list
    ## *sel shows there will be multiple results for query
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    ## Get statistics data
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
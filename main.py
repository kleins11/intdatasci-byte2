# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib

# this is used for constructing URLs to google's APIS
from googleapiclient.discovery import build

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
service = build('fusiontables', 'v1', developerKey=API_KEY)

# This is where I am attempting to load the API_KEY 
API_KEY = AIzaSyCQELPFTPR3k_SYv23WYGk0H6igFs2U5j0

# This is where I am attempting to load TABLE_ID
TABLE_ID = 1OVBDhPToqLcxTOiKb8LEUut1slvx6-2pdFlOY_Qc

# This is where I am attempting to load the response ID 
request = service.column().list(tableId=TABLE_ID)

# This is where I am define get_all_data() as per that dude on piazza's advice.
# I'm doing this because I couldn't run get all data self in the command line.  
def get_all_data():
    query = "SELECT * FROM " + TABLE_ID + " WHERE  Educational Atainment = 'No high school diploma' LIMIT 2"
    response = service.query().sql(sql=query).execute()
    logging.info(response['columns'])
    logging.info(response['rows'])
        
    return response

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def index():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    get_all_data()
    return template.render()
def hello():
    template =
JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

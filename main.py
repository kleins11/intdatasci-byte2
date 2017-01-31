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
def hello():
    template =
JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

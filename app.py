import os
from flask import Flask 
from pymongo import MongoClient, uri_parser

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

# Database
#client = MongoClient

@app.route('/')
def index():
	return "<h1>Hello World</h1>"

if __name__ == '__main__':
	app.run(debug=True)

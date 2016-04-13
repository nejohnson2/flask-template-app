import os
from flask import Flask 
from pymongo import MongoClient, uri_parser

app = Flask(__name__)

# Configuration
app.config.from_object(os.environ['APP_SETTINGS'])

# Database
parser = uri_parser.parse_uri(app.config['MONGODB_URI'])
db = MongoClient(app.config['MONGODB_URI'])[parser['database']]

@app.route('/')
def index():
	return "<h1>Hello World</h1>"

if __name__ == '__main__':
	app.run(debug=True)

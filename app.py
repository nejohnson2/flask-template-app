from __future__ import print_function # In python 2.7
import os, sys, json
from flask import Flask, request, Response
from pymongo import MongoClient, uri_parser

app = Flask(__name__)

# Configuration
app.config.from_object(os.environ['APP_SETTINGS'])
print(app.config, file=sys.stderr)
# Database
try:
	parser = uri_parser.parse_uri(app.config['MONGODB_URI'])
	db = MongoClient(app.config['MONGODB_URI'])[parser['database']]
	print("Successfully connected to database...", file=sys.stderr)
except:
	print('Failed to connect to MongoDB', file=sys.stderr)

@app.route('/')
def index():
	return "<h1>Hello World</h1>"

@app.route('/data', methods=["GET","POST"])
def read_data():
	if request.method == "POST":
		data = request.get_json()
		db.things.insert(data)

		resp = Response(status=200)
		return resp

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)

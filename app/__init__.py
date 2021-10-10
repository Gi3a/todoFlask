import os
import sys
import sqlalchemy
from flask import Flask
from yaml import load, Loader

def init_connect_engine():
	pool = sqlalchemy.create_engine(
		sqlalchemy.engine.url.URL(
			drivername="mysql+pymysql",
			username='root',
			password='',
			database='todo',
			host='localhost'
		)
	)

	return pool

app = Flask(__name__)
db = init_connect_engine()

from app import routes

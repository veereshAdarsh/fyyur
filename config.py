import os
from flask_sqlalchemy import SQLAlchemy
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = 'postgresql://Veeresh.Patil:patil@localhost:5000/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# TODO IMPLEMENT DATABASE URL

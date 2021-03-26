from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

# Configurations
app.config.from_object('config')

# Set the database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import models for DB schema creation
from .models.champion import Champion

# Build the database:
# This will create the database file using SQLAlchemy, necessary for views
db.create_all()

from .views.champions import champions_api

# Register blueprint(s)
app.register_blueprint(champions_api)

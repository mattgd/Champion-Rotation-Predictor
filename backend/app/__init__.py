from flask import Flask
from flask_cors import CORS
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

# Add CORS headers
CORS(app)

# Import models for DB schema creation
from .models.rotation import Rotation
from .models.champion import Champion

# Build the database:
# This will create the database file using SQLAlchemy, necessary for views
db.create_all()

from .views.champions import champions_api
from .views.rotations import rotations_api

# Register blueprint(s)
app.register_blueprint(champions_api)
app.register_blueprint(rotations_api)

# Scaper CLI command
@app.cli.command("scrape-data")
def scape_data():
    from .scraper import scraper
    scraper.scrape_champions()
    scraper.scrape_rotations()

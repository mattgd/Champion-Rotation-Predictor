import sqlite3

from flask import Flask, g, jsonify

app = Flask(__name__)


CHAMPION_SQUARE_IMAGE_URL_PREFIX = 'https://ddragon.leagueoflegends.com/cdn/5.15.1/img/champion/'
CHAMPION_TALL_IMAGE_URL_PREFIX = 'https://ddragon.leagueoflegends.com/cdn/img/champion/loading/'
DATABASE = 'database.db'


def get_db():
    """
    Gets the SQLite database from the global context.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    # Makes the db return Row objects (easier to work with)
    db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    """
    Populate database with initial schema.
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    """
    Closes the databaase connection on app teardown.
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return 'It works!'

@app.route('/champions')
def get_champions():
    parsed_champions = []
    for champion in query_db('SELECT * FROM champions'):
        key = champion['key']
        parsed_champions.append({
            'id': champion['id'],
            'name': champion['name'],
            'key': key,
            'squareImage': '{prefix}{key}.png'.format(prefix=CHAMPION_SQUARE_IMAGE_URL_PREFIX, key=key),
            'tallImage': '{prefix}{key}_0.jpg'.format(prefix=CHAMPION_TALL_IMAGE_URL_PREFIX, key=key)
        })
        
    return jsonify(parsed_champions)

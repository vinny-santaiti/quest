from flask import Flask
from SQLAlchemy
app = Flask(__name__)

app.config['DEBUG'] = True
POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
    }
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db=SQLAlchemy(app)

@app.route('/<name>')
def index(name):
    return 'Hello, {}!'.format('name')

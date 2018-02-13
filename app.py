from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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
    
db = SQLAlchemy(app)

@app.route('/<name>')
@app.route('/')
def index(name):
	return render_template('index.html', name=name)
    # return 'Hello, {}!'.format('name')

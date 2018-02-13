#__init__.py

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('../config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #silence deprecation warnings

db = SQLAlchemy(app)

from app import views
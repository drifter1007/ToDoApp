from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, jsonify
from os import sys, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Connecting Flask App  & SQLalchemy Database(POSTGRES)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sunny:123456@localhost:5432/testing'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating DataBase Table 'Todos'(Class) using sqlalchemy class Model Method
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    #completed = db.Column(db.Boolean,nullable = False , default=False)

# Creating repr for the  table 'todos'.


def __repr__(self):
    return '<Todo: %s%s>', ('self.id', 'self.description')


# Creating controller for the  index page
@app.route('/')
def index():
    return render_template('index.html', todos=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }])

from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, jsonify
from os import sys, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sunny:123456@localhost:5432/testing'
db = SQLAlchemy(app)

migrate = Migrate(app, db)


app = Flask(__name__)


class Todo(db.Model){
    __tablename__ = 'todos'
    id = db.Column(db.Integer primary_key=True)
    description = db.Column(db.String(), nullable=False)
    #completed = db.Column(db.Boolean,nullable = False , default=False)
}


def __repr__(self):
    return '<Todo: %s%s' >, ('self.id', 'self.description')


@app.route('/')
def index():
    return render_template('index.html', todos=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }])

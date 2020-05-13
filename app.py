from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import sys
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
    completed = db.Column(db.Boolean, nullable=False, default=False)


# Creating repr for the  table 'todos'.
def __repr__(self):
    return '<Todo: %s%s>', ('self.id', 'self.description')


# Controller  for MVC  model
# Creating controller for creating data or element in todos .
@app.route('/todos/create', methods=['POST'])
def create_todo():
    """
    # Normal way of using controller--------------------------------------------------------------------------------------------
    # Old traditional request methodss
    #    description = request.form.get('description', ' ')
    description = request.get_json()['description']
    #                                            / |\ using dictionary which have key decription in it
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    # return redirect(url_for('index'))
    return jsonify({
        'description': todo.description
    })
    # ---------------------------------------------------------------------------------------------------------------------------------
    """
    # USING SESSION IN CONTROLLERS ( try, except ,finally )
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        #                                       / |\ using dictionary which have key decription in it
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        # return jsonify({
        # 'description': todo.description
        # })
        return jsonify(body)

# Creating controller for the  index page
@app.route('/')
def index():
    return render_template('index.html', todos=Todo.query.all())

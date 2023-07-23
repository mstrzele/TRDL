from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
if app.testing:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{__name__}.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'
app.config.from_prefixed_env()

db = SQLAlchemy(app)


@app.route('/healthz')
def healhtz():
    return '', 200


class Value(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.cli.command('init-db')
@with_appcontext
def init_db():
    db.drop_all()
    db.create_all()

    value = Value()
    value.id = 42

    db.session.add(value)
    db.session.commit()


@app.route('/value')
def value():
    value = db.first_or_404(db.select(Value))
    return f'{value.id}'

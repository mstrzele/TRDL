from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'
app.config.from_prefixed_env()

db = SQLAlchemy(app)


@app.route('/healthz')
def healhtz():
    """Indicate the current status of the application.

    >>> healthz()
    ('', 200)
    """
    return '', 200


class Value(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.cli.command('init-db')
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        value = Value()
        value.id = 42

        db.session.add(value)
        db.session.commit()


@app.route('/value')
def value():
    """Return the value.

    >>> value()
    42
    """
    value = db.first_or_404(db.select(Value))
    return f'{value.id}'

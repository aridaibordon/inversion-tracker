import flask

from flaskapp import app

from scripts.database import return_degiro_balance_old

@app.route('/')
def home():
    balance, labels = return_degiro_balance_old(30)
    return flask.render_template('index.html', labels=labels, balance=balance)
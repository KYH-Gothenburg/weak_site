from flask import Flask, render_template
import random
import sqlite3
import hashlib

app = Flask(__name__)
app.database = "database.db"

@app.route('/')
def index():

    return render_template('index.html', name=random.randint(10, 100))

@app.route('/hepp')
def hepp():
    return '<h1>This is my other page. Hepp</h1>'


def connect_to_db():
    return sqlite3.connect(app.database)


def hash_pass(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()

def create_data():
    with connect_to_db() as connection:
        c = connection.cursor()

        c.execute("""CREATE TABLE shop_items(name TEXT, quantity TEXT, price TEXT)""")
        c.execute("""CREATE TABLE users(username TEXT, password TEXT)""")

        c.execute('INSERT INTO shop_items VALUES("water", "40", "100")')
        c.execute('INSERT INTO shop_items VALUES("juice", "34", "110")')
        c.execute('INSERT INTO shop_items VALUES("candy", "140", "10")')

        c.execute('INSERT INTO users VALUES("bob123", "{}")'.format(hash_pass('badword')))
        c.execute('INSERT INTO users VALUES("lisa45", "{}")'.format(hash_pass('badpassword')))
        c.execute('INSERT INTO users VALUES("alice77", "{}")'.format(hash_pass('pass123')))

        connection.commit()


if __name__ == '__main__':
    create_data()
    app.run()
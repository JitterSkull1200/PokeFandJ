from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysqltestfandj.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'saFandJ'
app.config['MYSQL_PASSWORD'] = 'Step2024'
app.config['MYSQL_DB'] = 'PokeFandJ'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Poke')
    data = cur.fetchall()
    return render_template('index.html', pokemon = data)

if __name__ == '__main__':
    app.run(port=3000,debug=True)
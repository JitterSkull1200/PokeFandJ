from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysqltestfandj.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'saFandJ'
app.config['MYSQL_PASSWORD'] = 'Step2024'
app.config['MYSQL_DB'] = 'PokeFandJ'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Poke')
    data = cur.fetchall()
    return render_template('index.html', pokemon = data)


@app.route('/new', methods=['GET','POST'])
def add_poke():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Poke (name, type) VALUES(%s, %s)',(name,type))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    return render_template('newpoke.html')
    

if __name__ == '__main__':
    app.run(port=3000,debug=True)
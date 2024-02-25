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
    cur.execute('''
    select
	Id,
	Name,
	TypeId,
	RegionId,
	Imagen,
    Biology,
    Etymology,
    Male,
    Female
    from Pokemon''')
    data = cur.fetchall()
    return render_template('index.html', pokemon = data)


@app.route('/new', methods=['GET','POST'])
def add_poke():
    if request.method == 'POST':
        id = request.form['Id']
        name = request.form['Name']
        type = request.form['TypeId']
        region = request.form['RegionId']
        imagen = request.form['Imagen']
        biology = request.form['Biology']
        etymology = request.form['Etymology']
        male = request.form['Male']
        female = request.form['Female']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Pokemon (Id, Name, TypeId, RegionId, Imagen, Biology, Etymology, Male, Female) VALUES(%i, %s,%i,%i,%b,%s,%s,%b,%b)',(id,name,type,region,imagen,biology,etymology,male,female))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    return render_template('newpoke.html')
    

if __name__ == '__main__':
    app.run(port=3000,debug=True)
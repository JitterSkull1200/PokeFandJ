from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import pathlib


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysqltestfandj.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'saFandJ'
app.config['MYSQL_PASSWORD'] = 'Step2024'
app.config['MYSQL_DB'] = 'PokeFandJ'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('newpoke.html')


@app.route('/hello')
def Home():
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
    print("Ya no puedo!")
    if request.method == 'POST':
        id = request.form['Id']
        name = request.form['Name']
        type = request.form['TypeId']
        region = request.form['RegionId']
        image = request.form['Imagen']
        biology = request.form['Biology']
        etymology = request.form['Etymology']
        male = request.form['Male']
        female = request.form['Female']
        print("Holaaaaa!")
        pic1 = convertToBinary(image)
        pic2 = convertToBinary(male)
        pic3 = convertToBinary(female)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Pokemon (Id, Name, TypeId, RegionId, Imagen, Biology, Etymology, Male, Female) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)',(id,name,type,region,pic1,biology,etymology,pic2,pic3))
        mysql.connection.commit()
    return redirect(url_for('Index'))

    
@app.route("/upload_file", methods=["GET","POST"])
def upload_file():
    return render_template('newpoke.html')

def convertToBinary(filename):
    with open(filename,"rb") as file:
        binaryData = file.read()
    return binaryData

def convertBinaryToFile(binarydata, filename):
    with open(filename, "wb") as file:
        file.write(binarydata)


if __name__ == '__main__':
    app.run(port=3000,debug=True)
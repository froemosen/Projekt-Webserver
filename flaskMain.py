from flask import Flask, render_template, request
import sqlite3 as sql
from getData import GetData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/new_student')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            
            with sql.connect("fakedatabase.db") as con:
                cur = con.cursor()
                
                
                
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                
                con.commit()
                msg = "Record successfully added"
        except Exception as noUpload:
            print(noUpload)    
            try: con.execute("CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT);")
            except Exception as noTableCreated: print(noTableCreated)
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            con.close()
            return render_template("result.html",msg = msg)
            

@app.route('/list')
def list():
    con = sql.connect("fakedatabase.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)


@app.route("/deathsPerInfected")
def deathsPerInfected():
    print("Getting deaths per infected...")
    deaths = GetData.deaths()
    infected = GetData.infected() 
    y = 
    return render_template("plotGraph.html", x=x, y=y)


@app.route("/rawData")
def rawData():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Covid")
    
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)


if __name__ == '__main__':    
    app.run(debug = True)

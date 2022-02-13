from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
from getData import GetData
import matplotlib.pyplot as plt
import numpy as np

#Example plot
plt.plot([0], [0])
plt.xlabel('Dates')
plt.ylabel('YOUR CHOSEN DATA')
plt.savefig('static/graph.png')

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


@app.route("/deathsPerInfected", methods = ['POST', 'GET'])
def deathsPerInfected():
    print("Getting deaths per infected...")
    #countries = GetData.countries()
    countries = ("Danmark", "Tyskland", "Bosnien")
    
    #deaths = GetData.deaths()
    #infected = GetData.infected() 
    
    #y = 
    return render_template("plotGraph.html", graphType = "deathsPerInfected", countries = countries)

@app.route("/createGraph-deathsPerInfected", methods = ['POST', 'GET'])
def plotGraph():
    if request.method=="POST":
        countries = request.form.getlist("country")
        print(countries)
        row = 0
        fig, axs = plt.subplots(len(countries))
        for country in countries:
            #dates = GetData.dates(country)
            #deaths = GetData.deaths(country)
            #infected = GetData.infected(country)
            dates = ["12/02-2020", "13/02-2020", "14/02-2020", "15/02-2020"]
            deaths = [2, 5, 6, 8]
            infected = [100, 615, 161, 1651]
            values = [i / j for i, j in zip(deaths, infected)]
            print(values)
            
            
            axs[row].plot(dates, values)
            axs[row].set_title(country)
            #plt.subplot(len(countries), 1, row)
            #plt.plot(dates, values)
            #plt.title(country)
            #plt.xlabel('Dates')
            #plt.ylabel('Deaths per infected')
            row += 1
        fig.tight_layout()
        plt.savefig('static/graph.png')
        
        return redirect(url_for('deathsPerInfected'))
        
                


@app.route("/rawData")
def rawData():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Covid")
    
    rows = cur.fetchall();
    return render_template("rawData.html",rows = rows)


if __name__ == '__main__':    
    app.run(debug = True)

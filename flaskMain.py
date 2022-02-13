from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
from getData import GetData
import matplotlib.pyplot as plt


#Example plot, Starter med blank plot når hjemmesiden startes.
plt.plot([0], [0])
plt.xlabel('Dates')
plt.ylabel('YOUR CHOSEN DATA')
plt.savefig('static/graph.png')

app = Flask(__name__)

@app.route('/') #Viser home-page
def home():
    return render_template('Home.html')

@app.route('/test') #Viser testside (ligegyldig)
def test():
    return render_template('test.html')

@app.route('/new_student') #Til at indtaste data i fakedatabase.db
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST']) #Bruges til at opdatere vores fakedatabase.db
def addrec():
    if request.method == 'POST':
        try:
            #Hent indtastet data
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            
            with sql.connect("fakedatabase.db") as con: #Gem indtastet data
                cur = con.cursor()                
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                
                con.commit()
                msg = "Record successfully added"
        except Exception as noUpload: #Hvis tabel ikke eksisterer
            print(noUpload)    
            try: con.execute("CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT);")
            except Exception as noTableCreated: print(noTableCreated) #Tabel kunne ikke laves.
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            con.close()
            return render_template("result.html",msg = msg)
            

@app.route('/list') #Viser data fra "falsk" database
def list():
    con = sql.connect("fakedatabase.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)


@app.route("/deathsPerInfected") #Siger til plotGraph at det er denne type graf vi skal have.
def deathsPerInfected():
    print("Getting deaths per infected...")
    countries = GetData().countries() #Liste med alle registrerede lande.
    return render_template("plotGraph.html", graphType = "deathsPerInfected", countries = countries)

@app.route("/createGraph-deathsPerInfected", methods = ['POST'])
def plotGraph():
    if request.method=="POST":
        countries = request.form.getlist("country") #Skaffer de "tjekkede" lande på siden som liste.
        print(countries)
        row = 0
        fig, axs = plt.subplots(len(countries)) #Et subplot per land
        for country in countries:
            dates = GetData().dates(country)
            deaths = GetData().deaths(country)
            infected = GetData().infected(country)
            
            #Data er reversed, så her rettes det til rigtig rækkefølge. 
            dates.reverse()
            deaths.reverse()
            infected.reverse()
        
            
            for item in range(len(infected)): #Division by 0 eller nonetype errors
                if infected[item] == 0 or infected[item] == None:
                    infected[item] = 0.000001 
                    
            for item in range(len(deaths)): #nonetype errors
                if deaths[item] == None:
                    deaths[item] = 0.000001 
            
            values = []
            for i in range(len(deaths)): #Dividerer alle dødstal med alle smittetal
                values.append(deaths[i]/infected[i])
            print(values)
            
            for i in range(len(values)): #Forbehold til mærkelig data
                if values[i] > 0.1:
                    values[i] = 0.1
                if values[i] < 0:
                    values[i] = 0
        
                        
            axs[row].plot(dates, values)
            axs[row].set_title(country)
        
            row += 1
        
        fig.tight_layout() #Layout af grafer
        plt.savefig('static/graph.png') #Gemmer graf som png
        
        return redirect(url_for('deathsPerInfected')) #Tilbage til side med deathsPerInfected med nyt png-plot
        
                


@app.route("/rawData") #Viser rå covid-data fra database.db
def rawData():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from Covid")
    
    rows = cur.fetchall();
    return render_template("rawData.html",rows = rows)


if __name__ == '__main__':    
    app.run(debug = True)

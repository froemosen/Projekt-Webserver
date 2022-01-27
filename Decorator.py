from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            
            with sql.connect("database.db") as con:
                cur = con.cursor()
                
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug = True)

"""
from flask import Flask, render_template, request
import sqlite3

#Opret database (Load database)
conn = sqlite3.connect('database.db')
print("Opened database successfully")
""""""
#INDSÆT DATA
conn.execute("INSERT INTO student (navn,addr,city,pin) \
      VALUES ('John', 'Johnnygade 31', 'Havnen', '27 damer pinned')");
conn.commit()
conn.close()

conn = sqlite3.connect('database.db')""""""
#LÆS DATA OG PRINT
cursor = conn.execute("SELECT navn, addr, city, pin from student")
conn.execute("")
for row in cursor:
   print("navn = ", row[0])
   print("addr = ", row[1])
   print("city = ", row[2])
   print("pin =", row[3], "\n")

print("Operation done successfully");

#conn.execute("CREATE TABLE student (navn TEXT, addr TEXT, city TEXT, pin TEXT);")
#print("Table created successfully")
conn.close()

         


app = Flask(__name__)

@app.route("/")   #<---DEN HER LINIE ER EN DECORATOR
def home():
    return render_template('Home.html')

@app.route("/test")
def test():
    return render_template("test.html", msg = "YEAAAAAH!")

@app.route('/student')
def new_student():
   return render_template('student.html')


@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            return render_template("result.html",msg = msg)
            con.close()
            


if __name__ == '__main__':
   app.run(debug = True)

"""
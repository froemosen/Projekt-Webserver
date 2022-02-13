import pandas as pd
import sqlite3 as sql

#Laver dataframe
df = pd.read_csv("SmittedeDødeData.csv")

#sortere datoer, smittetal, døde og lande fra og putter det ind i lister
dates = df["dateRep"]
cases = df["cases"]
deaths = df["deaths"]
country = df["countriesAndTerritories"]

#Indsætter dataene ind i databasen
for i in range(22173):
    d = dates[i]
    c = cases[i]
    dea = deaths[i]
    cou = country[i]
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Covid (Land, Smittede, Doede, Date) VALUES(?,?,?,?)", (cou, c, dea, d))
        con.commit()
    con.close()
    print(d)
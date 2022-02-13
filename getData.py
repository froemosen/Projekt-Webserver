import sqlite3 as sql

class GetData():
    def __init__(self):
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM Covid")
        self.data = cur.fetchall()
        self.dataToGetSentForDeaths = []
        self.dataToGetSentForInfected = []
        self.dataToGetSentForDates = []
        self.dataToGetSentForCountries = []
        self.i = 0
        self.j = 0

    def deaths(self, Country):
        for row in range(len(self.data)):
            #"Denmark" = Country
            if self.data[row]["Land"] == Country:
                self.dataToGetSentForDeaths.append(self.data[row]["Doede"])
        return self.dataToGetSentForDeaths

    def infected(self, Country):
        for row in range(len(self.data)):
            #"Denmark" = Country
            if self.data[row]["Land"] == Country:
                self.dataToGetSentForInfected.append(self.data[row]["Smittede"])
        return self.dataToGetSentForInfected


    def dates(self, Country):
        for row in range(len(self.data)):
            #"Denmark" = Country
            if self.data[row]["Land"] == Country:
                self.dataToGetSentForDates.append(self.data[row]["Date"])
        return self.dataToGetSentForDates

    def countries(self):
        for row in range(len(self.data)):
            self.dataToGetSentForCountries.append(self.data[row]["Land"])
        self.dataToGetSentForCountries = list(dict.fromkeys(self.dataToGetSentForCountries))
        return self.dataToGetSentForCountries

"""
mario = GetData()
deaths = mario.deaths("Denmark")
smittede = mario.infected("Denmark")
dato = mario.dates("Denmark")
lande = mario.countries()

print(deaths)
print(smittede)
print(dato)
print(lande)"""
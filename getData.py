import sqlite3 as sql

class GetData():
    def __init__(self):
        #Tilslutter sig til databasen
        con = sql.connect("database.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM Covid")
        #Tager alle daterne ud og putter dem i en liste
        self.data = cur.fetchall()
        #Bruges til at opbevare data som sende videre for hver kategori
        self.dataToGetSentForDeaths = []
        self.dataToGetSentForInfected = []
        self.dataToGetSentForDates = []
        self.dataToGetSentForCountries = []

        #Bruges til for loops
        self.i = 0
        self.j = 0

    #Sender data ud omkring døde
    def deaths(self, Country):
        #Sortere dataene efter det valgt land
        for row in range(len(self.data)):
            if self.data[row]["Land"] == Country:
                self.dataToGetSentForDeaths.append(self.data[row]["Doede"])
        #Sender dataen til websitet
        return self.dataToGetSentForDeaths

    # Sender data ud omkring smittede
    def infected(self, Country):
        # Sortere dataene efter det valgt land
        for row in range(len(self.data)):
            if self.data[row]["Land"] == Country:
                self.dataToGetSentForInfected.append(self.data[row]["Smittede"])
        # Sender dataen til websitet
        return self.dataToGetSentForInfected

    # Sender data ud omkring datoer
    def dates(self, Country):
        # Sortere dataene efter det valgt land
        for row in range(len(self.data)):
            if self.data[row]["Land"] == Country:
                self.dataToGetSentForDates.append(self.data[row]["Date"])
        # Sender dataen til websitet
        return self.dataToGetSentForDates

    # Sender data ud om alle lande
    def countries(self):
        for row in range(len(self.data)):
            self.dataToGetSentForCountries.append(self.data[row]["Land"])
        #Gøre at der ikke er nogle dublicates
        self.dataToGetSentForCountries = list(dict.fromkeys(self.dataToGetSentForCountries))
        # Sender dataen til websitet
        return self.dataToGetSentForCountries

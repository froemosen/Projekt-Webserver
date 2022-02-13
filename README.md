# Projekt-Webserver
Forklaringer af de forskellige filer som er relevante:
  - flaskMain.py
      * Programmets main. Kører hjemmesiden. Bemærk at man skal have flask installeret for at køre den. (flask, sqlite3, matplotlib)
  - getData.py    
      * Bruges til at hente data fra databasen (database.db), som bruges gennem flaskMain.py
  - DatabaseFiller.py
      * Opdaterer databasen med information fra csv-filen. 
  - DatabaseMaker.py    
      * Laver databasen (database.db)
  - SmittedeDødeData.csv
      * Manuelt hentet csv-fil med covid-19 data fra hele Europa.
  - database.db
      * Database med covid-data
  - fakedatabase.db
      * Database med indtastede oplysninger, bruges til at vise funktionalitet.

  - Templates
      * Home.html - Home page
      * list.html - Viser data fra fakedatabase.db
      * plotGraph.html - Plotter udvalgt type graf efter udvælgelse af lande
      * rawData.html - Viser rå data fra database.db
      * result.html - Viser status på overførsel af data i student.html
      * student.html - Til at indsætte data i fakedatabase.db
      * test.html - Testside

  - Static
      * corona.png - Billede til forside
      * graph.png - Billede af graf som vises i plotGraph.html


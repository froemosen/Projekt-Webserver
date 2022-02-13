# Projekt-Webserver
**Forklaringer af de forskellige filer som er relevante:**
  - **_flaskMain.py**_
      * Programmets main. Kører hjemmesiden. Bemærk at man skal have flask installeret for at køre den. (flask, sqlite3, matplotlib)
  - **_getData.py **_   
      * Bruges til at hente data fra databasen (database.db), som bruges gennem flaskMain.py
  - **_DatabaseFiller.py**_
      * Opdaterer databasen med information fra csv-filen. 
  - **_DatabaseMaker.py**_
      * Laver databasen (database.db)
  - **_SmittedeDødeData.csv**_
      * Manuelt hentet csv-fil med covid-19 data fra hele Europa.
  - **_database.db**_
      * Database med covid-data
  - **_fakedatabase.db**_
      * Database med indtastede oplysninger, bruges til at vise funktionalitet.

  - **_Templates**_
      * Home.html - Home page
      * list.html - Viser data fra fakedatabase.db
      * plotGraph.html - Plotter udvalgt type graf efter udvælgelse af lande
      * rawData.html - Viser rå data fra database.db
      * result.html - Viser status på overførsel af data i student.html
      * student.html - Til at indsætte data i fakedatabase.db
      * test.html - Testside

  - **_Static**_
      * corona.png - Billede til forside
      * graph.png - Billede af graf som vises i plotGraph.html


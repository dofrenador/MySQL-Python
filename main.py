import sqlite3
conn = sqlite3.connect('flowers.db') #Connect to the database

def displayFlowers(conn):
    c = conn.cursor()
    sql = '''SELECT * FROM FLOWERS GROUP BY COMNAME'''
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        print(row)
def displaySightings(conn):
    c = conn.cursor()
    sql1 = '''SELECT * FROM SIGHTINGS'''
    c.execute(sql1)
    rows = c.fetchall()
    for row in rows:
        print(row)

def displayFeatures(conn):
    c = conn.cursor()
    sql2 = '''SELECT * FROM FEATURES'''
    c.execute(sql2)
    rows = c.fetchall()
    for row in rows:
        print(row)

def getInfo(conn, name):
    c = conn.cursor()
    c.execute('SELECT PERSON, LOCATION, SIGHTED FROM SIGHTINGS WHERE NAME = ? ORDER BY SIGHTED DESC LIMIT 10', (name,))
    rows = c.fetchall()
    for row in rows:  # print row by row
        print(row)

def updateFlower(conn, name, genus, species):
    c = conn.cursor()
    c.execute('UPDATE FLOWERS SET GENUS= ?,SPECIES= ? WHERE COMNAME = ?', (genus, species, name,))
    c.execute('SELECT GENUS, SPECIES, COMNAME FROM FLOWERS WHERE COMNAME = ?', (name,))

    rows = c.fetchall()
 
    for row in rows:
        print(row)

def insertIntoSightings(conn,name,person,location,sighted):
    c = conn.cursor()
    c.execute('INSERT INTO SIGHTINGS (NAME, PERSON, LOCATION, SIGHTED) VALUES(?,?,?,?)', (name, person, location, sighted,))
    c.execute('SELECT NAME, PERSON, LOCATION, SIGHTED FROM SIGHTINGS WHERE PERSON = ? AND LOCATION = ? AND SIGHTED = ?',(person, location, sighted,))

    rows = c.fetchall()
 
    for row in rows:
        print(row)

def main():

    print("Menu:\n1.Select a flower, display the 10 most recent sightings \n2.Update flower(genus and species) \n3.Insert a new sighting of flower \n4.Display flowers after insertion\n5.Quit The Program")
    userInput = 0

    while userInput != 4:
        print("Select an option (1-5): ")
        userInput = input()
        if userInput == "1":
            displayFlowers(conn)
            print("\nEnter the common name of the flower: ")
            inputFlowerName = input()
            getInfo(conn, inputFlowerName)

        elif userInput == "2":

            displayFlowers(conn)
            print("\nEnter the name of flower: ")
            inputFlowerName = input()
            print("\nEnter a new genus name: ")
            newGenus = input()
            print("\nEnter a new species name: ")
            newSpecies = input()
            updateFlower(conn, inputFlowerName, newGenus, newSpecies)

        elif userInput == "3":
            inputFlowerName = input()
            print("Enter a new person: ")
            newPerson = input()
            print("\nEnter a new location: ")
            newLocation = input()
            print("\nEnter a new date (YYYY-MM-DD): ")
            newDate = input()
            insertIntoSightings(conn, inputFlowerName, newPerson, newLocation, newDate)

        elif userInput == "4":


            displayFlowers(conn)
            print("\nEnter the name of the flower: ")
            displaySightings(conn)

        elif userInput == "5":

            print("\nThanks for coming by. Hope to see you again !")
            break

        else:
            print("\nYou must enter (1-5)")

if __name__ == "__main__":
    main()
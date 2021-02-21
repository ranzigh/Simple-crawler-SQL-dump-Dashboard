import mysql.connector
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# cronjob code: 0 9-18 * * 1-5 um jede Stunde werktags das Bild zu aktulisieren

mydb = mysql.connector.connect(
	host="localhost", 
	user="user",        # In der Datenbank muss erst ein User eingerichtet werden und GRANTS für Zugriff bekommen
	passwd="password",  # Bestenfalls mit einem sicheren Passwort
	database="alexDB") 

mycursor = mydb.cursor()

mycursor.execute("SELECT Wert FROM finanzen100;")


y = mycursor.fetchall()[0]

mycursor.execute("SELECT Datum FROM finanzen100;")

x = mycursor.fetchall()[0]


plt.title("SQL-Extrakt")
img = plt.plot(x,y)
plt.savefig(fname= "image.jpg")


mydb.close()

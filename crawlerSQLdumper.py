from bs4 import BeautifulSoup as bs
import requests
import mysql.connector
from datetime import datetime
now = str(datetime.now())

# cronjob code: 0 9-18 * * 1-5 um jede Stunde werktags während die Börse offen ist zu crawlen

page = requests.get("https://www.finanzen100.de/aktien/gamestop-wkn-a0hgdx_H933557951_12950385/")
soup = bs(page.content, features="html.parser")
wert = soup.find(class_= "quote__price__price")
wert = wert.get_text()
wertlist = list(wert)

if len(wertlist) == 4: # Falls der Kurswert unter 10 sinkt
	wertlist[1] = "."
	wert = "".join(wertlist)
elif len(wertlist) == 5: # Falls der Kurswert zwischen 10 und 100 bleibt
	wertlist[2] = "."
	wert = "".join(wertlist)
elif len(wertlist) == 6: # Falls der Kurswert über 100 steigt
	wertlist[3] = "."
	wert = "".join(wertlist)
wert = float(wert)

extrakt = (1, wert, now) # Der erste Wert muss noch zum Counter umgewandelt werden

mydb = mysql.connector.connect(
	host="localhost", 
	user="user",        # In der Datenbank muss erst ein User eingerichtet werden und GRANTS für Zugriff bekommen
	passwd="password",  # Bestenfalls mit einem sicheren Passwort
	database="alexDB") 

mycursor = mydb.cursor()

sqlform = "INSERT INTO finanzen100 (Eintrag, Wert, Datum) VALUES (%s, %s, %s)"

mycursor.execute(sqlform, extrakt)

mydb.commit()
mydb.close()

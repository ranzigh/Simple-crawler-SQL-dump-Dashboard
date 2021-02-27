# Simple-crawler-SQL-dump-Dashboard

Dieses Programm kann stündlich einen Webcrawling-Job ausführen und das Ergebnis in einer Datenbank speichern. 
finanzen100 und die GameStop-Aktie ist hier nur ein Beispiel zu Demonstrationszwecken. Bitte nicht verklagen, finanzen100, ich crawle euch nicht wirklich.

Gleichzeitig kann aus der Datenbank der Aktienverlauf extrahiert, geplottet  und dann im Browser als HTML Dashboard angezeigt werden. Sowohl das Bild, als auch die Website aktualisieren sich dabei selbstständig. 

Was hier in den Projekt nicht enthalten ist, ist die Einrichtung zweier Cronjobs. Die sind aber essenziell, damit das alles funktioniert.

Im Terminal dazu:
'crontab -e'
eingeben und folgende Zeilen hinzufügen:

'0 9-18 * * 1-5 python3 SQLextrakt.py'

'0 9-18 * * 1-5 python3 crawlerSQLdumper.py'

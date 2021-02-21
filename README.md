# Webscraping-SQL-dump-Dashboard

Dieses Programm kann stündlich einen Webcrawling-Job ausführen, das Ergebnis in eine Datenbank packen. 
finanzen100 und die GameStop-Aktie ist hier nur ein Beispiel zu Demonstrationszwecken. Bitte nicht verklagen, finanzen100, ich crawle euch nicht wirklich.

Gleichzeitig kann aus der Datenbank der Aktienverlauf extrahiert, geplottet  und dann im Browser als HTML Dashboard angezeigt werden. Sowohl das Bild, als auch die Websize aktualisieren sich dabei selbstständig. 

Was hier in den Projekt nicht enthalten ist, ist die Einrichtung zweier Cronjobs. Die sind aber essenziell, damit das alles funktioniert.

Im Terminal dazu:
'crontab -e' 
0 9-18 * * 1-5 python3 
0 9-18 * * 1-5 python3 

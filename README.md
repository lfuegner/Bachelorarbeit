# Bachelorarbeit | Ludwig Fügner

Sehr geehrter Herr Neuenkrich,

hiermit versuche ich einen Überblick über den Code meiner Bachelorarbeit zu geben.

Python version: 3.12.0
Genutzte Packages:
- numpy
- statistics
- scipy
- pytest

Die Packages sind alle in der Datei [Requierments](requirements.txt) enthalten. Und können wie folgt mit dem Package Manager von Python PIP installiert werden.

```shell
# Installs all packages from the requirements.txt file.
pip install -r requirements.txt
```

Die Packages numpy, statistics und scipy wurden genutzt um Zufallsfunktionen und statistische Funktionen zu nutzen.

Das Package pytest wurde genutzt um einige Funktionen des Code zu testen. Die Tests befinden sich im Ordner [Tests](tests). Es wurden die Sequenzen, die Hifsfunktionen und weitere Funktionen getestet. Wenn das Package Pytest installiert ist können mit dem folgenden Command die Tests gelaufen lassen.
```shell
pytest
```

# Scripte
Um die beiden Scripte [Main](main.py) und [Data](data.py) laufen zu lassen, müssen die folgenden Command genutzt werden.
```shell
python main.py
# oder
python data.py
```
## Inputparameter
- "total_seats" = 132
- "type_" ist der Typ der sequence ["random","block","halfblock","row","halfrow","letter","seat","luggage"]
- "blocks" ist nur für die Typen block und halfblock interessant mit ["2","3","4","6","10"] sonst [""]
- "pattern" beschreibt die Regel die verwendet werden soll ist je nach Typ abhängig 
- "wrong_seats_percentage" ist die Wahrscheinlichkeit, dass ein Passgier zu einem falschen Sitzplatz geht. [0,0.05,0.2,1]
- "load" ist Auslastung des Hangepäcks ["normal","high"]
- "wrong_seats_distance" dies ist die Distanz die festlegt, wie weit der Falsche Sitzplatz von seinem echten Sitzplatz sein kann. Für "wrong_seats_distance" = 1 gilt für den Sitzplatz 45, dass als falsche Sitzplätze nur 44 und 46 in Frage kommen. "wrong_seats_distance" muss größer gleich 1 sein, eine Integer Variable und kleiner gleich der gesamt Sitzplatzanzahl hier 132.

## [Main](main.py)
Hier wird je nach Inputdaten ein Drchlauf gestartet und die Daten werden in [Data](data) als json Dateien gespeichert. Es werden [DATA_SEATS.json](DATA_SEATS.json), [DATA_ROWS.json](DATA_ROWS.json) und [DATA_PASSENGERS.json](DATA_PASSENGERS.json) gespeichert. Hier finden sie alle Daten die von der main Funktion gesammelt werden.

## [Data](data.py)
Hier werden alle Sequenzen die in der Datei [Sequence](sequence.txt) enthalten sind 10 mal durchgelaufen und die Gesamte Boarding-Zeit, die durchschnittliche individuelle Boarding-Zeit, die maximale individuelle Boarding-Zeit und die Konfidenzintervalle gespeichert. Die Daten die hier erzeugt wurden in den Tabellen und Plots der Bachelorarbeit genutzt.

## Data Procssing
In dem Jupiter Notebook wurden die Daten die mithilfe von data.py erstellt wurden so umstransformiert, dass man diese gut in LateX nutzen kann.

## Code Beschreibung

Über sequence.py werden die Sitz, Gepäck und fehlerhaften Sitzsequenzen erstellt, dabei wird bei der Generierung der Sitz Sequenz auf den Ordner [sequence_](sequence_) zurückgegriffen in dem für jeden Typ noch ein Pythondatei liegt, die dafür sorgt, dass die Sequenzen richtig erstellt werden.

data_structures.py erstellt die drei Mappings/ Dictionary die ich genutzt habe um die Daten wären einer Simulation zu speichern.

queueAllPassenger.py lässt alle Passagiere loop durch alle Passagiere, bis jeder einen Sitzplatz gefunden hat.

getToFirstRow.py sorgt dafür, dass die Passagiere in der Simulation an der Eingangstür ankommen und mäßig in Reihe 0 warten müssen bis die Reihe 1 vor ihnen frei ist.

Es wird dann geprüft, ob der Passagier schon seine gewünschte Reihe bereits erreicht hat, wenn nicht geht er mit getToTargetedRow zu dieser.

Wenn der Passagier seine Reihe erreich hat muss nun sein Sitzplatz überprüft werden, dafür ist checkSeat.py zuständig.
Wenn der Sitzplatz frei ist kann sich der Passagier hinsetzten.
Wenn der Sitzplatz bereits von einem anderen Passagier belegt ist, dann wird geschaut wem der Sitzplatz richtigerweise gehört. Der Falsche Passagier muss dann seinen richtigen Siztplatz aufsuchen.

getDirection.py schaut dabei ob er im Gang zurück oder weiter hinten ins Flugzeug muss. Wenn sein neuer Sitzplatz in der selben Reihe ist, dann bleibt er in der Reihe und versucht sich hinzusetzten. 

Dies geht solange bis alle Passagiere einen Sitzplatz gefunden haben.

Die Reihen sind solange blockiert, bis der vorherige Passagier endgültig die Reihe verlassen hat.

Aufgrund der for loop, kann ein Passagier erst los wenn der queue Prozess des Passagiers vor ihm beendet ist, deshalb ist es kein Problem, dass Passagiere in der Gangrichtung wieder zurück laufen können. Da sie dadurch nur die Wartezeit des nächsten erhöhen.

Ich hoffe ich konnte eine groben Überblick geben.

Beste Grüße

Ludwig Fügner
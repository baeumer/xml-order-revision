import xml.etree.ElementTree as ET
import time
tree = ET.parse('Versandliste.xml')
root = tree.getroot()

Termine = root[1]

Laufzeit = True

while Laufzeit:
    Beispieldatum = root[1][0][11].text
    print ""
    print "Beispieldatum:", Beispieldatum

    Suchtitel = raw_input("Suchtitel   : ")
    Start_NEU = raw_input("Start - NEU : ")
    Ende_NEU = raw_input("Ende - NEU  : ")
    
    Fehler = 0
    
    i = 0
    for Termin in Termine:
        Titel = Termin.find('titel').text
        if len(Start_NEU) != len (Termin.find('terminvon').text):
            print "Neuer Text mit falscher Laenge"
            Fehler = 1
            break
        if len(Ende_NEU) != len (Termin.find('terminbis').text):
            print "Neuer Text mit falscher Laenge"
            Fehler = 1
            break
        if Titel == Suchtitel:
            i = i + 1
            Termin.find('terminvon').text = Start_NEU
            Termin.find('terminbis').text = Ende_NEU

    if Fehler == 0:
        print i, "Aenderungen vorgenommen"

    Suchtitel = raw_input("Noch ein Titel? (J/N): ")
    if Suchtitel != 'J':
        Laufzeit = False


tree.write(open('Versandliste2.xml', 'w'))

# time.sleep(3)

def main(debug=False):
    text_list = []
    
    with open("real_test.TXT", "r") as f:
        for line in f: # Loop um jede einzelne Zeile der TXT Datei in eine Liste als einzelnes Element zu stecken
            text_list.append(line) 

    def remove_BW(Liste):
        
        counter = 0
        Nullerwert_gefunden = False
        Nullwert_markierung = "N0"
        
        for item in Liste:

            if Nullwert_markierung in item and "Proben_Nr" in item: # das and "Proben_Nr" ... ist um mögliche falsch positiv Sachen zu vermeiden
                Nullerwert_gefunden = True

            if Nullerwert_gefunden and "%PROBE%" in item:
                break

            counter += 1

        if Nullerwert_gefunden:
            return Liste[counter::]
        else:
            return Liste
        
    text_list = remove_BW(text_list)
    
    #text_list = text_list[10::] # Entfernt die Nullmessung # alte Funktion nicht mehr wirklich gebraucht

    for ind in range(0,len(text_list)):
        if "Mess_Datum_Uhrzeit" in text_list[ind]:
            temp_list = text_list[ind].split() # splittet die Messuhrzeit Zeile in Mess_Datum_Uhrzeit, Datum, Uhrzeit und schreibt es in eine temporäre Liste
            
            date_list = temp_list[1].split(".") # Ändert das Format in JJJJMMTT
            date_list.reverse()
            temp_list[1] = "".join(date_list) # Fügt es in temporäre Liste wieder ein

            time_list = str(temp_list[2]).split(":") # Ändert Format von hh:mm:ss in hhmm
            new_time = time_list[0] + time_list[1] 
            temp_list[2] = new_time # Fügt es in temporäre Liste wieder ein

            fin_item = " ".join(temp_list) # fügt einzele Listenbestandteile wieder zusammen
            text_list[ind] = fin_item + "\n" # schreibt die neu Fomatierte Zeile wieder in die Hauptliste und fügt Zeilenumbruch hinzu

        if "Messwert_CG" in text_list[ind]: # Wenn Messwert_CG in einer Zeile vorhanden ist prüft ob ein Ergebniss Ovr beträgt und ändert es gegenfalls zu 0
            messwert_split = text_list[ind].split()
            if messwert_split[2] == "0,00":
                messwert_split[4] = "0,00"
                text_list[ind] = " ".join(messwert_split) + "\n"
            

        if debug:
            print(f"{ind} " + f"{text_list[ind]}") # Nur zum Debuggen 
        

    new_file = open("text_output.LAF", "w") # Erstellt eine LAF Datei und schreibt die Daten der Liste herein
    new_file.writelines(text_list)
    
    # list_try = ["a","b","a"] # .index nur als Gedadenstütze falls man es mal verwendedn wollen würde
    # print(list_try.index("a"))

main(debug=False)

import pywhatkit as kit
import keyboard
import time
import csv

import csv
with open("./PrenotazioneTamponi.csv", newline="", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are {'; '.join(row)}")
            line_count += 1
        else:
            #print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
            number = row[5]
            if number != "":
                text = "Ciao, sono Andrea dell'ACG. Il tampone per " + row[3] + " " +row[4] +" si terra alla " + row[0] + " il giorno "+ row[1] + " alle ore "+row[2] + ". In caso non si possa accettare questa prenotazione o se ho sbagliato numero ti chiedo di comunicarmelo rispondendo a questo messaggio."
                print(row[3] + " " +row[4])
                kit.sendwhatmsg_instantly("+39"+number, text)
                time.sleep(10)
                keyboard.press_and_release("ctrl+w")
                line_count += 1
    print(f"Processed {line_count} lines.")




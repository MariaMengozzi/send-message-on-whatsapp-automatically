import pywhatkit as kit
import keyboard
import time
import csv

import csv
with open("./prova.csv", newline="", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are {'; '.join(row)}")
            line_count += 1
        else:
            #print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
            number = row[0]
            if number != "":
                text = """Ciao :-P"""
                kit.sendwhatmsg_instantly("+39"+number, text, 15, True, 4)
                time.sleep(10)
                line_count += 1
    print(f"Processed {line_count} lines.")




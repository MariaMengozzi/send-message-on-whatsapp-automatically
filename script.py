#import pywhatkit as kit #updateing sendwhatmsg_instantly with double click
import keyboard
import time
import csv

import pywhatkit as kit

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
                kit.sendwhatmsg_instantly("+39"+number, text, 15, True, 10)
                #time.sleep(10)
                line_count += 1
    print(f"Processed {line_count} lines.")


""" Pywhatkit update

def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    #INVIO DEL MESSAGGIO - rimetto il focus sulla chat
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


"""

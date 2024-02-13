import pywhatkit as kit
import keyboard
import time
import csv

class Send_message_script():

    def __init__(self, filename):
        self.filename = filename
        with open(filename, newline="", encoding="utf-8") as f:
            csv_reader = csv.reader(f, delimiter=";")
            self.column_name = next(csv_reader)
            self.column_name.index('Number')
    
    def get_column_name(self):
        return self.column_name

    def set_msg_string(self, text):
        self.msg_string = text
    
    def start_to_send(self):
        self.error_list = []

        with open(self.filename, newline="", encoding="utf-8") as f:
            csv_reader = csv.reader(f, delimiter=";")
            next(csv_reader)
            number = self.column_name.index('Number')
            for row in csv_reader:
                if row[number] != "":
                    txt = self.msg_string
                    for i in range(len(self.column_name)):
                        old = '{'+self.column_name[i]+'}'
                        new = str(row[i])
                        txt = txt.replace(old, new)
                    kit.sendwhatmsg_instantly("+39"+row[number], txt, 15, True, close_time=10)
                    #time.sleep(10)
                    #keyboard.press_and_release("ctrl+w")
                    #self.error_list.append('; '.join(row))
                else:
                    self.error_list.append('; '.join(row))
        return self.error_list
                



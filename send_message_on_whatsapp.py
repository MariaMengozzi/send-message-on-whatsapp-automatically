#https://realpython.com/pysimplegui-python/ -->tutorial

from Send_message_script import Send_message_script
import PySimpleGUI as sg
import os.path
from Send_message_script import Send_message_script
import traceback
import keyboard


#TODO check input != {}

def main():
    # First the window layout in 2 columns
    file_list_column = [
        [
            sg.Text('''The CSV file must have ; as separator
            the first line with name column 
            the phone nummber column called 'Number'!'''),
        ],
        [
            
            sg.Text("CSV File:"),
            sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(file_types=(("CSV files", "*.csv"),))
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-VARIABLE LIST-"
            )
        ],
    ]

    # For now will only show the name of the file that was chosen
    message_column = [
        [sg.Text('''Write a message. If you want to insert a variable from the column that 
        is in the csv select the name from the list on left. 
        [Note - you can't use {} if you want to delete a variable you must delete {VariableName}]''')],
        [sg.Multiline(size=(40, 20), key="-MULTILINE-")],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(message_column),
            
        ],
        [sg.Button('START')],
        [sg.Text('''Start to send message. 
            In order to avoid error open a browser tab and don\'t close it.''', key='-SENDING-',visible=False)],
        [sg.Text('Finished sending message', key='-FINISHED-', visible=False)]
    ]

    window = sg.Window("Send message on whatsapp", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-FILE-":
            script = None
            window['-MULTILINE-'].update('')
            window["-VARIABLE LIST-"].update([])
            window['-SENDING-'].Update(visible=False)
            window['-FINISHED-'].Update(visible=False)

            file = values["-FILE-"]
            try:
                #column_list
                script = Send_message_script(file)
                cnames = script.get_column_name()
            except Exception as e:
                tb = traceback.format_exc()
                sg.Print(f'An error happened.  Here is the info:', e, tb)
                sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
                cnames = []

            window["-VARIABLE LIST-"].update(cnames)

        elif event == "-VARIABLE LIST-":  # A file was chosen from the listbox
            text = window['-MULTILINE-']
            text.update(text.get()[:-1]+ '{'+ values['-VARIABLE LIST-'][0] + '}')
            
        elif event == "START":
            if script is not None:
                script.set_msg_string(window['-MULTILINE-'].get())
                '''window.disable()
                window['-SENDING-'].Update(visible=True)'''
                window.close()
                error_list = script.start_to_send()
                
                print('\n'.join([i for i in error_list]
                ))
                '''window['-SENDING-'].Update(visible=False
                )
                window['-FINISHED-'].Update(visible=True)
                window.enable()
                if len(error_list) != 0:
                    sg.popup_error(f'Message error list',  '\n'.join([i for i in error_list[1:]]))'''
                sg.popup(f'Message error list',  '\n'.join([i for i in error_list[:]]),)

    #window.close()

if __name__ == '__main__':
    main()

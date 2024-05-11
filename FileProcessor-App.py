import FreeSimpleGUI as sg
import Compressfilegui
import Extractfilegui

sg.theme("Black")

main_lable = sg.Text("Compress or Extract Zip Files")

compress_button = sg.Button("Compress Files", size=15)
extract_button = sg.Button("Extract Files", size=15)
exit_button = sg.Button("Exit", size=15)

layout = [[main_lable], [compress_button, extract_button], [exit_button]]

window = sg.Window("File Processor App",layout)

while True:
    event,values = window.read()
    match event:
        case "Compress Files":
            Compressfilegui.compress_files()
        
        case "Extract Files":
            Extractfilegui.extract_files()

        case "Exit":
            break
        
        case sg.WIN_CLOSED:
            break
        
window.close()
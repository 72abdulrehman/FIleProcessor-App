import FreeSimpleGUI as sg
import Extractfilebackend
import os

def extract_files():
    lable_com = sg.Text("Extract your compressed files")
    
    lable_1 = sg.Text("Select Archived Files:")
    input_1 = sg.Input(key="input1")
    file_browse_button = sg.FileBrowse("Choose", key="archive", target="input1")
    
    lable_2 = sg.Text("Choose Destination Folder:")
    input_2 = sg.Input(key="input2")
    folder_browse_button = sg.FolderBrowse("Choose", key="folder", target="input2")
    
    extract_button = sg.Button("Extract")
    output = sg.Text(key="output", text_color="White")
    
    exit_button = sg.Button("Exit")
    
    col_1 = sg.Column([[lable_1],[lable_2]])
    col_2 = sg.Column([[input_1],[input_2]])
    col_3 = sg.Column([[file_browse_button],[folder_browse_button]])
    
    #layout = [[lable_com], [lable_1,input_1,file_browse_button], [lable_2, input_2, folder_browse_button],[extract_button]]
    
    layout = [[lable_com],[col_1, col_2, col_3],[extract_button, output], [exit_button]]
    
    window = sg.Window("Extract Files", layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        match event:
            case sg.WIN_CLOSED:
                break
                
            case "Extract":
                archivepath = values["archive"]
                split_tup = os.path.splitext(archivepath)
                file_extension = split_tup[1]
                dest_dir = values["folder"]
                if file_extension != ".zip":
                    sg.popup("Please choose zip files for extraction")
                elif not archivepath or not dest_dir:
                    sg.popup("Please choose compressed files or destination folder before file extraction.")
                else:
                    Extractfilebackend.extract_files(archivepath, dest_dir)
                    window["output"].update(value="Extraction Successfull!")
                    
            case "Exit":
                break
                
    window.close()
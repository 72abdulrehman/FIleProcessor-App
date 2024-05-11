import FreeSimpleGUI as sg
import Compressfilebackend

def compress_files():
    lable_com = sg.Text("Compress your files into zip folder")
    
    lable_1 = sg.Text("Select Compressed Files:")
    input_1 = sg.Input(key="input1")
    file_browse_button = sg.FilesBrowse("Choose", key="zip", target="input1")
    
    lable_2 = sg.Text("Choose Destination Folder:")
    input_2 = sg.Input(key="input2")
    folder_browse_button = sg.FolderBrowse("Choose", key="folder", target="input2")
    
    compress_button = sg.Button("Compress")
    output = sg.Text(key="output", text_color="White")
    
    exit_button = sg.Button("Exit")
    
    col_1 = sg.Column([[lable_1],[lable_2]])
    col_2 = sg.Column([[input_1],[input_2]])
    col_3 = sg.Column([[file_browse_button],[folder_browse_button]])
    
    #layout = [[lable_com], [lable_1,input_1,file_browse_button], [lable_2, input_2, folder_browse_button],[compress_button, output],[exit_button]]
    
    layout = [[lable_com], [col_1, col_2, col_3],[compress_button, output],[exit_button]]
    
    window = sg.Window("Compress Files", layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        match event:
            case sg.WIN_CLOSED:
                break
            
            case "Compress":
                filespaths = values["zip"].split(";")
                folder = values["folder"]
                if values["zip"]=='' or not folder:
                    sg.popup("Please choose files or destination folder before compressing files.")
                else:
                    Compressfilebackend.make_archive(filespaths, folder)
                    window["output"].update(value="Compression Successfull!")
        
            case "Exit":
                break
            
    window.close()
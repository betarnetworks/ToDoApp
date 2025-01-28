import FreeSimpleGUI as sg

label1 = sg.Text("Select Files to compress")
input1 = sg.Input()
chooseButton = sg.FileBrowse('Choose File')

label2 = sg.Text("Select Files to compress")
input2 = sg.Input()
chooseButton2 = sg.FileBrowse('Choose File')

compressButton = sg.Button('Compress')

window = sg.Window('File Compressor', layout=[[label1, input1, chooseButton],
                                              [label2, input2, chooseButton2],
                                              [compressButton]])
window.read()
window.close()
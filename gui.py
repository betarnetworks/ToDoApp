import Fcntodo
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter todo")
addButton = sg.Button("Add")

window = sg.Window("Welcome to my To-Do App", layout=[[inputBox, addButton], [label]])
window.read()
window.close()
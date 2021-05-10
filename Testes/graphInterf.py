import PySimpleGUI as gui
import os.path

class Layouts:

        mainWindow = [
            [gui.Text('Musical Translation Software', font = ("Arial",20))],
            [gui.Text('Open file:', size = (20,1)), gui.FileBrowse(file_types=(("Text Files", "*.txt"),), target = 'addressOutput', size = (21,1), )],
            [gui.Text('', visible = False, key = 'addressOutput', enable_events = True)],
            [gui.Text('User input:', size = (20,1)), gui.Multiline('', size=(22,5), key = 'textInput')],
            [gui.Text('Status:', size = (21,1)), gui.Text('Waiting', key = 'statusOutput')],
            [gui.Button('Play', size = (20,1)), gui.Button('Quit', size = (20,1))]
        ]

class WindowManager:

    def createWindow(self, layout):
        return gui.Window('Musical Translation Software', element_justification='center', layout = layout, finalize=True)

    def swapActiveWindow(self, oldWindow, newWindow):
        self.hideWindow(oldWindow)
        self.unHideWindow(newWindow)

    def hideWindow(self, window):
        window.hide()

    def unHideWindow(self, window):
        window.un_hide()

class GraphInterf:

    def __init__(self, callback):
        self.manager = WindowManager()
        self.window = self.manager.createWindow(Layouts.mainWindow)
        self._callback = callback

    def event_loop(self):
        while True:
            self.window, self.event, self.values = gui.read_all_windows()

            print(self.event)

            if self.event == gui.WIN_CLOSED or self.event == 'Quit':
                self._callback(self.event,self.values)
                break

            elif self.event == 'Browse':
                if os.path.isfile(self.values['addressOutput']):
                    file = open(self.values['addressOutput'], 'r')
                    text = file.read()
                    window.Element['textInput'].Update(text)
                    self._callback(self.event, self.values)
                else:
                    window.Element['textInput'].Update('Please, select a valid address.')

            elif self.event == 'Play':
                self._callback(self.event,self.values)
                self.window.Element('statusOutput').Update('Playing')
        self.window.Close()

def printzin(event, values):
    print('oi')

teste = GraphInterf(callback = printzin)
teste.event_loop()


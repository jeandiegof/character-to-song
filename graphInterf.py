import PySimpleGUI as gui
import os.path

class MainWindow:

    def __init__(self, callback):
        self._currentStatus = 'waiting'
        self._callback = callback
        self._layout = [
            [gui.Text('Musical Translation Software', font = ("Arial",20))],
            [gui.Text('Open file:', size = (20,1)), gui.FileBrowse(file_types=(("Text Files", "*.txt"),), target = 'FileAddress', size = (21,1), )],
            [gui.Input(visible = False, key = 'FileAddress', enable_events = True)],
            [gui.Text('User input:', size = (20,1)), gui.Multiline(size=(22,5), key = 'textInput')],
            [gui.Text('Status:', size = (21,1)), gui.Text('Waiting', key = 'statusOutput')],
            [gui.Button('Play | Stop', size = (20,1)), gui.Button('Quit', size = (20,1))]
        ]
        self._window = self.createWindow()

    def createWindow(self):
        return gui.Window('Musical Translation Software', element_justification='center', layout = self._layout, finalize=True)
        
    def event_loop(self):
        while True:
            self._window, self.event, self.values = gui.read_all_windows()

            if self.event == gui.WIN_CLOSED or self.event == 'Quit':
                self._callback(self.event,self.values)
                break

            elif self.event == 'FileAddress':
                if os.path.isfile(self.values['FileAddress']):
                    file = open(self.values['FileAddress'], 'r')
                    text = file.read()
                    self._window.Element('textInput').Update(text)
                    self._callback(self.event, self.values)
                else:
                    self._window.Element('textInput').Update('Please, select a valid address.')

            elif self.event == 'Play | Stop':
                    self._callback(self.event,self.values)
                    if (self._currentStatus == 'waiting'):
                        self._currentStatus = 'playing'
                        self._window.Element('statusOutput').Update('Playing')
                    else:
                        self._currentStatus = 'waiting'
                        self._window.Element('statusOutput').Update('Waiting')
        self._window.Close()
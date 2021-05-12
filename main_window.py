import PySimpleGUI as gui
import os.path

import threading


class MainWindow:
    def __init__(self, callback):
        self._current_status = 'waiting'
        self._callback = callback
        self._layout = [
            [gui.Text('Musical Translation Software', font=("Arial", 20))],
            [gui.Text('Open file:', size=(20, 1)), gui.FileBrowse(file_types=(
                ("Text Files", "*.txt"),), target='FileAddress', size=(21, 1), )],
            [gui.Input(visible=False, key='FileAddress', enable_events=True)],
            [gui.Text('User input:', size=(20, 1)),
             gui.Multiline(size=(22, 5), key='textInput')],
            [gui.Text('Status:', size=(21, 1)), gui.Text(
                'Waiting', key='statusOutput')],
            [gui.Button('Play | Stop', size=(20, 1)),
             gui.Button('Quit', size=(20, 1))]
        ]
        self._window = None

    def create_window(self):
        return gui.Window('Musical Translation Software', element_justification='center', layout=self._layout, finalize=True)

    def run(self):
        self._window = self.create_window()

        while True:
            self._window, event, values = gui.read_all_windows()

            if event == gui.WIN_CLOSED or event == 'Quit':
                break
            elif event == 'FileAddress':
                filename = values['FileAddress']

                if os.path.isfile(filename):
                    file = open(filename, 'r')
                    self._update_text_input_element(file.read())
                else:
                    self._update_text_input_element(
                        'Please, select a valid address.')
            elif event == 'Play | Stop':
                song = values['textInput']
                threading.Thread(target=self._callback, args=(song,)).start()

        self._window.Close()

    def update_status_output_element(self, value):
        self._update_element('statusOutput', value)

    def _update_text_input_element(self, value):
        self._update_element('textInput', value)

    def _update_element(self, name, value):
        self._window.Element(name).Update(value)

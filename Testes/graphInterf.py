import PySimpleGUI as gui
import os.path

class Layouts:

    def startWindow(self):
        layout = [
            [gui.Text('Software de Tradução Texto-Musical', font = ("Arial",20))],
            [gui.Text('Selecione uma das opções abaixo:')],
            [gui.Button('Abrir um arquivo de texto'), gui.Button('Digitar um texto')]
        ]
        return layout

    def browserWindow(self):
        layout = [
            [gui.Text('Digite o diretório do arquivo')],
            [gui.Input(key = 'address')],
            [gui.Button('Voltar'), gui.Button('Avançar')]
        ]
        return layout

    def textWindow(self, input = ''): 
        layout = [
            [gui.Text('Digite ou complemente o texto abaixo')],
            [gui.Multiline(input, size=(60,30), key = 'textInput')],
            [gui.Button('Voltar'), gui.Button('Tradução musical')]
        ]
        return layout

class WindowManager:

    def createWindow(self, layout):
        return gui.Window('Conversor Musical', layout = layout, finalize=True)

    def swapActiveWindow(self, oldWindow, newWindow):
        self.hideWindow(oldWindow)
        self.unHideWindow(newWindow)

    def hideWindow(self, window):
        window.hide()

    def unHideWindow(self, window):
        window.un_hide()

class GraphInterf:

    def __init__(self):
        pass

#Testes temporários
manager = WindowManager()
layouts = Layouts()

startWindow = manager.createWindow(layouts.startWindow())
browserWindow, textWindow, textWindow2 = None, None, None

while True:

    window, event, values = gui.read_all_windows()
    if event == gui.WIN_CLOSED:
        break

    elif window == startWindow:
        if event == 'Abrir um arquivo de texto':
            browserWindow = manager.createWindow(layouts.browserWindow())
            manager.hideWindow(startWindow)

        elif event == 'Digitar um texto':
            textWindow = manager.createWindow(layouts.textWindow())
            manager.hideWindow(startWindow)

    elif window == browserWindow:
        if event == 'Voltar':
            manager.swapActiveWindow(browserWindow, startWindow)
            
        elif event == 'Avançar':
            #verifica a existência do diretório e do arquivo
            if(os.path.isfile(values['address'])):
                file = open(values['address'], 'r')
                text = file.read()
                textWindow2 = manager.createWindow(layouts.textWindow(text))
                manager.hideWindow(browserWindow)
            else:
                textWindow2 = manager.createWindow(layouts.textWindow('Não foi possível abrir o arquivo.'))
                manager.hideWindow(browserWindow)

    elif window == textWindow:
        if event == 'Voltar':
            manager.swapActiveWindow(textWindow, startWindow)

        elif event == 'Tradução musical':
            #chama a função do jean, enviando o texto como parâmetro
            manager.hideWindow(textWindow)

    elif window == textWindow2:
        if event == 'Voltar':
            manager.swapActiveWindow(textWindow2, startWindow)

        elif event == 'Tradução musical':
            #chama a função do jean, enviando o texto como parâmetro
            manager.hideWindow(textWindow2)

import PySimpleGUI as gui


class GraphInterf:

    def __init__(self):
        gui.theme('DarkGray5')
        layout = [
            [gui.Text('Software de Tradução Texto-Musical', font = ("Arial",22))],
            [gui.Text('Selecione uma das opções abaixo:')],
            [gui.Button('Abrir um arquivo de texto'), gui.Button('Digitar um texto')]
        ]
        return gui.Window('StartWindow', layout=layout, finalize=True)

    def textWindow(self):
        gui.theme('DarkGray5')
        layout = [
            [gui.text('Digite um texto abaixo')],
            [gui.Input()]
        ]
        return gui.Window('TextWindow', layout=layout, finalize=True)

    def browserWindow(self):
        pass


#Testes temporários
startWindow = GraphInterf()
browserWindow = None
textWindow = None

while True:

    window, event, values = gui.read_all_windows() 
            
    if window == startWindow and event == 'Abrir um arquivo de texto':
        browserWindow = GraphInterf.browserWindow()
        startWindow.hide()
            
    if window == startWindow and event == 'Digitar um texto':
        textWindow = GraphInterf.textWindow()
        startWindow.hide()
                

        



janelaTeste = InterfManager()

import PySimpleGUI as gui


class GraphInterf:

    def startWindow(self):
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
            [gui.Text('Digite um texto abaixo')],
            [gui.Multiline(size=(60,30))],
            [gui.Button('Voltar'), gui.Button('Tradução musical')]
        ]
        return gui.Window('TextWindow', layout=layout, finalize=True)

    def browserWindow(self):
        gui.theme('DarkGray5')
        layout = [
            [gui.Text('Digite o diretório do arquivo')],
            [gui.Input()],
            [gui.Button('Voltar'), gui.Button('Avançar')]
        ]
        return gui.Window('BrowserWindow', layout=layout, finalize=True)


#Testes temporários
InterfObj = GraphInterf()
startWindow = InterfObj.startWindow()
browserWindow = None
textWindow = None

while True:

    window, event, values = gui.read_all_windows()

    if event == gui.WIN_CLOSED:
        break

    elif window == startWindow:
        if event == 'Abrir um arquivo de texto':
            browserWindow = InterfObj.browserWindow()
            startWindow.hide()
        elif event == 'Digitar um texto':
            textWindow = InterfObj.textWindow()
            startWindow.hide()

    elif window == browserWindow:
        if event == 'Voltar':
            browserWindow.hide()
            startWindow.un_hide()
        elif event == 'Avançar':
            #verifica a existência do diretório e do arquivo
            #e adiciona o texto do arquivo ao 'multiline'
            browserWindow.hide()
            textWindow = InterfObj.textWindow()

    elif window == textWindow:
        if event == 'Voltar':
            textWindow.hide()
            startWindow.un_hide()
        elif event == 'Tradução musical':
            #envia o arquivo de texto para a parte do jean
            textWindow.hide()
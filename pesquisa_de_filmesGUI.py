import requests
import json
import PySimpleGUI as sg



layout = [
    [sg.Text("Buscar filme")],
    [sg.InputText(key="titulo")],
    [sg.Button("BUSCAR"), sg.Button("LIMPAR")],
    [sg.Text("",key="detalhes")
    ]
]

janela = sg.Window("FILMES", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    
    
    if evento == "BUSCAR":
        op = valores["titulo"]

        
    def titulo(pesquisa):
        try: 
            tit = requests.get('http://www.omdbapi.com/?apikey=8e3d0f3b&t=' + pesquisa + '&type=movie')
            dict = json.loads(tit.text)
            return dict
        except:
            print('ERRO')
            return None

    def print_detalhes(filme):
        
        valor = ('Titulo: ', filme['Title'],
        "ANO: ", filme['Year'],
        "Diretor: ", filme['Director'],
        "Atores: ", filme['Actors'],
        "Nota: ", filme['imdbRating'],
        "Premios: ", filme['Awards'])

        return valor

    filme = titulo(op)
    valor = print_detalhes(filme)
    if filme["Response"] == "False":
        janela["detalhes"].update("Filme nao encontrado!")
    else: 
        janela["detalhes"].update(valor)

    if evento == "LIMPAR":
        janela["titulo"].update("")
        janela["detalhes"].update("")
    

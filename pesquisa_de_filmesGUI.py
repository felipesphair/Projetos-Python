import requests
import json
import PySimpleGUI as sg



layout = [
    [sg.Text("Buscar filme")],
    [sg.InputText(key="titulo")],
    [sg.Button("BUSCAR"), sg.Button("LIMPAR")],
    [sg.Text(key="detalhes")
    ]
]

janela = sg.Window("FILMES", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    
    if evento == "LIMPAR":
        valores["detalhes"] = ""
        valores["titulo"] = ""
    
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
        
        print("Titulo: ", filme['Title'])
        print("ANO: ", filme['Year'])
        print("Diretor: ", filme['Director'])
        print("Atores: ", filme['Actors'])
        print("Nota: ", filme['imdbRating'])
        print("Premios: ", filme['Awards'])

    filme = titulo(op)
    if filme["Response"] == "False":
        valores["detalhes"] = "Filme nao encontrado!"
    else: 
        valores["detalhes"] = print_detalhes(filme)

    
janela.close()
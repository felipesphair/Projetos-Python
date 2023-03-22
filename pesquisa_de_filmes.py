import requests
import json
import PySimpleGUI as sg

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

sair = False 

while not sair:
    op = input("Digite o nome de um filme ou digite SAIR para finalizar o programa: ")

    if op == "SAIR":
        sair = True
        print("Desligando...")

    else:
        filme = titulo(op)
        if filme["Response"] == "False":
            print("Filme nao encontrado!")
        else: 
            print_detalhes(filme)


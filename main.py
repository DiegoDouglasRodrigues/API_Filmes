import requests
import pprint
import json
from tkinter import *
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import messagebox

import urllib.request
from PIL import Image
from PIL import ImageTk, Image
import os
import glob

#Definindo as cores
cor0 = '#000000' #preto
cor1 = '#ffffff' #branco
cor2 = '#071169' #azul framde de cima
cor3 = '#cadce0' # azul frame debaixo
cor3b = '#f2f2f2' #azul frame filme
cor4 = '#4e8a96' # azul faixa
cor5 = '#04d43c' #verde botao
cor6 = '#f04646' #vermelho botao
cor7 = '#d993ca' #rosa
cor8 = '#d9d9d9' #cinza bg letras abas



janela = Tk()
janela.geometry('1300x900')
janela.title('Filmes')

#Criando frame de cima
frame_cima = Frame(janela, width=1800, height=100, background=cor2)
frame_cima.place(x=5,y=5)

l_titulo = Label(frame_cima, text="Sistema Acompanhamento de Filmes", bg=cor2, fg=cor1, font=('verdana 20 '))
l_titulo.place(x=200, y=25)

#inserindo logo
logo = tk.PhotoImage(file="Capturar.PNG")
logo = logo.subsample(3, 4)
l_logo = Label(frame_cima, image=logo)
l_logo.place(x=20, y=15 )


# photo = ImageTk.PhotoImage(file=fr"C:\Users\DIEGO\Desktop\projetos\API\imagens\{arquivo}")
# canvas.create_image(20, 20, anchor=NW, image=photo)
# img = Label(frame_filmes, image=photo).pack()

#Criando frame Debaixo
frame_meio = Frame(janela,width=1800, height=400, bg=cor3)
frame_meio.place(x=190, y=120)

#Criando frame Filmes
frame_filmes = Frame(frame_meio, width=1300, height=350, bg=cor5)



#criando scrollbar
container = ttk.Frame(frame_meio, )

canvas = tk.Canvas(container, width=900, height=500)
scrollbar_y = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar_x = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
frame_filmes = ttk.Frame(canvas, )

frame_filmes.bind(
  "<Configure>",
  lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")
  )
)

canvas.create_window((0, 0), window=frame_filmes, anchor="nw")


canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)


container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")

canvas.pack(side="left", fill="both", expand=True)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")



messagebox.showinfo('Seja bem vindo!','Click em um dos botoes ao lado para atualizar a lista!')


def limpar_imagens_filmes():
  files = glob.glob(r'C:\Users\DIEGO\Desktop\projetos\API\imagens\*.jpg')

  for f in files:
    os.remove(f)


def download_imagens():

  api_key = '3adbb5856e462f0378b57334a2d07412'
  REQUEST_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYWRiYjU4NTZlNDYyZjAzNzhiNTczMzRhMmQwNzQxMiIsInN1YiI6IjYzZjI4ODE3YTI0YzUwMDA3OGM5NDJiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HwZx9EkJD0M1jdkmk6osQszIyX88rSP-iRlmvbYw_sw'

  #filmes populares
  link = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"
  link_imagem = "https://image.tmdb.org/t/p/w500"

  limpar_imagens_filmes()

  requisicao = requests.get(link)
  informacoes = requisicao.json()
  lista_filmes = (informacoes['results'])

  indice = 0

  dicio = {}
  for item in lista_filmes:
    dicio['titulo'] = (lista_filmes[indice]['original_title'])
    dicio['nota'] = (lista_filmes[indice]['vote_average'])
    dicio['descricao'] = (lista_filmes[indice]['overview'])
    dicio['foto_01'] = (lista_filmes[indice]['backdrop_path'])
    dicio['foto_02'] = (lista_filmes[indice]['poster_path'])

    link_capa = (link_imagem + str(dicio['foto_01']))
    #print(link_capa)

    dicio['foto_01'] = dicio['foto_01'][1:]
    #print(dicio)



    # import urllib
    resource = urllib.request.urlopen(link_capa)
    os.chdir(r'C:\Users\DIEGO\Desktop\projetos\API\imagens')

    salvar = open(r'C:\Users\DIEGO\Desktop\projetos\API\imagens\\'f"{dicio['foto_01']}", "wb")
    salvar.write(resource.read())
    salvar.close()
    dicio['imagem'] = r'C:\Users\DIEGO\Desktop\projetos\API\imagens\\'f"{dicio['foto_01']}"

    indice = indice + 1


    titulo = dicio['titulo']
    nota = dicio['nota']
    descricao = dicio['descricao']
    foto_1 = dicio['foto_01']
    capa = dicio['imagem']
    foto_capa_enredeco_final = (dicio['imagem'][45:84])

    print(f'imagem baixada {titulo}')

  popular()

#funcao para criar tupla e postar
def popular():
  global imagens
  lista_filmes2 = []


  api_key = '3adbb5856e462f0378b57334a2d07412'
  REQUEST_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYWRiYjU4NTZlNDYyZjAzNzhiNTczMzRhMmQwNzQxMiIsInN1YiI6IjYzZjI4ODE3YTI0YzUwMDA3OGM5NDJiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HwZx9EkJD0M1jdkmk6osQszIyX88rSP-iRlmvbYw_sw'

  #filmes populares
  link = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"
  link_imagem = "https://image.tmdb.org/t/p/w500"



  requisicao = requests.get(link)
  informacoes = requisicao.json()
  lista_filmes = (informacoes['results'])


  indice = 0

  dicio = {}

  for item in lista_filmes:
    dicio['titulo'] = (lista_filmes[indice]['original_title'])
    dicio['nota'] = (lista_filmes[indice]['vote_average'])
    dicio['descricao'] = (lista_filmes[indice]['overview'])
    dicio['foto_01'] = (lista_filmes[indice]['backdrop_path'])
    dicio['foto_02'] = (lista_filmes[indice]['poster_path'])


    tupla = dicio['titulo'] , dicio['foto_01'], dicio['nota'], dicio['descricao']
    indice += 1
    lista_filmes2.append(tupla)


# localizando a foto e postando junto com titulo, foto, nota, descricao
  for titulo, arquivo , nota, descricao in lista_filmes2:

    titulo_filme = Label(frame_filmes, text=f'{titulo}', font=('verdana 20 ')).pack()
    #print(fr"C:\Users\DIEGO\Desktop\projetos\API\imagens\{arquivo}")
    photo=ImageTk.PhotoImage(file=fr"C:\Users\DIEGO\Desktop\projetos\API\imagens\{arquivo}")
    canvas.create_image(20, 20, anchor=NW, image=photo)
    img = Label(frame_filmes,image=photo).pack()
    imagens.append(photo)
    nota_filme = Label(frame_filmes, text=f'Avaliacao: {nota}', font=('verdana 12 ')).pack()

    if len(descricao) > 10:
      separador = ('\n')
      primeira_parte = (descricao[:80])
      segunda_parte = (descricao[80:180])
      terceira_parte = (descricao[180:260])
      quarta_parte = (descricao[260:340])
      quinta_parte = (descricao[340:420])
      sexta_parte = (descricao[420:])
      descricao_formatada =  (primeira_parte + separador + segunda_parte + separador +
                              terceira_parte + separador+ quarta_parte + separador + quinta_parte + separador + sexta_parte)

      descricao_filme = Label(frame_filmes, text=f'Descricao: {descricao_formatada}', font=('verdana 12 ')).pack()

    else:
      print(descricao)

      descricao_filme = Label(frame_filmes, text=f'Descricao: {descricao}', font=('verdana 12 ')).pack()

    espaco = Label(frame_filmes, text='\n\n\n\n ').pack()


imagens = []




frame_botoes = Frame(janela, width=170, height=500, background=cor3)
frame_botoes.place(x=5, y=120)


bt1 = Button(frame_botoes, text='Filmes populares', command=download_imagens, height=2, width=15, font=('verdana 10 bold') )
bt1.place(x=10,y=30)

bt2 = Button(frame_botoes, text='Filmes cinema', command=popular, height=2, width=15, font=('verdana 10 bold') )
bt2.place(x=10,y=80)

bt3 = Button(frame_botoes, text='Series populares', height=2, width=15, font=('verdana 10 bold') )
bt3.place(x=10,y=130)

bt4 = Button(frame_botoes, text='Series em cartas  ', height=2, width=15, font=('verdana 10 bold') )
bt4.place(x=10,y=180)


janela.mainloop()

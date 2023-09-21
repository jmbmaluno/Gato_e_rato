from classes import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def atualizar(lista):
    x = []
    y = []

    for p in lista:
        p.andar()
        x.append(p.ponto_atual.x)
        y.append(p.ponto_atual.y)

    return x,y

gato = Personagem(Vetor(0,1), 1, Vetor(1,0))
rato = Personagem(Vetor(0,0), 0.5, Vetor(1,0))

lista_personagem = []
x = []
y = []

lista_personagem.append(gato)
lista_personagem.append(rato)

fig,ax = plt.subplots()
ax.plot(x,y)


def update(i):
    
    pos_x,pos_y = atualizar(lista_personagem)
    global x
    global y

    
    x = x + pos_x
    y = y + pos_y
    

    plt.cla()
    ax.plot(x,y)


ani = FuncAnimation(fig = fig, func = update, frames = 200)

plt.show()

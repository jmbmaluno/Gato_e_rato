from personagem import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


##########  CASO GERAL  ###########


entrada = open('entrada.txt', 'r')

cena = Cenario()
mov = []

for i in entrada:
    i = i.replace(' ', '')
    l = i.split(';')

    l[2] = l[2].replace('(', '')
    l[2] = l[2].replace(')', '')

    coord = l[2].split(',')

    cena.add(Personagem(l[0], l[1],
                        Vetor(float(coord[0]), float(coord[1])),
                        float(l[3])))

    if len(l) > 4:
        mov.append(l[4])


for i in range(len(mov)):
    mov[i] = mov[i].replace('\n', '')

    if mov[i][0] == '(':
        mov[i] = mov[i].replace('(', '')
        mov[i] = mov[i].replace(')', '')

        coord = mov[i].split(',')

        cena.lista[i].adicionar_direcao(Vetor(
            float(coord[0]), float(coord[1])))
    
    elif  mov[i][0] == '[':
        #Aplicar aqui a parte de trajetoria
        mov[i] = mov[i].replace('[', '')
        mov[i] = mov[i].replace(']', '')
        mov[i] = mov[i].replace(' ', '')

        l = []

        j = 1

        while j < len(mov[i]):
            
            if mov[i][j] != ',':
                l.append(Vetor(float(mov[i][j]), float(mov[i][j+2])))
                j = j + 2

            j = j + 2
        
        cena.lista[i].adicionar_trajetoria(l)
    
    else:
        alvo = mov[i]
        for j in cena.lista:
            if j.nome == alvo:
                cena.lista[i].adicionar_alvo(j)
                break


entrada.close()


fig, ax = plt.subplots()


for i in range(len(cena.matriz_x)):
    nome = cena.lista[i].nome
    cor = cena.lista[i].cor
    ax.plot(cena.matriz_x[i], cena.matriz_y[i], color = cor, label = nome)


def update(i):
    cena.atualizar()

    for i in range(len(cena.matriz_x)):
        nome = cena.lista[i].nome
        cor = cena.lista[i].cor
        
        ax.plot(cena.matriz_x[i], cena.matriz_y[i], color = cor, label = nome)    


ani = FuncAnimation(fig = fig, func = update, frames = 1000)


plt.legend()
plt.grid()
plt.show()

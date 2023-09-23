
class Vetor():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def __sub__(self, v):
        return Vetor(self.x - v.x, self.y - v.y)
    
    def __add__(self, v):
        return Vetor(self.x + v.x, self.y + v.y)
    
    def __mul__(self, k):
        return Vetor(self.x * k, self.y * k)
    
    def __truediv__(self, k):
        return Vetor(self.x / k, self.y / k)
    
    def __eq__(self, v):
        if isinstance(v, Vetor):
            return (self.x == v.x and self.y == v.y)

    def __ge__(self, v):
        if isinstance(v, Vetor):
            return (self.x >= v.x and self.y >= v.y)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    def normalizar(self):
        
        norma = (self.x**2 + self.y**2)**0.5

        return self / norma

    #Distancia entre dois pontos usando o operador >> entre dois Vetores
    def __rshift__(self, v):
        return ((v.x - self.x)**2 + (v.y - self.y)**2)**0.5



class Personagem:
    def __init__(self, nome, cor, origem, velocidade, 
                 direcao = None, alvo = None, trajetoria = None, loop = True):
        
        self.origem = origem
        self.nome = nome
        self.velocidade = velocidade
        self.ponto_atual = origem
        self.alvo = alvo
        self.direcao = direcao
        self.cor = cor
        self.trajetoria = trajetoria
        self.contador_trajetoria = 0
        self.loop = loop

        if trajetoria != None:
            self.alvo = self.trajetoria[self.contador_trajetoria]

        if alvo != None:
            if isinstance(alvo, Personagem):
                self.direcao = alvo.ponto_atual - self.ponto_atual
            
            if isinstance(alvo, Vetor):
                self.direcao = alvo - self.ponto_atual
        
    
    def __str__(self):
        resposta  = "Nome: " + self.nome
        resposta += "\nCor: " + self.cor
        resposta += "\nOrigem: " + str(self.origem)
        resposta += "\nVelocidade: " +  str(self.velocidade)
        resposta += "\nDireção: " +  str(self.direcao)
        
        if self.alvo != None:
            resposta += "\nAlvo: " +  self.alvo.nome
        else:
             resposta += "\nAlvo: " +  str(self.alvo)
        
        if self.trajetoria != None:
            resposta += "\nTrajetoria: tem" 

        return   resposta 

    def atualizar_direcao(self):
        
        if self.trajetoria != None:
            
            if self.ponto_atual == self.alvo and self.contador_trajetoria < len(self.trajetoria):
                self.ponto_atual = self.alvo

                self.contador_trajetoria += 1

                if self.contador_trajetoria >= len(self.trajetoria):
                    if self.loop == False:
                        self.velocidade = 0

                    self.contador_trajetoria = 0
                
                
                self.alvo = self.trajetoria[self.contador_trajetoria]
    

        if self.alvo != None:
            if isinstance(self.alvo, Personagem):
                self.direcao = self.alvo.ponto_atual - self.ponto_atual
            
            if isinstance(self.alvo, Vetor):
                self.direcao = self.alvo - self.ponto_atual


    def andar(self):
        self.atualizar_direcao()

        prox_step = self.ponto_atual + (self.direcao.normalizar() * self.velocidade)
        
        if isinstance(self.alvo, Vetor) and abs(self.ponto_atual >> prox_step) > abs(self.ponto_atual >> self.alvo):
            self.ponto_atual = self.alvo
        
        else:
            self.ponto_atual = prox_step

        #print(self.ponto_atual)
    
    def adicionar_alvo(self, p):
        self.alvo = p
    
    def adicionar_direcao(self, d):
        self.direcao = d
    
    def adicionar_trajetoria(self, t):
        self.trajetoria = t
        self.alvo = self.trajetoria[self.contador_trajetoria]


class Cenario:
    def __init__(self):
        self.matriz_x = []
        self.matriz_y = []
        self.lista = []
    
    def add(self, p):
        self.lista.append(p)
        self.matriz_x.append([p.ponto_atual.x])
        self.matriz_y.append([p.ponto_atual.y])
    
    def atualizar(self):
        for i in range(len(self.lista)):
            self.lista[i].andar()
            x = self.lista[i].ponto_atual.x
            y = self.lista[i].ponto_atual.y
            
            self.matriz_x[i].append(x)
            self.matriz_y[i].append(y)
    

    def __str__(self):
        resposta = ''

        for i in self.lista:
            resposta += str(i) + '\n\n'
                    
        return resposta
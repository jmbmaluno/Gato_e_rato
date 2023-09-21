
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

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"



class Personagem:
    def __init__(self, origem, velocidade, direcao = None, alvo = None):
        self.origem = origem
        self.velocidade = velocidade
        self.ponto_atual = origem
        self.alvo = alvo
        self.direcao = direcao

        if alvo != None:
            self.direcao = alvo.ponto_atual - self.ponto_atual
    
    def __str__(self):
        
        return "Origem: " + str(self.origem) + "\nVelocidade: " +  str(self.velocidade) + "\nDireção: " +  str(self.direcao)

    def atualizar_direcao(self):
        if self.alvo != None:
            self.direcao = self.alvo.ponto_atual - self.ponto_atual
    
    def andar(self):
        self.atualizar_direcao()
        self.ponto_atual = self.ponto_atual + (self.direcao * self.velocidade)




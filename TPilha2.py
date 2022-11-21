class Tpilha2:
    def __init__(self,capacidadepilha_n,capacidadepilha_p):
        self.capacidadepilha_n = capacidadepilha_n
        self.capacidadepilha_p = capacidadepilha_p
        self.pilha_n = []
        self.pilha_p = []

    def empilhar(self, vetor):
        valor_temporario = 0
        pilha_n = self.pilha_n
        pilha_p = self.pilha_p
        for valores_vetor in vetor:
            valor_temporario = valores_vetor
            tamanho_pilhap = len(pilha_p)
            tamanho_pilhan = len(pilha_n)
            if(valor_temporario > 0):
                pilha_p.append(valor_temporario)
            if(valor_temporario < 0):
                pilha_n.append(valor_temporario)
            else:
                if(valor_temporario == 0 and tamanho_pilhap > 0):
                    pilha_p.pop()
                if(valor_temporario == 0 and tamanho_pilhan > 0):
                    pilha_n.pop()

    def imprimir (self):
        return self.pilha_p,self.pilha_n



valores = Tpilha2(10,10)
(valores.empilhar([1,5,-3,0,-1]))
print(valores.imprimir())

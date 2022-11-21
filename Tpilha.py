class TPilha:
    
    def __init__(self,capacidade):
        self.capacidade = capacidade

    def empilhar(self,vetor):
        tamanho_vetor = len(vetor)
        tamanho_array = len(vetor)
        contador = 0
        self.pilha = []
        if (tamanho_vetor > self.capacidade):
            return "Tamanho do vetor maior que a capacidade, remova um elemento!"
        else:
            for i in vetor:
                valor_temporario = i
                contador += 1
                tamanho_pilha = len(self.pilha)
                if (contador <= tamanho_array):
                    if(valor_temporario % 2 == 1 and tamanho_pilha > 0):
                        self.pilha.pop()
                    else:
                        self.pilha.append(valor_temporario)
    def ver_topo(self):
        return self.pilha


array = TPilha(15)
array.empilhar([1,3,2,7,9,1,6,0,8,10,25,26,84,96,47])
print(array.ver_topo())
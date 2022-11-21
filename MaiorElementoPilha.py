class Pilha:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.pilha = []
    def empilhar(self,valor):
        pilha = self.pilha
        pilha.append(valor)
    def ver_topo(self):
        return self.pilha
    def maior(self):
        valores = self.pilha
        tamanho_pilha = len(valores)
        maior = 0
        if (tamanho_pilha == 0):
            return "Pilha Vazia !"
        elif (tamanho_pilha == self.capacidade):
            print("A pilha estourou, não é possivel adicionar mais itens.")
            for itens in valores:
                valor = itens
                if valor > maior:
                    maior = itens
            print("O numero maior da pilha é:")
            return maior










pilha = Pilha(4)
pilha.empilhar(300)
pilha.empilhar(400)
pilha.empilhar(2000)
pilha.empilhar(0)
print(pilha.maior())









import numpy as np

class Pilhas:
        def __init__(self, capacidade1, capacidade2):
            self.capacidade1 = capacidade1
            self.topo1 = -1
            self.valores1 = np.empty(self.capacidade1, dtype=int)
            self.capacidade2 = capacidade2
            self.topo2 = -1
            self.valores2 = np.empty(self.capacidade2, dtype=int)

        def empilhar(self,valor1,valor2):
            if self.topo1 == self.capacidade1 - 1:
                print("Pilha 1 cheia!")
            else:
                self.topo1 += 1
                self.valores1[self.topo1] = valor1

            if self.topo2 == self.capacidade2 - 1:
                print("Pilha 2 cheia")
            else:
                self.topo2 += 1
                self.valores2[self.topo2] = valor2


        def ver_topo(self):
            if(self.topo1 != -1 and self.topo2 != -1):
                return self.valores1, self.valores2

        def comparar_pilhas(self):
            if(self.capacidade1 != self.capacidade2):
                return "As pilhas não são iguais, suas capacidades são diferentes!"
            if(self.capacidade1 == self.capacidade2):
                if (self.valores1 == self.valores2).all():
                    return "São iguais!"
                else:
                    return "As pilhas não são iguais, seus valores são diferentes!"










pilhas = Pilhas(4,4)
pilhas.empilhar(1,1)
pilhas.empilhar(1,1)
pilhas.empilhar(1,1)
pilhas.empilhar(1,1)
print(pilhas.ver_topo())
print(pilhas.comparar_pilhas())






























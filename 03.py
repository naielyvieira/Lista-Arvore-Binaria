class No:
    def __init__(self, valor = None):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class Arvore_Binaria:
    def __init__(self):
        self.raiz = None
        
    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)

    def _inserir_em_nivel_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.direita)

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return False

        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivamente(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivamente(no_atual.direita, valor)

# Exemplo de uso
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(10)
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(15)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(12)
arvore.inserir_em_nivel(17)

print(arvore.buscar(7))
print(arvore.buscar(8))

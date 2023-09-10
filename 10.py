class No:
    def __init__(self, valor=None):
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

    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, no_atual):
        if no_atual is None:
            return 0

        altura_esquerda = self._calcular_altura(no_atual.esquerda)
        altura_direita = self._calcular_altura(no_atual.direita)

        return max(altura_esquerda, altura_direita) + 1

    def encontrar_valor_maximo(self):
        if self.raiz is None:
            return None
        else:
            return self._encontrar_valor_maximo_recursivamente(self.raiz)

    def _encontrar_valor_maximo_recursivamente(self, no_atual):
        if no_atual.direita is None:
            return no_atual.valor
        else:
            return self._encontrar_valor_maximo_recursivamente(no_atual.direita)

# Exemplo de uso:
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(50)
arvore.inserir_em_nivel(30)
arvore.inserir_em_nivel(70)
arvore.inserir_em_nivel(20)
arvore.inserir_em_nivel(40)
arvore.inserir_em_nivel(60)
arvore.inserir_em_nivel(80)

valor_maximo = arvore.encontrar_valor_maximo()
print(valor_maximo)

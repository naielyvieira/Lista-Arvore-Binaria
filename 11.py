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

    def mostrar_in_ordem(self):
        valores = []
        if self.raiz is None:
            print('A árvore está vazia!')
        else:
            self._mostrar_in_ordem_recursivo(self.raiz, valores)
        return valores

    def _mostrar_in_ordem_recursivo(self, no, valores):
        if no is not None:
            self._mostrar_in_ordem_recursivo(no.esquerda, valores)
            valores.append(no.valor)
            self._mostrar_in_ordem_recursivo(no.direita, valores)

    def e_arvore_busca_valida(self):
        valores = self.mostrar_in_ordem()
        return self._e_ordenado_crescente(valores)

    def _e_ordenado_crescente(self, valores):
        for i in range(1, len(valores)):
            if valores[i] <= valores[i - 1]:
                return False
        return True

# Exemplo de uso:
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(10)
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(15)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(12)
arvore.inserir_em_nivel(20)
arvore.inserir_em_nivel(22)

e_valida = arvore.e_arvore_busca_valida()
print(e_valida)
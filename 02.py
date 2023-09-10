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
                
# Exemplo de uso:
if __name__ == "__main__":
    arvore = Arvore_Binaria()
    numeros = [8, 9, 10, 2, 12 ,13, 14, 20]

    for numero in numeros:
        arvore.inserir_em_nivel(numero)

    print("\nÁrvore Binária")
    print("\n", numeros, "\n")
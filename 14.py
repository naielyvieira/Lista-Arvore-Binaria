class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class Arvore_Binaria:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir_em_nivel(self, valor):
        if self.valor is None:
            self.valor = valor
        else:
            self._inserir_em_nivel_recursivo(valor, self)

    def _inserir_em_nivel_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Arvore_Binaria(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = Arvore_Binaria(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.direita)

    def encontrar_caminho_para_no(self, valor_alvo):
        caminho = self._encontrar_caminho_recursivamente(self, valor_alvo, [])
        return caminho

    def _encontrar_caminho_recursivamente(self, no_atual, valor_alvo, caminho_atual):
        if no_atual is None:
            return []

        caminho_atual.append(no_atual.valor)

        if no_atual.valor == valor_alvo:
            return caminho_atual

        if valor_alvo < no_atual.valor:
            caminho_esquerda = self._encontrar_caminho_recursivamente(no_atual.esquerda, valor_alvo, caminho_atual.copy())
            if caminho_esquerda:
                return caminho_esquerda

        if valor_alvo > no_atual.valor:
            caminho_direita = self._encontrar_caminho_recursivamente(no_atual.direita, valor_alvo, caminho_atual.copy())
            if caminho_direita:
                return caminho_direita

        return []

# Exemplo de uso:
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(50)
arvore.inserir_em_nivel(30)
arvore.inserir_em_nivel(70)
arvore.inserir_em_nivel(20)
arvore.inserir_em_nivel(40)
arvore.inserir_em_nivel(60)
arvore.inserir_em_nivel(80)

valor_alvo = 80
caminho = arvore.encontrar_caminho_para_no(valor_alvo)

print(f"Caminho para o nó {valor_alvo}: {caminho}")  # Isso imprimirá o caminho da raiz até o nó com o valor.

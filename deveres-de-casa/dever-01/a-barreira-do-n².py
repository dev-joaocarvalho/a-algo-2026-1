"""
Módulo para comparação empírica de algoritmos de ordenação.

Resolve o dever de casa sobre a barreira do n^2, comparando
a eficiência do Insertion Sort com a função nativa sorted() do Python
para identificar o ponto de ruptura assintótico.
"""

import random
import time

# Constantes em SCREAMING_SNAKE_CASE
TAMANHOS_N = [1000, 5000, 10000, 20000, 50000]


class ComparadorOrdenacao:
    """
    Classe responsável por gerenciar e executar a comparação de algoritmos.
    
    Encapsula os métodos de ordenação e as rotinas de medição de tempo
    para o experimento empírico.
    """

    @staticmethod
    def insertion_sort(lista_entrada):
        """
        Ordena uma lista utilizando o algoritmo Insertion Sort O(n^2).
        
        Não altera a lista original para garantir testes justos subsequentes.
        
        Args:
            lista_entrada (list): A lista de elementos numéricos a ser ordenada.
            
        Returns:
            list: Uma nova lista com os elementos ordenados de forma crescente.
        """
        lista_ordenada = lista_entrada.copy()
        tamanho_lista = len(lista_ordenada)
        
        for indice_atual in range(1, tamanho_lista):
            chave = lista_ordenada[indice_atual]
            indice_anterior = indice_atual - 1
            
            while indice_anterior >= 0 and chave < lista_ordenada[indice_anterior]:
                lista_ordenada[indice_anterior + 1] = lista_ordenada[indice_anterior]
                indice_anterior -= 1
                
            lista_ordenada[indice_anterior + 1] = chave
            
        return lista_ordenada

    @staticmethod
    def medir_tempo(funcao_ordenacao, lista_dados):
        """
        Mede o tempo de execução de uma função de ordenação específica.
        
        Args:
            funcao_ordenacao (callable): A função de ordenação a ser testada.
            lista_dados (list): A lista de dados de entrada para a função.
            
        Returns:
            float: O tempo total de execução medido em segundos.
        """
        tempo_inicio = time.time()
        funcao_ordenacao(lista_dados)
        tempo_fim = time.time()
        
        return tempo_fim - tempo_inicio

    def executar_experimento(self):
        """
        Gera listas aleatórias e executa a comparação empírica de tempos.
        
        Itera sobre os tamanhos definidos na constante TAMANHOS_N, gera
        valores aleatórios e imprime o tempo de execução de cada algoritmo
        no terminal.
        """
        print("Iniciando a comparação empírica: Insertion Sort vs Timsort...\n")
        
        for tamanho in TAMANHOS_N:
            print(f"--- Tamanho da entrada (n) = {tamanho} ---")
            
            # Gera a lista com valores inteiros aleatórios
            lista_teste = [random.randint(0, 100000) for _ in range(tamanho)]
            
            # Medição do Insertion Sort O(n^2)
            tempo_insertion = self.medir_tempo(self.insertion_sort, lista_teste)
            print(f"Insertion Sort O(n^2)    : {tempo_insertion:.4f} segundos")
            
            # Medição do Timsort (função nativa sorted) O(n log n)
            tempo_timsort = self.medir_tempo(sorted, lista_teste)
            print(f"Timsort nativo O(n log n): {tempo_timsort:.4f} segundos\n")


if __name__ == "__main__":
    comparador = ComparadorOrdenacao()
    comparador.executar_experimento()


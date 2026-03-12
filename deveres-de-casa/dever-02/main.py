
"""
Módulo para cálculo de fatorial recursivo e análise empírica de tempo.

Este script implementa o algoritmo de fatorial utilizando recursão e
mede seu tempo de execução para diferentes tamanhos de entrada,
auxiliando na avaliação do crescimento de tempo.
"""

import sys
import time

# Constante com os valores de entrada definidos no exercício
VALORES_TESTE_N = [10, 100, 500, 1000]

# O limite padrão de recursão do Python é 1000. 
# Para calcular o fatorial de 1000 em segurança, aumentamos esse limite.
sys.setrecursionlimit(2000)


class AnalisadorFatorial:
    """
    Classe responsável por encapsular o cálculo do fatorial 
    e a medição do tempo de execução do algoritmo.
    """

    @staticmethod
    def calcular_fatorial_recursivo(n):
        """
        Calcula o fatorial de um número inteiro de forma recursiva.
        
        Args:
            n (int): O número inteiro base para o cálculo.
            
        Returns:
            int: O valor do fatorial de n.
        """
        # Caso base: o fatorial de 0 ou 1 é sempre 1
        if n <= 1:
            return 1
            
        # Passo recursivo: multiplica n pelo fatorial de n - 1
        return n * AnalisadorFatorial.calcular_fatorial_recursivo(n - 1)

    def executar_experimento(self):
        """
        Mede e exibe no terminal o tempo de execução do algoritmo para 
        diferentes valores de n, permitindo a análise empírica.
        """
        print("Iniciando medição de tempo para o Fatorial Recursivo...\n")
        
        for valor in VALORES_TESTE_N:
            tempo_inicio = time.time()
            
            # Chamada da função recursiva
            self.calcular_fatorial_recursivo(valor)
            
            tempo_fim = time.time()
            tempo_total = tempo_fim - tempo_inicio
            
            print(f"Tempo para n = {valor:>4}: {tempo_total:.6f} segundos")


if __name__ == "__main__":
    analisador = AnalisadorFatorial()
    analisador.executar_experimento()

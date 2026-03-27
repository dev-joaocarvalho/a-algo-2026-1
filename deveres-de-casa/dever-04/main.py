"""
Module for calculating mathematical recurrence functions.

This script solves the recurrence equation F(n) = 2F(n-1) + n^2
through both simple recursion and its closed-form formula,
using the math library.
"""

import math

# SCREAMING_SNAKE_CASE for configuration constants
VALOR_CASO_BASE = 2


def calcular_funcao_recursiva(valor_n):
    """
    Calculates F(n) using recursive calls.

    The time complexity of this function is exponential, growing 
    at a rate of O(2^n). It is not recommended for high values of n.

    Args:
        valor_n (int): The numerical value of n.

    Returns:
        int: The result of the recursive calculation.
    """
    if valor_n <= 1:
        return VALOR_CASO_BASE
    
    return 2 * calcular_funcao_recursiva(valor_n - 1) + (valor_n ** 2)


def calcular_formula_fechada(valor_n):
    """
    Calculates F(n) using the exact mathematical closed-form solution.

    The closed formula for the recurrence is: F(n) = 13 * 2^(n-1) - n^2 - 4n - 6.
    The time complexity drops drastically to O(1).

    Args:
        valor_n (int): The numerical value of n.

    Returns:
        int: The exact mathematical result of the operation.
    """
    # math.pow returns a float, so we convert it back to int at the end
    termo_exponencial = 13 * math.pow(2, valor_n - 1)
    termo_polinomial = math.pow(valor_n, 2) + (4 * valor_n) + 6
    
    resultado_final = termo_exponencial - termo_polinomial
    return int(resultado_final)


if __name__ == "__main__":
    print("=== Recurrence Calculator F(n) ===")
    print("Warning: Due to O(2^n) exponential complexity, avoid high values.\n")
    
    # snake_case for main flow variables
    entrada_usuario = input("Enter an integer value for n (e.g., 3, 5, 10): ")
    
    try:
        numero_n = int(entrada_usuario)
        
        if numero_n < 1:
            print("Please enter a value greater than or equal to 1 (base case).")
        else:
            resultado_recursao = calcular_funcao_recursiva(numero_n)
            resultado_matematico = calcular_formula_fechada(numero_n)
            
            print(f"\nResults for F({numero_n}):")
            print(f"Via Recursion:      {resultado_recursao}")
            print(f"Via Formula (math): {resultado_matematico}")
            
    except ValueError:
        print("Error: Invalid input. Make sure to enter an integer.")

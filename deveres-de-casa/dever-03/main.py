"""
Palindrome verification.

Recursive implementation to determine if a linear data structure (such as an array/list) is a palindrome.
"""

def verificar_palindromo_recursivo(array_entrada, indice_inicio=0, indice_fim=None):
    """
    Recursively checks if an array is a palindrome.

    Args:
        array_entrada (list): The list of elements to be checked.
        indice_inicio (int, optional): The starting index for the check. Defaults to 0.
        indice_fim (int, optional): The ending index for the check. Defaults to None.

    Returns:
        bool: True if the array is a palindrome, False otherwise.
    """
    # Sets the ending index on the first function call
    if indice_fim is None:
        indice_fim = len(array_entrada) - 1

    # Base Case 1: If the indices cross or equal each other, we've read everything. It's a palindrome!
    if indice_inicio >= indice_fim:
        return True

    # Base Case 2: If the elements at opposite ends are different, it is not a palindrome.
    if array_entrada[indice_inicio] != array_entrada[indice_fim]:
        return False

    # Recursive Step: Checks the "core" of the array, bringing the pointers closer
    return verificar_palindromo_recursivo(
        array_entrada, 
        indice_inicio + 1, 
        indice_fim - 1
    )


if __name__ == "__main__":
    # Example arrays provided in your request
    array_exemplo_1 = [0, 1, 2, 3, 2, 1, 0]
    array_exemplo_2 = ["a", "b", "b", "a"]
    array_exemplo_3 = ["a", "b", "c", "b", "a"]
    array_exemplo_4 = ["a", "b", "c", "f", "b", "a"]

    # snake_case for the list that will iterate through the tests
    lista_de_testes = [
        array_exemplo_1,
        array_exemplo_2,
        array_exemplo_3,
        array_exemplo_4
    ]

    # Validation and printing of results
    for array_teste in lista_de_testes:
        resultado = verificar_palindromo_recursivo(array_teste)
        mensagem = "Is a palindrome" if resultado else "Not a palindrome"
        print(f"{array_teste} -> {mensagem}")

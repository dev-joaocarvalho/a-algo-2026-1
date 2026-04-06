"""
Module for demonstrating specific recurrence relations.

This script applies the Master Theorem logic to solve the exact three 
recurrences provided in the user's image. The mathematical proofs and 
answers are detailed in the block comments before the execution.
"""

import math

# SCREAMING_SNAKE_CASE for constant values
FLOAT_TOLERANCE = 1e-9


class MasterTheoremAnalyzer:
    """
    Analyzer for recurrence relations using the Master Theorem.

    Attributes:
        value_a (float): Number of subproblems.
        value_b (float): Subproblem size reduction factor.
        value_k (float): Polynomial exponent in f(n).
        value_p (float): Logarithmic exponent in f(n).
    """

    def __init__(self, value_a, value_b, value_k, value_p=0.0):
        """Initializes the analyzer with the recurrence parameters."""
        self.value_a = value_a
        self.value_b = value_b
        self.value_k = value_k
        self.value_p = value_p

    def evaluate_recurrence(self):
        """
        Evaluates the recurrence to find the matching Master Theorem case.

        Returns:
            tuple: A tuple containing the case number (int) and the 
                   asymptotic complexity (str).
        """
        log_b_a = math.log(self.value_a, self.value_b)

        if self.value_k < log_b_a - FLOAT_TOLERANCE:
            return 1, f"Θ(n^{log_b_a:g})"

        elif math.isclose(self.value_k, log_b_a, abs_tol=FLOAT_TOLERANCE):
            new_p = self.value_p + 1
            log_part = f" * log^{new_p:g}(n)" if new_p > 0 else ""
            return 2, f"Θ(n^{self.value_k:g}{log_part})"

        else:
            log_part = f" * log^{self.value_p:g}(n)" if self.value_p > 0 else ""
            return 3, f"Θ(n^{self.value_k:g}{log_part})"


if __name__ == "__main__":
    print("=== Resolução das Recorrências da Imagem ===\n")

    """
    -------------------------------------------------------------------
    RECURRENCE 1: T(n) = 2T(n/4) + sqrt(n)
    -------------------------------------------------------------------
    - sqrt(n) is mathematically equivalent to n^(0.5).
    - Parameters: a = 2, b = 4, k = 0.5, p = 0.
    - Critical exponent: log_4(2) = 0.5.
    - Comparison: f(n) = n^0.5 is exactly equal to n^(log_b a).
    - Conclusion: This falls under Master Theorem Case 2.
    - ANSWER: Complexity is Θ(n^(0.5) * log(n)) or Θ(sqrt(n) * log(n)).
    -------------------------------------------------------------------
    """
    analyzer_case_1 = MasterTheoremAnalyzer(value_a=2, value_b=4, value_k=0.5)
    case_1, complexity_1 = analyzer_case_1.evaluate_recurrence()
    print("1) T(n) = 2T(n/4) + √n")
    print(f"   -> Teorema Mestre (Caso {case_1}): Complexidade {complexity_1}\n")


    """
    -------------------------------------------------------------------
    RECURRENCE 2: T(n) = 2T(n/4) + n
    -------------------------------------------------------------------
    - Parameters: a = 2, b = 4, k = 1, p = 0.
    - Critical exponent: log_4(2) = 0.5.
    - Comparison: f(n) = n^1 is polynomially larger than n^0.5.
    - Conclusion: This falls under Master Theorem Case 3.
    - ANSWER: Complexity is Θ(n^1) or simply Θ(n).
    -------------------------------------------------------------------
    """
    analyzer_case_2 = MasterTheoremAnalyzer(value_a=2, value_b=4, value_k=1.0)
    case_2, complexity_2 = analyzer_case_2.evaluate_recurrence()
    print("2) T(n) = 2T(n/4) + n")
    print(f"   -> Teorema Mestre (Caso {case_2}): Complexidade {complexity_2}\n")


    """
    -------------------------------------------------------------------
    RECURRENCE 3: T(n) = 16T(n/4) + n^2
    -------------------------------------------------------------------
    - Parameters: a = 16, b = 4, k = 2, p = 0.
    - Critical exponent: log_4(16) = 2.
    - Comparison: f(n) = n^2 is exactly equal to n^(log_b a).
    - Conclusion: This falls under Master Theorem Case 2.
    - ANSWER: Complexity is Θ(n^2 * log(n)).
    -------------------------------------------------------------------
    """
    analyzer_case_3 = MasterTheoremAnalyzer(value_a=16, value_b=4, value_k=2.0)
    case_3, complexity_3 = analyzer_case_3.evaluate_recurrence()
    print("3) T(n) = 16T(n/4) + n^2")
    print(f"   -> Teorema Mestre (Caso {case_3}): Complexidade {complexity_3}\n")

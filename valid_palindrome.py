"""

Problema: Dado una cadena (o arreglo de caracteres),
determina si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
Considera solo letras y números, ignorando mayúsculas.

Entrada: "Aman a Panama" (Simplificado a: "amanapanama")

Salida: true

"""

def valid_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1
    is_valid = True

    while start <= end:
        if s[start] != s[end]:
            is_valid = False
            break

        start += 1
        end -= 1

    return is_valid

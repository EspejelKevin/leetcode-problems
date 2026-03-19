"""

Two Sum II (Arreglo Ordenado)
Problema: Se te da un arreglo de números enteros que ya está ordenado de menor a mayor.
Encuentra dos números que sumen un objetivo (target) específico. Debes devolver los índices (sumando 1 a cada uno).

Entrada: nums = [2, 7, 11, 15], target = 9

Salida: [1, 2] (porque 2 + 7 = 9)

Pista: Si la suma de tus punteros es menor al objetivo,
¿cuál puntero deberías mover para que la suma aumente? Si es mayor, ¿cuál mueves para que disminuya?

"""

def two_sum_ii(target: int, arr: list[int]) -> list[int]:
    start = 0
    end = len(arr) - 1

    while start <= end:
        _sum = arr[start] + arr[end]

        if _sum == target:
            return [start+1, end+1]
        
        if _sum > target:
            end -= 1
        else:
            start += 1

    return []

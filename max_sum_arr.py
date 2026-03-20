"""

Suma Máxima de Subarreglo (Tamaño Fijo)

Problema: Dado un arreglo de números y un entero k, encuentra la suma máxima de cualquier subarreglo de tamaño exactamente k.

Entrada: nums = [2, 1, 5, 1, 3, 2], k = 3
1, 5, 15, 1, 3,
Salida: 9 (porque [5, 1, 3] es la suma más alta).

Pista: No sumes los 3 elementos en cada paso. Suma el nuevo elemento que entra a la derecha y resta el que sale por la izquierda.

"""

def max_sum_arr(arr, k):
    # start = 0, k = 3

    # tomo el primer sub arreglo

    # arr[start:k] -> [2, 1, 5]

    # sumo 2 + 1 + 5 = 8

    # suma_maxima es 8, de momento

    # a start le sumo 1, start = 1

    # a k, le sumo 1, k = 4

    # arr[start:k] -> [1, 5, 1]

    # sumo 1 + 5 + 1 = 7

    # comparo, la nueva suma > suma_maxima (previa) -> 7 > 8, no es cierto, entonces se mantiene el valor de 8

    # a start le sumo 1, start = 2

    # a k, le sumo 1, k = 5

    # arr[start:k] -> [5, 1, 3] 

    # sumo 5 + 1 + 3 = 9
    
    # comparo, nueva_suma > suma_maxima -> 9 > 8, es cierto, actualizo el valor de suma_maxima a 9

    # a start le sumo 1, start 3

    # a k, le sumo 1, k = 6

    # arr[start:k] -> [1, 3, 2]

    # sumo 1 + 3 + 2 = 6

    # comparo, nueva_suma > suma_maxima -> 6 > 9, no es cierto, entonces se mantiene el valor de 9

    # ya no hay mas iteraciones porque k <= len(arr), return suma_maxima

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)

    return max_sum

print(max_sum_arr([2, 1, 5, 1, 3, 2], k = 3))
"""

Encontrar el Índice de Pivote

Problema: Encuentra el índice donde la suma de los números a su izquierda sea igual a la suma de los números a su derecha.

Entrada: nums = [1, 7, 3, 1, 6, 1, 5, 6]

Salida: 3 (porque a la izquierda de 6 está 1+7+3 = 11 y a la derecha 5+6 = 11).

Pista: Calcula la suma total primero. Mientras recorres, mantén una "suma izquierda".
       La "suma derecha" es simplemente Total - Suma Izquierda - Valor Actual

"""

def find_pivote(nums):
    sum_total = sum(nums)

    sum_left = 0

    for i in range(len(nums)):
        sum_right = sum_total - sum_left - nums[i]

        if sum_left == sum_right:
            return i
        
        sum_left += nums[i]
        
    return -1


    # sum_total = 28

    # sum_izq = 1

    # sum_der = 28 - 1 - 7 = 20

    # sum_izq = 8

    # sum_der = 28 - 8 - 3 = 17

    # sum_izq = 11

    # sum_der = 28 - 11 - 6 = 11


print(find_pivote([1, 7, 3, 1, 6, 1, 5, 6]))
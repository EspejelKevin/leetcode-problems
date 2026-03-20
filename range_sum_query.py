"""

Suma de Rango (Range Sum Query)

Problema: Dado un arreglo de números, prepara una estructura que permita responder varias consultas de tipo "Suma desde el índice L hasta el R".

Entrada: nums = [1, 2, 3, 4, 5], Consultas: (0, 2), (2, 4)

Salida: Para (0, 2) →6. Para (2, 4) →12.

Reto: Intenta crear el arreglo de prefijos primero y luego úsalo para responder las consultas sin usar ciclos for adicionales.

Suma(i,j) = P[j] - P[i-1]

"""

def range_sum_query(nums: list, queries):
    output = []
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum += nums[i]
        nums[i] = current_sum

    for i, j in queries:
        if i == 0:
            output.append(nums[j])
        else:
            output.append((nums[j] - nums[i-1]))

    return output

print(range_sum_query([1, 2, 3, 4, 5], [(0, 2), (2, 4), (1, 3)]))
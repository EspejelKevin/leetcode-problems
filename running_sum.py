"""

Correr de Ganancias (Running Sum)

Problema: Dado un arreglo nums, devuelve un arreglo que sea la suma acumulada en cada paso. (Este es el ejercicio más básico para soltar la mano).

    Entrada: [1, 1, 1, 1, 1]

    Salida: [1, 2, 3, 4, 5]

"""

def running_sum(nums):
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum += nums[i]
        nums[i] = current_sum
    
    return nums


print(running_sum([1, 1, 1, 1, 1]))
"""

Subarreglo más pequeño con suma mayor a 'S' (Tamaño Variable)

Problema: Dado un arreglo de números positivos y un valor target,
          encuentra la longitud mínima de un subarreglo cuya suma sea mayor o igual a target. Si no existe, devuelve 0.

Entrada: nums = [2, 3, 1, 2, 4, 3], target = 7

Salida: 2 (el subarreglo [4, 3] suma 7 y es el más corto).

Pista: Aquí la ventana crece por la derecha hasta alcanzar el target,
       y luego se encoge por la izquierda para ver si puedes mantener la suma con menos elementos.

"""

def min_arr_with_max_sum_to_s(arr, target):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            current_len = (right - left) + 1
            min_len = min(min_len, current_len)

            current_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0


    # left = 0
    # right = 1
    # min_len = len(arr)

    # arr[left: right] -> [2]

    # sum([2]) = 2 

    # comparo, 2 >= 7, false
        # entonces, aumento right en 1, right = 2

    # arr[left: right] -> [2, 3]

    # sum([2, 3]) = 5

    # comparo, 5 >= 7, false
        # entonces, aumento right en 1, right = 3

    # arr[left: right] -> [2, 3, 1]

    # sum([2, 3, 1]) = 6

    # comparto 6 >= 7, false
        # entonces, aumento right en 1, right = 4

    # arr[left: right] -> [2, 3, 1, 2]

    # sum([2, 3, 1, 2]) = 8

    # comparo 8 >= 7, true
        # entonces
            # len([2, 3, 1, 2]) < min_len, true
                # entonces, min_len = len([2, 3, 1, 2])

            # resto sum([2, 3, 1, 2]) - (arr[left] -> 2) = 6

            # a left lo aumento en 1, left = 1
        
            # comparo, 6 >= 7, false
                # entonces, no cambio el valor de min_len y aumento right en 1, right = 5

    # arr[left: right] -> [3, 1, 2, 4]

    # sum([3, 1, 2, 4]) = 10

    # comparo 10 >= 7, true
        # entonces
            # len([3, 1, 2, 4]) < min_len, false
                # entonces, no muevo el valor de min_len
            
            # resto sum([3, 1, 2, 4]) - (arr[left] -> 3) = 7

            # a left lo aumento en 1, left = 2

            # comparo 7 >= 7, true
                # entonces
                    # len([1, 2, 4]) < min_len, true
                        # entonces, min_len = len([1, 2, 4])

                    # resto sum([1, 2, 4]) - (arr[left] -> 1) = 6

                    # a left lo aumento en 1, left = 3

                    # comparto 6 >= 7, false
                        # entonces, no cambio el valor de min_len y aumento right en 1, right = 6
    
    # arr[left: right] -> [2, 4, 3]

    # sum([2, 4, 3]) = 9

    # comparto 9 >= 7, true
        # entonces
            # len([2, 4, 3]) < min_len, false
                # entonces, no muevo el valor de min_len

            # resto sum([2, 4, 3]) - (arr[left] -> 2) = 7

            # a left lo aumento en 1, left = 4

            # comparto 7 >= 7, true
                # entonces
                    # len([4, 3]) < min_len, true
                        # entonces, min_len = len([4, 3])

                    # resto sum([4, 3]) - (arr[left] -> 4) = 3

                    # a left lo aumento en 1, left = 5

                    # comparto 3 >= 7, false
                        # entonces, no cambio el valor de min_len y aumento right en 1, right = 7

    # termina porque right ya es mayor a len(arr)

    # return min_len
    
print(min_arr_with_max_sum_to_s([2, 3, 1, 2, 4, 3], target=7))

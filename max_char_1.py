"""

Máximo de caracteres "1" tras un cambio

Problema: Tienes un arreglo de solo 0s y 1s. Puedes cambiar como máximo un 0 por un 1.
¿Cuál es la longitud máxima de una secuencia de 1s que puedes lograr?

Entrada: nums = [1, 0, 1, 1, 0]

Salida: 4 (si cambias el primer cero, obtienes [1, 1, 1, 1]).

Pista: Tu ventana puede contener como máximo un 0. Si entra un segundo 0,
debes encoger la ventana por la izquierda hasta que vuelva a haber solo uno.

"""

def max_char_1(nums):
    left = 0
    right = 0
    max_len = 0
    count_zeros = 0

    while right < len(nums):
        elem = nums[right]

        if elem == 0:
            count_zeros += 1
        
        if count_zeros > 1:
            while nums[left] == 1:
                left += 1

            left += 1
            count_zeros = 1

        current_len = (right - left) + 1
        max_len = max(max_len, current_len)

        right += 1


    return max_len

    # left = 0
    # current_pos = 0
    # max_len = 0
    # contador_de_ceros = 0

    # tomo el primer elemento de la lista -> 1

    # verifico si es 0 o 1, es 1

        # mi longitud es 1

    # entonces, avanzo mi ventana

    # verifico si es 0 o 1, es 0

    # entonces aumento mi contador de ceros, contador_de_ceros = 1

        # mi ventana actual es -> [1, 0]

        # mi longitud es 2

    # avanzo mi ventana -> [1, 0, 1]

    # verifico si es 0 o 1, es 1

        # mi longitud es 3

    # entonces, avanzo mi ventana -> [1, 0, 1, 1]

    # verifico si es 0 o 1, es 1

        # mi longitud es 4

    # avanzo mi ventana -> [1, 0, 1, 1, 0]

    # verifico si es 0 o 1, es 0

    # entonces aumento mi contador de ceros, contador_de_ceros = 2

    # if contador_de_ceros > 1
        # entonces debo reducir mi ventana con left, hasta que left sea igual a 0, cuando lo encuentre, entonces mi left valdra esa pos+1
        # mi contador debo reducirlo a 1, contador_de_ceros = 1

    # cuando current_pos sea igual a la len de arr, termina mi recorrido

    # retorno max_len

    

print(max_char_1([1, 0, 1, 1, 0]))
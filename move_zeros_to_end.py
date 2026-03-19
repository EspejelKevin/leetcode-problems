"""

Mover Ceros al Final
Problema: Dado un arreglo de números, mueve todos los 0 al final del mismo,
manteniendo el orden relativo de los demás números. Debes hacerlo in-place (sin crear un arreglo nuevo).

Entrada: [0, 1, 0, 3, 12]

Salida: [1, 3, 12, 0, 0]

Pista: Aquí los dos punteros van en la misma dirección.
Un puntero (i) recorre todo el arreglo.
El otro puntero (posicionEscritura) solo avanza cuando encuentras un número que no es cero para "escribirlo" en esa posición.

"""

def move_zeros(arr: list[int]) -> list[int]:
    # Entrada: [0, 1, 0, 3, 12]
        
        # iniciar variables: start = 0, end = 0

        # avanzo end en 1: start = 0, end = 1

        # intercambio valores
        # arr[start] = 1
        # arr[end] = 0

        # resultado
        # [1, 0, 0, 3, 12]

        # aumento en 1 start: start = 1
        # arr[start] es igual a 0: start no lo muevo

        # como ya movi start a la posicion de end, tengo que mover end en 1: end = 2
        # arr[end] es distinto a 0: end no lo muevo

        # [1, 0, 0, 3, 12]
            # s  e

        # ambos son ceros, pero start no lo muevo, end si lo muevo en 1: end = 3

        # [1, 0, 0, 3, 12]
        #     s     e

        # arr[end] ahora es != 0

        # realizo el intercambio:

        # arr[start] = 3
        # arr[end] = 0

        # resultado        
        # [1, 3, 0, 0, 12]
        #     s     e

        # los valores actuales son: start = 1, end = 3

        # arr[start] ahora es 3, por lo cual lo tengo que aumentar en 1: start = 2
        # arr[end] ahora es 0, por lo cual lo tengo que aumentar en 1: end = 4

        # valores actuales: arr[start] = 0, arr[end] = 12

        # como arr[start] es cero, no lo muevo y tampoco arr[end] porque es != 0

        # [1, 3, 0, 0, 12]
        #        s      e

        # ahora hago el intercambio

        # arr[start] = 12
        # arr[end] = 0

        # resultado
        # [1, 3, 12, 0, 0]

    pos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1
    
    return arr

print(move_zeros([0, 1, 1, 1, 1, 1]))

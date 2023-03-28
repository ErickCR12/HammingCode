# Definimos la funcion para calcular el codigo hamming
def hamming(mensaje):
    # Creamos una lista para guardar el mensaje
    lista = []
    listaF = []

    # Recorremos el mensaje y lo guardamos en la lista
    for i in mensaje:
        lista.append(i)

    # Calculamos los bits de paridad
    p1 = int(lista[0]) ^ int(lista[1]) ^ int(lista[3]) ^ int(lista[4]) ^ int(lista[6]) ^ int(lista[8]) ^ int(
        lista[10])  # Correcto
    p2 = int(lista[0]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[9]) ^ int(
        lista[10])  # Correcto
    p4 = int(lista[1]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[7]) ^ int(lista[8]) ^ int(lista[9]) ^ int(
        lista[10])  # Correcto
    p8 = int(lista[4]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[7]) ^ int(lista[8]) ^ int(lista[9]) ^ int(
        lista[10])  # Correcto

    # Imprimimos el mensaje original
    print("Mensaje original: " + mensaje)

    # Imprimimos el mensaje con los bits de paridad
    print(
        "Mensaje con bits de paridad: " + str(p1) + str(p2) + lista[0] + str(p4) + lista[1] + lista[2] + lista[3] + str(
            p8) + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10])

    # Calculamos el codigo hamming
    codigo = str(p1) + str(p2) + lista[0] + str(p4) + lista[1] + lista[2] + lista[3] + str(p8) + lista[4] + lista[5] + \
             lista[6] + lista[7] + lista[8] + lista[9] + lista[10]

    # Imprimimos el codigo hamming
    print("Codigo hamming: " + codigo)

    for i in codigo:
        listaF.append(i)

    MH = [[" ", " ", lista[0], " ", lista[1], lista[2], lista[3], " ", lista[4], lista[5], lista[6], lista[7], lista[8],
           lista[9], lista[10]],
          [str(p1), 0, lista[0], 0, lista[1], 0, lista[3], 0, lista[4], 0, lista[6], 0, lista[8], 0, lista[10]],
          [0, str(p2), lista[0], 0, 0, lista[2], lista[3], 0, 0, lista[5], lista[6], 0, 0, lista[9], lista[10]],
          [0, 0, 0, str(p4), lista[1], lista[2], lista[3], 0, 0, 0, 0, lista[7], lista[8], lista[9], lista[10]],
          [0, 0, 0, 0, 0, 0, 0, str(p8), lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]],
          [listaF[0], listaF[1], listaF[2], listaF[3], listaF[4], listaF[5], listaF[6], listaF[7], listaF[8], listaF[9], listaF[10], listaF[11], listaF[12], listaF[13], listaF[14]]]

    print(MH)

    # Retornamos el codigo hamming
    return MH




# Genere una funcion que permita calcular el mensaje original a partir del codigo hamming
def mensaje(codigo):
    # Creamos una lista para guardar el codigo
    lista = []

    # Recorremos el codigo y lo guardamos en la lista
    for i in codigo:
        lista.append(i)

    # Calculamos los bits de paridad
    p1 = int(lista[0]) ^ int(lista[2]) ^ int(lista[4]) ^ int(lista[6]) ^ int(lista[8]) ^ int(lista[10]) ^ int(
        lista[12]) ^ int(lista[14])  # Correcto
    p2 = int(lista[1]) ^ int(lista[2]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[9]) ^ int(lista[10]) ^ int(
        lista[13]) ^ int(lista[14])  # Correcto
    p4 = int(lista[3]) ^ int(lista[4]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[11]) ^ int(lista[12]) ^ int(
        lista[13]) ^ int(lista[14])  # Correcto
    p8 = int(lista[7]) ^ int(lista[8]) ^ int(lista[9]) ^ int(lista[10]) ^ int(lista[11]) ^ int(lista[12]) ^ int(
        lista[13]) ^ int(lista[14])  # Correcto

    # Calculamos el error
    error = str(p1) + str(p2) + str(p4) + str(p8)

    # Imprimimos el mensaje original
    print(
        "Mensaje original: " + lista[2] + lista[4] + lista[5] + lista[6] + lista[8] + lista[9] + lista[10] + lista[11] +
        lista[12] + lista[13] + lista[14])

    # Imprimimos el error
    print("Error: " + error)

    # Retornamos el mensaje original
    return lista[2] + lista[4] + lista[5] + lista[6] + lista[8] + lista[9] + lista[10] + lista[11] + lista[12] + lista[
        13] + lista[14]


hamming("11001001010")
#hamming("10101010101")
#mensaje("101110011001010")
#mensaje("101101001010101")

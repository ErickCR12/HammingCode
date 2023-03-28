# Definimos la funcion para calcular el codigo hamming
def hamming(mensaje):
    # Creamos una lista para guardar el mensaje
    lista = list(mensaje)
    listaF = []

    # Calculamos los bits de paridad
    p1 = int(lista[0]) ^ int(lista[1]) ^ int(lista[3]) ^ int(lista[4]) ^ int(lista[6]) ^ int(lista[8]) ^ int(
        lista[10])  # Correcto
    p2 = int(lista[0]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[9]) ^ int(
        lista[10])  # Correcto
    p4 = int(lista[1]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[7]) ^ int(lista[8]) ^ int(lista[9]) ^ int(
        lista[10])  # Correcto
    p8 = int(lista[4]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[7]) ^ int(lista[8]) ^ int(lista[9]) ^ int(
        lista[10])  # Correcto

    # Calculamos el codigo hamming
    codigo = str(p1) + str(p2) + lista[0] + str(p4) + lista[1] + lista[2] + lista[3] + str(p8) + lista[4] + lista[5] + \
             lista[6] + lista[7] + lista[8] + lista[9] + lista[10]


    for i in codigo:
        listaF.append(i)

    MH = [[" ", " ", lista[0], " ", lista[1], lista[2], lista[3], " ", lista[4], lista[5], lista[6], lista[7], lista[8],
           lista[9], lista[10]],
          [str(p1), " ", lista[0], " ", lista[1], " ", lista[3], " ", lista[4], " ", lista[6], " ", lista[8], " ", lista[10]],
          [" ", str(p2), lista[0], " ", " ", lista[2], lista[3], " ", " ", lista[5], lista[6], " ", " ", lista[9], lista[10]],
          [" ", " ", " ", str(p4), lista[1], lista[2], lista[3], " ", " ", " ", " ", lista[7], lista[8], lista[9], lista[10]],
          [" ", " ", " ", " ", " ", " ", " ", str(p8), lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]],
          [listaF[0], listaF[1], listaF[2], listaF[3], listaF[4], listaF[5], listaF[6], listaF[7], listaF[8], listaF[9], listaF[10], listaF[11], listaF[12], listaF[13], listaF[14]]]


    # Retornamos el codigo hamming
    return MH

def decodificar(mensaje):
    lista = list(mensaje)

    pruebaParidad1 = int(lista[2]) ^ int(lista[4]) ^ int(lista[6]) ^ int(lista[8]) ^ int(lista[10]) ^ int(lista[12]) ^ int(
        lista[14])  # Correcto
    pruebaParidad2 = int(lista[2]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[9]) ^ int(lista[10]) ^ int(lista[13]) ^ int(
        lista[14])  # Correcto
    pruebaParidad3 = int(lista[4]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[11]) ^ int(lista[12]) ^ int(lista[13]) ^ int(
        lista[14])  # Correcto
    pruebaParidad4 = int(lista[8]) ^ int(lista[9]) ^ int(lista[10]) ^ int(lista[11]) ^ int(lista[12]) ^ int(lista[13]) ^ int(
        lista[14])  # Correcto

    bitParidad1 = int(pruebaParidad1 != int(lista[0]))
    bitParidad2 = int(pruebaParidad2 != int(lista[1]))
    bitParidad3 = int(pruebaParidad3 != int(lista[3]))
    bitParidad4 = int(pruebaParidad4 != int(lista[7]))

    pruebaStr1 = "Error" if bitParidad1 == 1 else "Correcto"
    pruebaStr2 = "Error" if bitParidad2 == 1 else "Correcto"
    pruebaStr3 = "Error" if bitParidad3 == 1 else "Correcto"
    pruebaStr4 = "Error" if bitParidad4 == 1 else "Correcto"

    MH = [lista,
          [lista[0], " ", lista[2], " ", lista[4], " ", lista[6], " ", lista[8], " ", lista[10], " ", lista[12],  " ", lista[14], pruebaStr1 , str(bitParidad1)],
          [" ", lista[1], lista[2], " ", " ", lista[5], lista[6], " ", " ", lista[9], lista[10], " ", " ", lista[13], lista[14], pruebaStr2 , str(bitParidad2)],
          [" ", " ", " ", lista[3], lista[4], lista[5], lista[6], " ", " ", " ", " ", lista[11], lista[12], lista[13], lista[14], pruebaStr3 , str(bitParidad3)],
          [" ", " ", " ", " ", " ", " ", " ", lista[7], lista[8], lista[9], lista[10], lista[11], lista[12], lista[13], lista[14], pruebaStr4 , str(bitParidad4)]
          ]

    return MH


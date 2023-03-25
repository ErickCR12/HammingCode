#Calcule el codigo hamming (15,11) para cualquier mensaje de 11 bits
#Autor: Jose Luis Macias Urbina
#Fecha: 10/10/2016
#Version: 1.0
#Plataforma: Python v2.7
#Descripcion: El codigo hamming es un codigo de paridad que permite detectar y corregir errores en un mensaje de 11 bits
#Ejemplo: 10101010101

#Importamos la libreria sys para poder usar la funcion exit
import sys

#Definimos la funcion para calcular el codigo hamming
def hamming(mensaje):
    #Creamos una lista para guardar el mensaje
    lista = []


    #Recorremos el mensaje y lo guardamos en la lista
    for i in mensaje:
        lista.append(i)

    #Calculamos los bits de paridad
    p1 = int(lista[0]) ^ int(lista[1]) ^ int(lista[3]) ^ int(lista[4]) ^ int(lista[6]) ^ int(lista[8]) ^ int(lista[10])
    p2 = int(lista[0]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[9]) ^ int(lista[10])
    p4 = int(lista[1]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[7])
    p8 = int(lista[4]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[7])

    #Imprimimos el mensaje original
    print ("Mensaje original: " + mensaje)

    #Imprimimos el mensaje con los bits de paridad
    print ("Mensaje con bits de paridad: " + str(p1) + str(p2) + lista[0] + str(p4) + lista[1] + lista[2] + lista[3] + str(p8) + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10])

    #Calculamos el codigo hamming
    codigo = str(p1) + str(p2) + lista[0] + str(p4) + lista[1] + lista[2] + lista[3] + str(p8) + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10]

    #Imprimimos el codigo hamming
    print("Codigo hamming: " + codigo)

    #Retornamos el codigo hamming
    return codigo

#Definimos la funcion para calcular el mensaje original
def mensaje(codigo):
    #Creamos una lista para guardar el codigo
    lista = []

    #Recorremos el codigo y lo guardamos en la lista
    for i in codigo:
        lista.append(i)

    #Calculamos los bits de paridad
    p1 = int(lista[0]) ^ int(lista[1]) ^ int(lista[3]) ^ int(lista[4]) ^ int(lista[6]) ^ int(lista[8]) ^ int(lista[10])
    p2 = int(lista[0]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[9]) ^ int(lista[10])
    p4 = int(lista[1]) ^ int(lista[2]) ^ int(lista[3]) ^ int(lista[7])
    p8 = int(lista[4]) ^ int(lista[5]) ^ int(lista[6]) ^ int(lista[7])

    #Calculamos el bit de error
    error = p1 + p2 + p4 + p8

    #Imprimimos el codigo hamming
    print("Codigo hamming: " + codigo)

    #Imprimimos el bit de error
    print("Bit de error: " + str(error))

    #Si el bit de error es 0, no hay errores
    if error == 0:
        print("No hay errores")
    #Si el bit de error es mayor a 0, hay errores
    else:
        print("Hay errores")

        #Si el bit de error es mayor a 15, hay mas de un error
        if error > 15:
            print("Hay mas de un error")
        #Si el bit de error es menor a 15, hay un error
        else:
            print("Hay un error")

            #Imprimimos el mensaje original
            print("Mensaje original: " + lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10])

    #Retornamos el mensaje original
    return
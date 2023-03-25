import matplotlib.pyplot as plt


def nrzi_signal(bin_string):

    # Convertir la cadena de caracteres a una lista de dígitos binarios
    binary_digits = [int(d) for d in bin_string]

    # Inicializar la señal NRZI
    signal = [0]

    # Establecer el nivel de la señal de acuerdo al primer dígito binario
    if binary_digits[0] == 0:
        level = 0
    else:
        level = 1

    # Codificar la señal NRZI
    for bit in binary_digits:
        if bit == 0:
            # Mantener el nivel actual
            signal.append(level)
        else:
            # Invertir el nivel actual
            level = 1 - level
            signal.append(level)

    # Graficar la señal NRZI
    plt.plot(signal, drawstyle='steps-post')
    plt.xticks(range(len(signal)))
    plt.yticks([0,1])
    plt.xlabel('Tiempo')
    plt.ylabel('Número binario')
    plt.title('Señal digital NRZI')
    plt.show()

nrzi_signal('110100101')


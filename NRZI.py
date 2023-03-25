import matplotlib.pyplot as plt

def nrzi_signal(binary_string):
    binary_list = list(binary_string)
    x_values = []
    y_values = []
    current_level = 0
    
    for bit in binary_list:
        if bit == '1':
            current_level = 1 - current_level
        x_values.append(len(x_values))
        y_values.append(current_level)

    plt.step(x_values, y_values, where='post')
    plt.ylim([-0.5, 1.5])
    plt.xlabel('Bit')
    plt.ylabel('NRZI Signal')
    plt.xticks(x_values, binary_list)
    plt.title('NRZI Signal for ' + binary_string)
    plt.show()

nrzi_signal('011000110100')

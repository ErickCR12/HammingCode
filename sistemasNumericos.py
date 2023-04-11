
############################################################ 

def tres_digitos(cadena):
    if len(cadena) == 3:
        return True
    else:
        return False

############################################################     

def hex_to_decimal(num):
    
    if tres_digitos(num):
        try:

            decimal_num = int(num, 16)
            if decimal_num > 2047:
                raise ValueError
            return decimal_num

        except ValueError:
            raise ValueError("El número no es un hexadecimal válido o está fuera del rango.")
        
    else:
        raise ValueError("El numero debe contener tres dígitos.")

############################################################ 

def hex_a_octal(num):
    
    if tres_digitos(num):
        
        try:
            numero_dec = int(num, 16)
            numero_oct = oct(numero_dec)
            return numero_oct [2:]

        except ValueError:
            raise ValueError("El numero no es Hexadecimal")

    else:

        raise ValueError("El numero debe contener tres dígitos.")
       
############################################################ 

def hexadecimal_a_binario(num):

    if tres_digitos(num):

        try:
            numero_dec = int(num, 16)
            numero_bin = bin(numero_dec)
            return bin_11digitos(numero_bin[2:])

        except ValueError as e:
            raise ValueError("El numero no es Hexadecimal")
    else:
        raise ValueError("El numero debe contener tres dígitos.")


def bin_11digitos(num):
    ceros = 11 - len(num)
    return "0"*ceros + num
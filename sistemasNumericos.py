
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
            return decimal_num
        
        except ValueError:
            return "El numero no es Hexadecimal" 
        
    else:
        return "El numero debe contener tres dígitos."

############################################################ 

def hex_a_octal(num):
    
    if tres_digitos(num):
        
        try:
            numero_dec = int(num, 16)
            numero_oct = oct(numero_dec)
            return numero_oct [2:]

        except ValueError:
            return "El numero no es Hexadecimal"

    else:

        return "El numero debe contener tres dígitos."
       
############################################################ 

def hexadecimal_a_binario(num):

    if tres_digitos(num):

        try:       
            numero_dec = int(num, 16)
            numero_bin = bin(numero_dec)
            return numero_bin[2:]
        
        except ValueError:
            return "El numero no es Hexadecimal"

    else:

        return "El numero debe contener tres dígitos."    



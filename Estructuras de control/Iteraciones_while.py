line = input("Ingresa 8 bits (ceros y unos): ")
#Inicia el bucle hasta encontrar un espacio en blanco
while line != "":
    #Condición que asegura que tiene excatamente 8 bits
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        #Si es diferente de ocho intenta de nuevo
        print("No son 8 bits, intenta de nuevo")
    else:
        #Cuenta los unos
        ones = line.count("1")
        #Este conteo regresa el número de veces que aparce el uno en la cadena de ocho bits
        #despliega el bit de paridad
        if ones %2 == 0:
            print("El bit de paridad debe ser 0.")
        else:
            print("El bit de paridad debe ser 1.")
    #Lee la siguiente cadena de bits
    line = input("Ingresa 8 bits: ")
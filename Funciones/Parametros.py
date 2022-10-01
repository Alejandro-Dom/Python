#La función se llama 'dibujo', dibuja un rectángulo y las variables (parámetros)
#que solicita el ancho y el alto de la figura

def dibujo(ancho, largo):
    #Se utiliza una estructura de control
    if ancho < 10 or largo < 10:
        print("Error: la figura es muy pequeña o muy grande.")
        quit()
    #Dibuja la parte superior de la figura
    print("*" * ancho)
    #Dibuja los lados, en este caso se utiliza un bucle para el valor del alto de la figura
    for i in range (largo - 2):
        print("*" + " " * (ancho - 2) + "*")
    #Dibuja la parte inferior
    print("*" * ancho)

dibujo(20,20)
#Funciuón de una sucesión geométrica

def sumGeometrica(a, r, n):
    #Si el radio tiene un valor de uno
    if r == 1:
        return a * n
    #Calcula la suma geométrica cuando el radio es diferente de 1
    s = a * (1-r**n) / (1-r)
    #Regresa el valor de s
    return s

print(sumGeometrica(2,3,4))

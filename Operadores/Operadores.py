x = int(input("Ingresa un número entero: "))

#Se determina si el digito se encunetra en los primeros cinco números primos
if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
    print("El número pertenece a los primeros cinco números primos")
else:
    print("El número no pertenece a los primeros cinco números primos")
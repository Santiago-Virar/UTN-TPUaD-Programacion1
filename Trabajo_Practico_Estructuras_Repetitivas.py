#ACTIVIDAD 1
"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for num in range (0, 101):
    print(num)   


#ACTIVIDAD 2
"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene."""

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero))) 

print(f"El número tiene {cantidad_digitos} dígitos.")


#ACTIVIDAD 3
"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores."""

valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))
suma = 0

for num in range(valor1 + 1, valor2):
    suma += num
print("La suma de los números entre", valor1, "y", valor2, "es:", suma)


#ACTIVIDAD 4
"""Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0."""

suma_acumulada = 0

while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    suma_acumulada += numero
print("La suma acumulada es:", suma_acumulada)


#ACTIVIDAD 5
"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random
numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")


#ACTIVIDAD 6
"""Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente."""

for num in range(100, -1, -1):
    if num % 2 == 0:
        print(num)


#ACTIVIDAD 7
"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario."""

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, numero + 1):
    suma += i
print(f"La suma de los números entre 0 y {numero} es: {suma}")


#ACTIVIDAD 8
"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(20):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    else:
        positivos += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")


#ACTIVIDAD 9
"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""

suma = 0
cantidad_numeros = 20
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero
media = suma / cantidad_numeros
print(f"La media de los {cantidad_numeros} números ingresados es: {media}") 


#ACTIVIDAD 10
"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = input("Ingrese un número entero: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")
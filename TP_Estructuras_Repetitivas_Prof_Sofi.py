#ACTIVIDAD 1
"""Escribir un programa que pida al usuario una palabra y la muestre por 
pantalla 10 veces."""

palabra = input("Ingrese una palabra: ")
for i in range(10):
    print(palabra)



#ACTIVIDAD 2
"""Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

edad = int(input("Edad: "))

for i in range(1, edad + 1):
    print("Has cumplido", i, "años")



#ACTIVIDAD 3
"""Escribir un programa que pida al usuario un número entero y muestre 
por pantalla un triángulo rectángulo como el de más abajo, de altura el 
número introducido."""

numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



#ACTIVIDAD 4
"""Escribir un programa que muestre por pantalla la tabla de multiplicar 
del 1 al 10."""

for i in range (1, 11):
    for j in range (1, 11):
        print(f"{i} x {j} = {i*j}")
    print ()



#ACTIVIDAD 5

"""Escribir un programa que almacene la cadena de 
caracteres contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta"""

contraseña = "Santiago2024"
while True:
    ingreso = input("Ingrese la contraseña: ")
    ingreso == contraseña
    if ingreso == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, intente nuevamente")
        continue



#ACTIVIDAD 6
"""Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará. """

salir = "salir"

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == salir:
        print("Uso la palabra de salida")
        break
    else:
        print(f"{palabra}, {palabra}")
        continue



#AVTIVIDAD 7
"""Escribe un bucle for que imprima los números pares del 2 al 20 
(inclusive)."""

for i in range(2,21,2):
    print (i)



#ACTIVIDAD 8
"""Imprime números del 1 al 100, pero:
Para múltiplos de 3 → "Fizz". 
Para múltiplos de 5 → "Buzz". 
Para múltiplos de ambos → "FizzBuzz"."""

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} - Fizz")
    elif i % 5 == 0:
        print(f"{i} - Buzz")
    else:
        print(i)



#ACTIVIDAD 9
"""Desarrollar un programa que solicite la carga de 10 números e imprima 
la suma de los últimos 5 valores ingresados. """

suma = 0
for i in range(10): 
    numero = int(input("Ingrese un número: "))
    if i >= 5:
        suma += numero
print("La suma de los últimos 5 números es:", suma) 



#ACTIVIDAD 10
"""Realizar un programa que lea los lados de n triángulos. 
Informar después de cada triángulo si es equilátero (tres lados iguales), 
isósceles (dos lados iguales) o escaleno (ningún lado igual). Informar 
después del total de triángulos de cada tipo """

n=int(input("Ingrese la cantidad de triangulos:"))
equilatero=0
isosceles=0
escaleno=0

for i in range(n):
    print(f"Ingrese los valores de los lados del {i+1} triangulo")
    a=float(input("Ingrese el valor del primer lado :"))
    b=float(input("Ingrese el valor del segundo lado :"))
    c=float(input("Ingrese el valor del tercer lado :"))

    if a==b and b==c:
        print("El triangulo es equilatero")
        equilatero=+1

    elif a==b or a==c or b==c:
        print("El triangulo es isosceles")
        isosceles=+1
    else:
        print("El triangulo es escaleno")
        escaleno=+1 

print(f"La cantidad de triangulos equilateros es: {equilatero}")
print(f"La cantidad de triangulos isoceles es: {isosceles}")
print(f"La cantidad de triangulos escalenos es: {escaleno}")  

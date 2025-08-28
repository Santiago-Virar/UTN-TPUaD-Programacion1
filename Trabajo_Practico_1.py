#Actividad 1

print ("Hola Mundo") 

#Actividad 2

nombre = input ("¿Cual es tu nombre?:")
print (f"Hola {nombre}")

#Actividad 3

"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla"""

nombre = input ("Escribe tu nombre:")
apellido = input("Escribe tu apellido:")
edad = input ("Escribe tu edad:")
domicilio = input ("Escribe tu domicilio:")

print (f"Hola soy {nombre} {apellido}, tengo {edad} años de edad y vivo en {domicilio}")

#Actividad 4

"""Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro."""

radio = float (input("Ingrese el radio de su circulo: "))
area = 3.1416 * radio **2
perimetro = 2 * 3.1416 * radio
print (f"El area del circulo es {area}")
print (f"El perimetro del circulo es: {perimetro}")

#Actividad 5

"""Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""

segundos = int(input("Ingrese la cantidad de segundos que desea convertir a horas: "))
horas = segundos / 3600
print (f"{segundos} equivale a {horas} hs" )

#Actividad 6

"""Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""

numero = int(input("Ingrese el número que desea multiplicar: "))
print (f"{numero} x 1 = {numero *1}")
print (f"{numero} x 2 = {numero *2}")
print (f"{numero} x 3 = {numero *3}")
print (f"{numero} x 4 = {numero *4}")
print (f"{numero} x 5 = {numero *5}")
print (f"{numero} x 6 = {numero *6}")
print (f"{numero} x 7 = {numero *7}")
print (f"{numero} x 8 = {numero *8}")
print (f"{numero} x 9 = {numero *9}")
print (f"{numero} x 10 = {numero *10}")

#Actividad 7

"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

numero1 = int(input("Ingrese el primer número entero distinto de cero: "))
numero2 = int(input("Ingrese el segundo número entero distinto de cero: "))

print (f"Suma = {numero1 + numero2}")
print (f"División = {numero1 / numero2}")
print (f"Multiplicacion = {numero1 * numero2}")
print (f"Resta = {numero1 - numero2}")

#Actividad 8

"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:"""

peso = float(input("Ingrese su peso:"))
altura = float(input("Ingrese su altura:"))
indice_masa_corporal = peso / altura**2

print (f"Tu indice de masa corporal es igual a: {indice_masa_corporal}")

#Actividad 9

"""Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:"""

temperatura_celcius = int(input("Ingrese la temperatura que desea saber en Celsius: "))
fahrenheit = 9/5 * temperatura_celcius + 32

print (f"La temperatura en Fahrenheit es de {fahrenheit} grados.")

#Actividad 10

"""Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

suma= numero1 + numero2 + numero3
suma = round(suma / 3, 2)

print (f"El promedio de los números ingresados es {suma}")
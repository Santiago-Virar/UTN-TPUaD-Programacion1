#ACTIVIDAD 1

"""Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

edad = int(input ("Escribe tu edad: "))
if edad >= 18:
    print ("Eres mayor de edad")
print ("Puedes solicitar tu permiso de conducir")

#ACTIVIDAD 2

""" Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado” """

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print ("¡Felicitaciones estas aprobado! ✅")
else:
    print ("Lo siento has desaprobado ☹️")

#ACTIVIDAD 3

"""Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

numero = int(input("Ingrese un numero entero que sea par:"))
if numero % 2==0:
    print (f"Has ingrasado un numero par: {numero}")
else:
    print("Por favor ingrese un numero par")

#ACTIVIDAD 4

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""

edad = int(input("Ingrese su edad:"))
if edad < 12:
    print ("Perteneces a la categoria Niño/a:👦")
elif edad >= 12 and edad <18:
    print ("Perteneces a la categoria Adolescente:👦")
elif edad >= 18 and edad <30:
    print("Perteneces a la categoria Adulto/a joven: 👨👨‍🦰")
else: edad >=30
print ("Perteneces a la categoria Adulto/a mayor: 👨‍🦲👨‍🦱")

print ("Gracias por brindarnos su edad ✅")

#ACTIVIDAD 5

"""Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string"""

contrasena = input("Ingrese una contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ACTIVIDAD 6

"""Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

import random
from statistics import mean, median, mode


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

valor_media = mean(numeros_aleatorios)
valor_mediana = median(numeros_aleatorios)
valor_moda = mode(numeros_aleatorios)

if valor_media > valor_mediana > valor_moda:
    print ("Hay sesgo positivo ✅")
elif valor_media < valor_mediana < valor_moda:
    print ("Hay sesgo negativo ❌")
elif valor_media == valor_mediana == valor_moda:
    print ("Sin sesgo 👎")
else:
    print ("Sesgo no definido ☹️")

print (numeros_aleatorios)
print (f"Media: {valor_media}")
print (f"Mediana: {valor_mediana}")
print (f"Moda {valor_moda}")

#ACTIVIDAD 7

"""Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""

frase = input ("Escriba una frase o palabra que desee:")
ultima_letra = frase[-1]

if ultima_letra in "aeiouAEIOU":
    print (frase + "!")
else:
    print (frase)

#ACTIVIDAD 8

"""Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."""

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida ❌ Debe ser 1, 2 o 3.")

#ACTIVIDAD 9

"""Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte (puede causar daños significativos).
● Mayor o igual que 7: "Extremo (puede causar graves daños a gran escala)."""

magnitud_terremoto = float(input("Ingrese la magnitud del Terremoto:"))

if magnitud_terremoto < 3:
    print("Muy leve - (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto <4 :
    print("Leve - (ligeramente perceptible) " )
elif magnitud_terremoto >= 4 and magnitud_terremoto <5 :
    print("Moderado - (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto <6:
    print ("Fuerte - (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto <7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo - (puede causar graves daños a gran escala)")
else:
    print("Error, ingrese un valor válido")

#ACTIVIDAD 10

"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

emisferio = input("Ingrese en cuál hemisferio se encuentra (N/S): ").upper()
mes = input("Ingrese el mes actual: ").lower()
dia = int(input("Ingrese el día del mes: "))

if emisferio == "N":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia < 21):
        print("Invierno")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia < 21):
        print("Primavera")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia < 23):
        print("Verano")
    elif (mes == "septiembre" and dia >= 23) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia < 21):
        print("Otoño")
    else:
        print("Error, ingrese un mes válido")
elif emisferio == "S":
    if (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia < 23):
        print("Invierno")
    elif (mes == "septiembre" and dia >= 23) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia < 21):
        print("Primavera")
    elif (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia < 21):
        print("Verano")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia < 21):
        print("Otoño")
    else:
        print("Error, ingrese un mes válido")
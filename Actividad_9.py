"""Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:"""

temperatura_celcius = int(input("Ingrese la temperatura que desea saber en Celsius: "))
fahrenheit = 9/5 * temperatura_celcius + 32

print (f"La temperatura en Fahrenheit es de {fahrenheit} grados.")


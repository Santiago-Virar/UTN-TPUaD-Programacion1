"""Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

suma= numero1 + numero2 + numero3
suma = round(suma / 3, 2)

print (f"El promedio de los números ingresados es {suma}")



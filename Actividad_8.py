"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:"""

peso = float(input("Ingrese su peso:"))
altura = float(input("Ingrese su altura:"))
indice_masa_corporal = peso / altura**2

print (f"Tu indice de masa corporal es igual a: {indice_masa_corporal}")


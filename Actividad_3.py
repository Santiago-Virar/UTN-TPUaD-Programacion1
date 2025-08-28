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

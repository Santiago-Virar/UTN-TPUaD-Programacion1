#ACTIVIDAD 1

"""1. Lee el siguiente código y explica qué hace:"""

contrasena_correcta = "programacion1" 
contrasena_usuario = input("Introduce la contraseña: ") 
if contrasena_usuario == contrasena_correcta: 
    print("Contraseña correcta. Bienvenido.") 
else: 
    print("Contraseña incorrecta. Intenta de nuevo.") 

"""El código solicita al usuario que introduzca una contraseña y la compara con una contraseña 
predefinida ("programacion1").
Si la contraseña es correcta, se muestra un mensaje de bienvenida; de lo contrario
se le pide al usuario que lo intente de nuevo.
1- Si lo ingresa con mayusculas lo toma como incorrecto
2- Lo que haria para mejorarlo es usar el metodo lower() para que no importe si lo ingresa 
en mayusculas o minusculas. Tambien se podria agregar un contador de intentos para limitar 
la cantidad de veces que el usuario puede intentar ingresar la contraseña."""

#ACTIVIDAD 2

"""1. Solicita una letra al usuario.
2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra 
ingresada es una vocal".
3. En otro caso, imprime: "La letra ingresada no es una vocal"."""

letra = input("Ingresa una letra: ")

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada no es una vocal.")


#ACTIVIDAD 3

""""1. Pide un número al usuario.
2. Si es positivo, imprime: "El número es positivo".
3. Si es negativo, imprime: "El número es negativo".
4. Si es cero, imprime: "El número es cero"""

numero = int(input("Ingrese un numero: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

#ACTIVIDAD 4

"""1. Solicita dos números al usuario.
2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
3. Si el primero es menor, imprime: "El primer número ingresado es menor".
4. Si son iguales, imprime: "Los números ingresados son iguales"."""

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

if num_1 > num_2:
    print ("El primer número es mayor que el segundo ✅")
elif num_1 < num_2:
    print ("El primer número es menor que el segundo ☹️")
else:
    num_1 == num_2 
    print("Los números ingresados son iguales 🟰")


#ACTIVIDAD 5

"""1. Pide la temperatura actual en °C.
2. Si es ≤ 10°C, imprime: "Hace frío".
3. Si está entre 10°C y 25°C, imprime: "Está templado".
4. Si es > 25°C, imprime: "Hace calor". """

temperatura = float(input("Ingrese la temperatura actual en °C: "))
if temperatura <= 10:
    print("Hace frío.")
elif 10 < temperatura <= 25:
    print("Está templado.")
else:
    temperatura > 25
    print("Hace calor.")

#ACTIVIDAD 6

"""1. Pide un año al usuario.
2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se 
ingresó un año bisiesto".
3. En otro caso, imprime: "Se ingresó un año no bisiesto"""

año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Se ingresó un año bisiesto.")
else:
    print("Se ingresó un año no bisiesto.")

#ACTIVIDAD 7

"""1. Pide una frase o palabra al usuario.
2. Si no termina en punto, añádelo al final.
3. Imprime el resultado."""

frase = input("Ingrese una frase o palabra: ")
if not frase.endswith("."):
    frase += "."
print(frase)

#ACTIVIDAD 8

"""1. Pide al usuario que cree una contraseña.
2. Verifica que cumpla:
- 8+ caracteres y ≤20 caracteres.
- Al menos 1 mayúscula (usa .isupper()).
- Al menos 1 número (usa .isdigit()).
3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
4. Si no, imprime: "La contraseña no es segura."""

contraseña = input("Ingrese una contraseña: ")

if (8 <= len(contraseña) <= 20 and
    any(c.isupper() for c in contraseña) and
    any(c.isdigit() for c in contraseña)):
    print("¡Felicitaciones! Creaste tu contraseña segura. ✅")
else:
    print("La contraseña no es segura. ❌")

#ACTIVIDAD 8

"""1. Pide al usuario que cree una contraseña.
2. Verifica que cumpla:
- 8+ caracteres y ≤20 caracteres.
- Al menos 1 mayúscula (usa .isupper()).
- Al menos 1 número (usa .isdigit()).
3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
4. Si no, imprime: "La contraseña no es segura."""

contraseña = input("Ingrese una contraseña: ")

if (8 <= len(contraseña) <= 20 and 
    any(c.isupper() for c in contraseña) and 
    any(c.isdigit() for c in contraseña)):
    print("¡Felicitaciones! Creaste tu contraseña segura. ✅")
else:
    print("La contraseña no es segura. ❌")


#ACTIVIDAD 9

"""1. Basado en el Ejercicio 8, mejora los mensajes de error:
o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al 
menos 8 caracteres.".
o Si tiene >20 caracteres: "...no más de 20 caracteres.".
o Si falta mayúscula: "...al menos una mayúscula.".
o Si falta número: "...al menos un número."."""

contraseña = input("Ingrese una contraseña: ")

if 8 < len(contraseña):
    print ("La contraseña no es segura. Debe tener al menos 8 caracteres.")
elif 20 > len(contraseña):
    print ("...no más de 20 caracteres.")
elif not any(c.isupper() for c in contraseña):
    print ("...al menos una mayúscula.")    
elif not any(c.isdigit() for c in contraseña):
    print ("...al menos un número.")
else:
    print("¡Felicitaciones! Creaste tu contraseña segura. ✅")


#ACTIVIDAD 10
"""1. Simula un juego de "Piedra, Papel o Tijera" entre dos jugadores."""


jugador1 = input("Jugador 1, ingresa tu jugada (Piedra, Papel o Tijera): ").lower()
jugador2 = input("Jugador 2, ingresa tu jugada (Piedra, Papel o Tijera): ").lower()

if jugador1 == jugador2:
    print("EMPATE")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
    (jugador1 == "papel" and jugador2 == "piedra") or \
    (jugador1 == "tijera" and jugador2 == "papel"):
    print("GANA JUGADOR 1")
else:
    print("GANA JUGADOR 2")

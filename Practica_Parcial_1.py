#ACTIVIDAD 1 

pelicula = []
butacas = []

opcion = ""

while opcion != 6:
    print("\n--- MENÚ DEL CINE ---")
    print("1. Agregar película")
    print("2. Consultar butacas disponibles")
    print("3. Ver cartelera completa")
    print("4. Listar películas sin butacas")
    print("5. Reservar / Cancelar butacas")
    print("6. Salir")
    
    opcion = int(input("Elegí una opción: "))
    # OPCION 1 - Agregar película
    if opcion == 1:
        nombre = input ("✅ Ingrese el nombre de la pelicula que desea agregar: ").strip()
        if nombre == "":
            print ("❌ Escriba un nombre por favor.")
        elif nombre in pelicula:
            print ("❌ Esa pelicula ya esta cargada.")
        else:
            cantidad = int(input("✅ Ingrese la cantidad de butacas:  "))
            if cantidad < 0:
                print ("❌ La cantidad de butacas no puede ser negativa")
            else:
                pelicula.append(nombre)
                butacas.append(cantidad)
                print (f"✅ Pelicula {nombre} agregada con {cantidad} butacas disponibles.")
    # OPCION 2 - Consultar butacas disponibles   
    elif opcion == 2:
        nombre = input("✅ Ingrese el nombre de la película que desea saber la cantidad de butacas: ").strip()
        if nombre in pelicula:
            posicion = pelicula.index(nombre)
            print(f"✅ La película '{nombre}' tiene {butacas[posicion]} butacas disponibles.")
        else:
            print ("❌ La pelicula no se encuentra cargada:")
    # OPCION 3 - Ver cartelera completa
    elif opcion == 3:
        print("\n--- CARTELERA COMPLETA ---")
        if len(pelicula) == 0:
            print ("❌ Todavia no hay ninguna pelicula agregada.")
        else:
            for i in range (len(pelicula)):
                print (f"🎥 {pelicula[i]} ➡️  {butacas[i]} butacas disponibles")
    # OPCION 4 - Listar películas sin butacas
    elif opcion == 3:
        print("\n--- PELÍCULAS SIN BUTACAS ---")
        if len(pelicula) == 0:
            print("❌ No hay películas cargadas en la cartelera.")
        else:
            bandera = False  # Para saber si encontramos alguna sin butacas
            for i in range(len(pelicula)):
                if butacas[i] == 0:
                    print(f"🎥 {pelicula[i]} ➡️  SIN BUTACAS")
                    bandera = True
            if not bandera:
                print("✅ Todas las películas tienen butacas disponibles.")
    #OPCION 5 - Reservar / Cancelar butacas
    elif opcion == 5:
        nombre = input("Ingrese el nombre de la película: ").strip()

        if nombre in pelicula:
            posicion = pelicula.index(nombre)
        
        print("1. Reservar 1 butaca")
        print("2. Cancelar 1 butaca")
        accion = int(input("Elija una opción: "))
        if accion == 1:
            if butacas[posicion] > 0:
                butacas[posicion] -= 1
                print(f"✅ Butaca reservada. Quedan {butacas[posicion]} butacas.")
            else:
                print("❌ No hay butacas disponibles para reservar.")
        elif accion == 2:
            butacas[posicion] += 1
            print(f"✅ Butaca cancelada. Quedan {butacas[posicion]} butacas.")
        else:
            print("❌ Opción inválida.")
    else:
        print("❌ La película no existe en la cartelera.")
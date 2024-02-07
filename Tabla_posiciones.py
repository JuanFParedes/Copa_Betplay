equipos = {}


def imprimir_menu():
    menu = """
            ++++++++++++++++++++++++++++++++++++++++++++++
            +++++++++ LIGA BETPLAY COLOMBIA 2024 +++++++++
            ++++++++++++++++++++++++++++++++++++++++++++++
            
    1. Registrar Equipo
    2. Registrar fecha de juego
    3. Reportes
    4. Salir
    """

    print(menu)


def menu_reportes():
    menu = """
            +++++++++++++++++++++++++++++++++++++++
            +         REPORTES DEL TORNEO         +
            +++++++++++++++++++++++++++++++++++++++
            
    A. Nombre del equipo que más goles anotó
    B. Nombre del equipo que más puntos tiene
    C. Nombre del equipo que más partidos ganó
    D. Total de goles anotados por todos los equipos
    E. Promedio de goles anotados en el torneo
    F. Regresar al menú principal
    """

    print(menu)


def mas_goles():
    equipo_mas_goles = ""
    maximo_goles = 0

    for equipo, datos_equipo in equipos.items():
        goles_equipo = datos_equipo["GF"]
        if goles_equipo > maximo_goles:
            maximo_goles = goles_equipo
            equipo_mas_goles = equipo

    print("El equipo con más goles es:", equipo_mas_goles, "con", maximo_goles, "goles.")


def mas_puntos():
    equipo_mas_puntos = ""
    maximo_puntos = 0

    for equipo, datos_equipo in equipos.items():
        puntos_equipo = datos_equipo["TP"]
        if puntos_equipo > maximo_puntos:
            maximo_puntos = puntos_equipo
            equipo_mas_puntos = equipo

    print("El equipo con más puntos es:", equipo_mas_puntos, "con", maximo_puntos, "puntos.")


def mas_partidos():
    equipo_mas_partidos = ""
    maximo_partidos = 0

    for equipo, datos_equipo in equipos.items():
        partidos_equipo = datos_equipo["TP"]
        if partidos_equipo > maximo_partidos:
            maximo_partidos = partidos_equipo
            equipo_mas_partidos = equipo

    print("El equipo con más partidos ganados es:", equipo_mas_partidos, "con", maximo_partidos, "partidos ganados.")


def total_goles():
    maximo_goles = 0

    for equipo, datos_equipo in equipos.items():
        goles_equipo = datos_equipo["GF"]
        maximo_goles += goles_equipo

    print("El total de goles es:", maximo_goles, "goles.")


def promedio_goles():
    tot_goles = 0
    total_partidos = (len(equipos) * (len(equipos) - 1)) // 2

    for equipo, datos_equipo in equipos.items():
        goles_equipo = datos_equipo["GF"]
        tot_goles += goles_equipo

    prom_goles = tot_goles / total_partidos

    print("El promedio de goles es de:", prom_goles, "goles.")


def seleccion_reportes():
    menu_reportes()
    opcion = input("Por favor, seleccione una opción: ").lower()

    if opcion == "a":
        mas_goles()
        seleccion_reportes()
    elif opcion == "b":
        mas_puntos()
        seleccion_reportes()
    elif opcion == "c":
        mas_partidos()
        seleccion_reportes()
    elif opcion == "d":
        total_goles()
        seleccion_reportes()
    elif opcion == "e":
        promedio_goles()
        seleccion_reportes()
    elif opcion == "f":
        main()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        seleccion_reportes()


def registrar_equipos(nombre_equipo):
    equipos[nombre_equipo] = {
        "PJ": 0,
        "PG": 0,
        "PP": 0,
        "PE": 0,
        "GF": 0,
        "GC": 0,
        "TP": 0,
    }

    print("Equipo registrado exitosamente")


def registrar_fechas():
    bandera = 0
    equipo_local = 0
    equipo_visitante = 0

    while bandera == 0:
        for i, clave in enumerate(equipos.keys(), start=1):
            print(f"{i}. {clave}")

        equipo_local = input("Por favor ingrese el número del equipo local: ")

        if equipo_local.isdigit() and 1 <= int(equipo_local) <= len(equipos):
            indice_seleccionado = int(equipo_local) - 1
            claves = list(equipos.keys())
            clave_seleccionada = claves[indice_seleccionado]
            print("Ha seleccionado como local al equipo: ", clave_seleccionada)
        else:
            print("Opción inválida. El equipo no está en la lista.")
            continue

        equipo_visitante = input("Por favor ingrese el número del equipo visitante: ")

        if equipo_visitante.isdigit() and 1 <= int(equipo_visitante) <= len(equipos):
            if equipo_visitante == equipo_local:
                print("El equipo local y visitante no pueden ser el mismo.")
            else:
                indice_seleccionado = int(equipo_visitante) - 1
                claves = list(equipos.keys())
                clave_seleccionada = claves[indice_seleccionado]
                print("Ha seleccionado como visitante al equipo: ", clave_seleccionada)
                bandera = 1
        else:
            print("Opción inválida. El equipo no está en la lista.")

    claves = list(equipos.keys())
    nombre_equipo_local = claves[int(equipo_local) - 1]
    nombre_equipo_visitante = claves[int(equipo_visitante) - 1]

    goles_local = input(f"Ingrese la cantidad de goles del equipo {nombre_equipo_local}: ")
    goles_visitante = input(f"Ingrese la cantidad de goles del equipo {nombre_equipo_visitante}: ")

    equipos[nombre_equipo_local]["PJ"] += 1
    equipos[nombre_equipo_visitante]["PJ"] += 1
    equipos[nombre_equipo_local]["GF"] += int(goles_local)
    equipos[nombre_equipo_visitante]["GF"] += int(goles_visitante)
    equipos[nombre_equipo_local]["GC"] += int(goles_visitante)
    equipos[nombre_equipo_visitante]["GC"] += int(goles_local)

    if int(goles_visitante) > int(goles_local):
        equipos[nombre_equipo_visitante]["PG"] += 1
        equipos[nombre_equipo_local]["PP"] += 1
        equipos[nombre_equipo_visitante]["TP"] += 3
    elif int(goles_visitante) < int(goles_local):
        equipos[nombre_equipo_visitante]["PP"] += 1
        equipos[nombre_equipo_local]["PG"] += 1
        equipos[nombre_equipo_local]["TP"] += 3
    else:
        equipos[nombre_equipo_visitante]["PE"] += 1
        equipos[nombre_equipo_local]["PE"] += 1
        equipos[nombre_equipo_visitante]["TP"] += 1
        equipos[nombre_equipo_local]["TP"] += 1

    print("Se ha registrado con éxito la fecha del encuentro")


def main():
    imprimir_menu()
    opcion = input("Por favor, seleccione una opción: ")

    if opcion == "1":
        nombre_equipo = input("Por favor ingrese el nombre del equipo: ")
        registrar_equipos(nombre_equipo)
        main()
    elif opcion == "2":
        registrar_fechas()
        main()
    elif opcion == "3":
        seleccion_reportes()
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        main()


if __name__ == "__main__":
    main()
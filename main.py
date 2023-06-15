from ClaseAgenteUnivesitario import AgenteUniversitario
from ClaseDocente import Docente
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalDeApoyo
from InterfaceTesorero import ITesorero
from InterfaceDirector import IDirector
from ClaseTesorero import Tesorero
from ClaseDirector import Director
import json

# Función para cargar datos desde un archivo JSON
def cargar_datos(desde_archivo):
    try:
        with open(desde_archivo, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# Función para guardar datos en un archivo JSON
def guardar_datos(datos, hacia_archivo):
    with open(hacia_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)


# Programa principal
def main():
    datos = cargar_datos("personal.json")
    agentes = []

    for dato in datos:
        tipo_agente = dato.get("tipo_agente")

        if tipo_agente == "Docente":
            agente = Docente(
                dato["cuil"],
                dato["apellido"],
                dato["nombre"],
                dato["sueldo_basico"],
                dato["antiguedad"],
                dato["carrera"],
                dato["cargo"],
                dato["catedra"],
            )
        elif tipo_agente == "PersonalDeApoyo":
            agente = PersonalDeApoyo(
                dato["cuil"],
                dato["apellido"],
                dato["nombre"],
                dato["sueldo_basico"],
                dato["antiguedad"],
                dato["categoria"],
            )
        elif tipo_agente == "Investigador":
            agente = Investigador(
                dato["cuil"],
                dato["apellido"],
                dato["nombre"],
                dato["sueldo_basico"],
                dato["antiguedad"],
                dato["area_investigacion"],
                dato["tipo_investigacion"],
            )
        elif tipo_agente == "DocenteInvestigador":
            agente = DocenteInvestigador(
                dato["cuil"],
                dato["apellido"],
                dato["nombre"],
                dato["sueldo_basico"],
                dato["antiguedad"],
                dato["carrera"],
                dato["cargo"],
                dato["catedra"],
                dato["area_investigacion"],
                dato["tipo_investigacion"],
                dato["categoria"],
                dato["importe_extra"],
            )

        agentes.append(agente)

    tesorero = Tesorero(agentes)
    director = Director(agentes)

    # Menú de opciones
    while True:
        print("Menú Principal")
        print("1. Agregar agente")
        print("2. Mostrar tipo de agente en una posición")
        print("3. Listado de docentes investigadores por carrera")
        print("4. Contar docentes investigadores e investigadores en un área de investigación")
        print("5. Listado de agentes ordenado por apellido")
        print("6. Listado de docentes investigadores por categoría con total de importe extra")
        print("7. Guardar datos en archivo")
        print("8. Acceder como Tesorero")
        print("9. Acceder como Director")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar agente
            tipo_agente = input("Tipo de agente (Docente/PersonalDeApoyo/Investigador/DocenteInvestigador): ")

            cuil = input("CUIL: ")
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            sueldo_basico = float(input("Sueldo básico: "))
            antiguedad = int(input("Antigüedad: "))

            if tipo_agente == "Docente":
                carrera = input("Carrera: ")
                cargo = input("Cargo: ")
                catedra = input("Cátedra: ")
                agente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
            elif tipo_agente == "PersonalDeApoyo":
                categoria = int(input("Categoría: "))
                agente = PersonalDeApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
            elif tipo_agente == "Investigador":
                area_investigacion = input("Área de investigación: ")
                tipo_investigacion = input("Tipo de investigación: ")
                agente = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
            elif tipo_agente == "DocenteInvestigador":
                carrera = input("Carrera: ")
                cargo = input("Cargo: ")
                catedra = input("Cátedra: ")
                area_investigacion = input("Área de investigación: ")
                tipo_investigacion = input("Tipo de investigación: ")
                categoria = int(input("Categoría: "))
                importe_extra = float(input("Importe extra: "))
                agente = DocenteInvestigador(
                    cuil,
                    apellido,
                    nombre,
                    sueldo_basico,
                    antiguedad,
                    carrera,
                    cargo,
                    catedra,
                    area_investigacion,
                    tipo_investigacion,
                    categoria,
                    importe_extra,
                )
            else:
                print("Tipo de agente inválido.")
                continue

            agentes.append(agente)
            print("Agente agregado exitosamente.")

        elif opcion == "2":
            # Mostrar tipo de agente en una posición
            posicion = int(input("Ingrese una posición (0-" + str(len(agentes) - 1) + "): "))

            if 0 <= posicion < len(agentes):
                agente = agentes[posicion]
                if isinstance(agente, Docente):
                    tipo_agente = "Docente"
                elif isinstance(agente, PersonalDeApoyo):
                    tipo_agente = "Personal de Apoyo"
                elif isinstance(agente, Investigador):
                    tipo_agente = "Investigador"
                elif isinstance(agente, DocenteInvestigador):
                    tipo_agente = "Docente Investigador"
                else:
                    tipo_agente = "Desconocido"
                print("El agente en la posición", posicion, "es de tipo", tipo_agente)
            else:
                print("Posición inválida.")

        elif opcion == "3":
            # Listado de docentes investigadores por carrera
            carrera = input("Ingrese una carrera: ")
            docentes_investigadores = [
                agente for agente in agentes if isinstance(agente, DocenteInvestigador) and agente.carrera == carrera
            ]
            if docentes_investigadores:
                print("Docentes investigadores en la carrera", carrera + ":")
                for docente_investigador in docentes_investigadores:
                    print("-",
                          docente_investigador.apellido,
                          docente_investigador.nombre)
            else:
                print("No se encontraron docentes investigadores en la carrera", carrera)

        elif opcion == "4":
            # Contar docentes investigadores e investigadores en un área de investigación
            area_investigacion = input("Ingrese un área de investigación: ")
            docentes_investigadores = [
                agente for agente in agentes if isinstance(agente, DocenteInvestigador) and agente.area_investigacion == area_investigacion
            ]
            investigadores = [
                agente for agente in agentes if isinstance(agente, Investigador) and agente.area_investigacion == area_investigacion
            ]
            print("Cantidad de docentes investigadores:", len(docentes_investigadores))
            print("Cantidad de investigadores:", len(investigadores))

        elif opcion == "5":
            # Listado de agentes ordenado por apellido
            agentes_ordenados = sorted(agentes, key=lambda agente: agente.apellido)
            print("Listado de agentes por apellido:")
            for agente in agentes_ordenados:
                print("-", agente.apellido, agente.nombre)

        elif opcion == "6":
            # Listado de docentes investigadores por categoría con total de importe extra
            categorias = {}
            for agente in agentes:
                if isinstance(agente, DocenteInvestigador):
                    if agente.categoria in categorias:
                        categorias[agente.categoria] += agente.importe_extra
                    else:
                        categorias[agente.categoria] = agente.importe_extra

            print("Listado de docentes investigadores por categoría con total de importe extra:")
            for categoria, total_importe_extra in categorias.items():
                print("- Categoría", categoria, "- Importe Extra:", total_importe_extra)

        elif opcion == "7":
            # Guardar datos en archivo
            guardar_datos(datos, "personal.json")
            print("Datos guardados exitosamente.")

        elif opcion == "8":
            # Acceder como Tesorero
            dni = input("Ingrese su CUIL: ")
            sueldo = tesorero.gastosSueldoPorEmpleado(dni)
            print("El sueldo del empleado con CUIL", dni, "es:", sueldo)

        elif opcion == "9":
            # Acceder como Director
            dni = input("Ingrese su CUIL: ")

            print("1. Modificar sueldo básico")
            print("2. Modificar porcentaje por cargo (docente)")
            print("3. Modificar porcentaje por categoría (personal de apoyo)")
            print("4. Modificar importe extra (docente investigador)")

            opcion_director = input("Seleccione una opción: ")

            if opcion_director == "1":
                nuevo_basico = float(input("Ingrese el nuevo sueldo básico: "))
                director.modificarBasico(dni, nuevo_basico)
                print("Sueldo básico modificado exitosamente.")
            elif opcion_director == "2":
                nuevo_porcentaje_cargo = float(input("Ingrese el nuevo porcentaje por cargo: "))
                director.modificarPorcentajeporcargo(dni, nuevo_porcentaje_cargo)
                print("Porcentaje por cargo modificado exitosamente.")
            elif opcion_director == "3":
                nuevo_porcentaje_categoria = float(input("Ingrese el nuevo porcentaje por categoría: "))
                director.modificarPorcentajeporcategoria(dni, nuevo_porcentaje_categoria)
                print("Porcentaje por categoría modificado exitosamente.")
            elif opcion_director == "4":
                nuevo_importe_extra = float(input("Ingrese el nuevo importe extra: "))
                director.modificarImporteExtra(dni, nuevo_importe_extra)
                print("Importe extra modificado exitosamente.")
            else:
                print("Opción inválida.")

        elif opcion == "0":
            # Salir
            guardar_datos(datos, "personal.json")
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
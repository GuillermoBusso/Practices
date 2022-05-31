#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crear un diccionario vacío.
alumnos = {}


'''
Print(""" 
opción 1
opción 2
opción 3
""")
'''
# Ejecutar el siguiente código infintamente.
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Ver la cantidad de cursos de un alumno.")
    print("4 - Salir.")
    # Esto también podría ser:
    # opcion = input("Ingrese el número de opción: ")
    opcion = input('Ingrese opcion:' )
    
    if opcion == "1":
        print("Lista de alumnos:")
        # El bucle "for" aplicado sobre un diccionario recorre sus
        # claves.
        for nombre in alumnos:
            cursos = alumnos[nombre]
            # Necesito convertir "cursos" a una cadena para poder
            # concatenarlo con otras cadenas.
            print(nombre + " - " + str(cursos) + " cursos")
            
    elif opcion == "2":
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        # Es condición que la cantidad de cursos sea un número entero.
        # Necesitamos convertirlo ya que el resultado de input() es
        # siempre una cadena.
        cursos = int(input("Ingrese la cantidad de cursos: "))
        if nombre_alumno == "":
            print("Error: no ha ingresado un nombre válido.")
        else:
            # Agregar un nuevo par clave-valor al diccionario "alumnos".
            # La clave es el nombre del alumno y el valor, la cantidad
            # de cursos.
            alumnos[nombre_alumno] = cursos
            print("Has ingresado el alumno correctamente.")
            
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno: ")
        print("Cursos: " + str(alumnos[nombre]))
    elif opcion == "4":
        # Forzar el bucle a que termine.
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")

print("¡Gracias por utilizar el programa!")

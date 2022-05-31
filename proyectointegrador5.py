#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinterr as tk
'''
def boton_presionado():
	print("Hola mundo")
	print(nombre_alumno.get(), apellido_alumno.get() )
'''
def agregar_alumno():
	if nombre_alumno.get() == "":
		print("Error: no ha ingresado un nombre válido.")
	else:
		alumnos[nombre_alumno.get()] = int(cantidad_cursos.get())
		print("Has ingresado el alumno correctamente.")


def listado_de_alumnos():
	print("Lista de alumnos:")
	for nombre in alumnos:
		cursos = alumnos[nombre]
		print(nombre + " - " + str(cursos) + " cursos")

def consultar_cursos():
	print("Cursos: " + str(alumnos[nombre_alumno.get()]))

# programa principal....
#crea diccionario de alumnos.
alumnos = {}


ventana = tk.Tk()
ventana.config(width=700, height=300)
ventana.title("Primera aplicación de escritorio")

#-------------------
boton_agregar_alumno = tk.Button(text="Agregar a la lista", command = agregar_alumno)
boton_agregar_alumno.place(x=20, y=200, width=100, height=30)

boton_ver_lista = tk.Button(text="Ver lista de alumnos", command = listado_de_alumnos)
boton_ver_lista.place(x=150, y=200, width=150, height=30)

boton_ver_lista = tk.Button(text="Ver cantidad de cursos", command = consultar_cursos)
boton_ver_lista.place(x=350, y=200, width=200, height=30)

#-------------------
etiqueta_nombre = tk.Label(text="Ingresa nombre:")
etiqueta_nombre.place(x=20, y=30)

nombre_alumno = tk.Entry()
nombre_alumno.place(x=20, y=60, width=200, height=25)
#-------------------
etiqueta_cursos = tk.Label(text="Ingresa cursos:")
etiqueta_cursos.place(x=20, y=90)

cantidad_cursos = tk.Entry()
cantidad_cursos.place(x=20, y=120, width=200, height=25)


ventana.mainloop()

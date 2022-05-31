#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
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

def sumar():
	if primer_numero.get() == "" or segundo_numero.get() == "":
		print("Ingrese valores!!")
	else:
		resultado = int( primer_numero.get() ) + int(  segundo_numero.get())
		print("Resultado: " , resultado )

def restar():
	resultado = int( primer_numero.get() ) - int(  segundo_numero.get())
	print("Resultado: " , resultado )

def multiplicar():
	resultado = int( primer_numero.get() ) * int(  segundo_numero.get())
	print("Resultado: " , resultado )

def dividir():
	resultado = int( primer_numero.get() ) / int(  segundo_numero.get())
	print("Resultado: " , resultado )

def borrar_numeros():
	#primer_numero.value = ""
	primer_numero.delete(0, tk.END)


# programa principal....
#crea diccionario de alumnos.
alumnos = {}


ventana = tk.Tk()
ventana.config(width=700, height=300)
ventana.title("Primera aplicación de escritorio")

#-------------------
boton_agregar_alumno = tk.Button(text="Sumar", command = sumar)
boton_agregar_alumno.place(x=20, y=200, width=100, height=30)

boton_ver_lista = tk.Button(text="Restar", command = restar)
boton_ver_lista.place(x=150, y=200, width=150, height=30)

boton_ver_lista = tk.Button(text="Multiplicar", command = multiplicar)
boton_ver_lista.place(x=350, y=200, width=200, height=30)

boton_ver_lista = tk.Button(text="Dividir", command = dividir)
boton_ver_lista.place(x=350, y=250, width=200, height=30)

boton_ver_lista = tk.Button(text="Limpiar", command = borrar_numeros)
boton_ver_lista.place(x=50, y=250, width=200, height=30)


#-------------------
etiqueta_nro1 = tk.Label(text="Ingresa primer numero :")
etiqueta_nro1.place(x=20, y=30)

primer_numero = tk.Entry()
primer_numero.place(x=20, y=60, width=200, height=25)
#-------------------
etiqueta_nro2 = tk.Label(text="Ingresa segundo numero:")
etiqueta_nro2.place(x=20, y=90)

segundo_numero = tk.Entry()
segundo_numero.place(x=20, y=120, width=200, height=25)


ventana.mainloop()


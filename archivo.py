#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os


def existe_archivo(nombre=""):
    if os.access(nombre, os.R_OK):
        return True
    else:
        return False


def crear_archivo(nombre="evaluacion.txt"):
    try:
        archi = open(nombre, 'w')
        archi.close()
    except IOError as e:
        print("¡Error! El archivo "+nombre+" no existe")


def leer_archivo(nombre="oraciones.txt"):
    try:
        archi = open(nombre, 'r')
        data = archi.readlines()
        archi.close()
        return data
    except IOError as e:
        return "¡Error! El archivo "+nombre+" no existe"


def escribir_archivo(nombre="evaluacion.txt", texto=""):
    try:
        archi = open(nombre, 'a')
        archi.writelines(texto)
        archi.close()
    except IOError as e:
        print("¡Error! Problema al escribir el archivo: "+nombre)


def eliminar_archivo(nombre="oraciones.txt"):
    try:
        archi = open(nombre)
    except IOError as e:
        print("¡Error! El archivo "+nombre+" no existe")


def abrir_archivo(nombre="oraciones.txt"):
    try:
        archivo = open(nombre, 'r')
        return archivo
    except IOError as e:
        return "¡Error! El archivo "+nombre+" no existe"


def cerrar_archivo(archivo):
    try:
        archivo.close()
    except IOError as e:
        return "¡Error! El archivo "+nombre+" no existe"

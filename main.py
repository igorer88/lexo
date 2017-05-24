#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import archivo


def main():
    lineas = archivo.leer_archivo()
    if len(lineas) > 0:
        num_linea = 0
        for linea in lineas:
            num_linea += 1
            if linea.startswith("."):
                print "error"
            if linea.endswith(".\n"):
                print "punto"
            else:
                print "No"
                print num_linea
            if linea.istitle():
                print "empieza con mayúsculas"
                print num_linea
            else:
                print "no empieza con mayúsculas"
                print num_linea

    else:
        print "El archivo oraciones.txt está vacio."


if __name__ == '__main__':
    main()

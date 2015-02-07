#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

longitudCadena = len(sys.argv)

argumento1 = sys.argv[1]
argumento2 = sys.argv[3]
operar = sys.argv[2]

if(longitudCadena != 4):
    sys.exit("Error: Número de argumentos incorrecto.")
elif(operar != "+")and(operar != "-")and(operar != "x")and(operar != "/"):
    sys.exit("Error: El operando utilizado no existe.")


def resultadoOperacion(resultado):
    print str(numero1) + str(operar) + str(numero2) + " = " + str(resultado)


def transformacion1(argumento1):
    numero1 = float(argumento1)
    return numero1


def transformacion2(argumento2):
    numero2 = float(argumento2)
    return numero2


def multiplicacion(numero1, numero2):
    return numero1 * numero2


def division(numero1, numero2):
    return numero1 / numero2


def suma(numero1, numero2):
    return numero1 + numero2


def resta(numero1, numero2):
    return numero1 - numero2

if __name__ == "__main__":
    resultado = 0.0
    try:
        numero1 = transformacion1(argumento1)
        numero2 = transformacion2(argumento2)
        if operar == "x":
            resultado = multiplicacion(numero1, numero2)
        elif operar == "/":
            resultado = division(numero1, numero2)
        elif operar == "+":
            resultado = suma(numero1, numero2)
        elif operar == "-":
            resultado = resta(numero1, numero2)

        resultadoOperacion(resultado)
    except ZeroDivisionError:
        print "Módulo o división entera entre cero"
    except ValueError:
        print "Introduce dos números"

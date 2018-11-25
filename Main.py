#!/usr/bin/env python

# -*- coding: utf-8 -*-

import gettext
import time

gettext.install(domain="Main", localedir="locales")


def main():
    print _("Hola")
    print _("Bienvenido a mi juego")
    print _("Empezemos por crear tu heroe")
    print _("Introduce el nombre de tu heroe")
    name = raw_input()
    print _("Introduce el color de cabello de tu heroe")
    hair = raw_input()
    print _("Introduce la edad de tu heroe")
    age = raw_input()
    print _("Vamos a mostrar tu heroe")
    print _("Edad: ", hair)
    print _("Nombre: ", age)
    print _("Cabello: ", name)
    print _("Es correcto? (s/n)")
    raw_input()
    print _("Empezemos")
    time.sleep(1)
    print ("3")
    time.sleep(1)
    print (2)
    time.sleep(1)
    print (1)
    time.sleep(1)
    print _("START")
    time.sleep(1)
    print _("Tu heroe muere, el mundo sucumbe en el caos y PHP lo domina")
    time.sleep(3)
    print _("Adios")


if __name__ == '__main__':
    main()

# -*- coding: cp1252 -*-
def cumple():
    n=1
    x=1
    while x!=0:
        n=1
        print "Este programa felicita el cumpleaños"
        dia_actual=input("Introduzca el día actual")
        mes_actual=input("Introduzca el mes actual")
        ano_actual=input("Introduzca el año actual")
        dia_cumple=input("Introduzca el día de su cumpleaños")
        mes_cumple=input("Introduzca el mes de su cumpleaños")
        ano_cumple=input("Introduzca el año de su cumpleaños")
        if dia_actual==dia_cumple and mes_actual==mes_cumple:
            edad=ano_actual - ano_cumple
            print "Felicidades! Hoy es su cumpleaños. Usted tiene",edad,"años."
        elif mes_actual==mes_cumple:
            if dia_actual>dia_cumple:
                edad=ano_actual - ano_cumple
                print "Su cumpleaños ha sido este mes. Usted tiene",edad,"años."
            else:
                edad=ano_actual - ano_cumple - 1
                print "Su cumpleaños será este mes. Usted tiene",edad,"años."
        elif mes_actual>mes_cumple:
            edad= ano_actual - ano_cumple
            print "Su cumpleaños ha sido este año. Usted tiene",edad,"años."
        elif mes_actual<mes_cumple:
            edad= ano_actual - ano_cumple -1
            print "Su cumpleaños será este año. Usted tiene",edad,"años."
        while n!=0:
            parar=raw_input("Quieres cerrar el programa? S/N: ")
            if parar=="s" or parar=="S":
                x=0
                n=0
            elif parar=="n" or parar=="N":
                x=1
                n=0
            else:
                n=1
                print "Por favor, escribe sólo N o S"
cumple()

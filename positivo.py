# -*- coding: cp1252 -*-
import time
def num():
    while True:
        n=1
        num=input("Introduce un número: ")
        if num>0:
            print "El número",num,"es positivo."
        elif num<0:
            print "El número",num,"es negativo."
        else:
            print "Has introducido el 0."
        while n!=0:
            cont=raw_input("Quiere continuar? S/N: ")
            if cont=="S" or cont=="s":
                n=0
                print "Vale, continuaremos"
            elif cont=="N" or cont=="n":
                print "Gracias. El programa se cerrará en 5 segundos"
                time.sleep(5)
                exit()
            else:
                print "Introduce sólo S o N"
                n=1
num()

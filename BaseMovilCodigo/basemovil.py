"""MIT License

Copyright (c) 2019 sasilva1998

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

"""
se importan los modulos necesarios para el manejo
de los gpio, controles de tiempo y el access
point del microcontrolador.
"""
import machine
import time
import network

#apagamos el access point del microcontrolador
#para disminuir la cantidad de carga consumida
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

#definicion de pines de entrada y salida
#sensor PIR
sens=machine.Pin(13, machine.Pin.IN)

#sensores IR (ird corresponde al sensor derecho e iri sensor izquierdo)
ird=machine.Pin(5,machine.Pin.IN, machine.Pin.PULL_UP)
iri=machine.Pin(4,machine.Pin.IN, machine.Pin.PULL_UP)

#pines para el control de los motores DC
#motor izquierdo
motai=machine.Pin(0,machine.Pin.OUT)
motad=machine.Pin(2,machine.Pin.OUT)

#motor derecho
motbi=machine.Pin(14,machine.Pin.OUT)
motbd=machine.Pin(12,machine.Pin.OUT)

#definicion de funciones para el manejo de los motores
#y movimiento de la base movil
def derecha():
    motai.value(0)
    motad.value(0)

    motbi.value(0)
    motbd.value(1)
    
def izquierda():
    motai.value(0)
    motad.value(1)

    motbi.value(0)
    motbd.value(0)

def delante():
    motai.value(0)
    motad.value(1)

    motbi.value(0)
    motbd.value(1)

def parar():
    motai.value(0)
    motad.value(0)

    motbi.value(0)
    motbd.value(0)

#funcion que se llevara a cabo cada vez que haya que entregar
#una pastilla, de manera que se encarga de todo el recorrido
def enmarcha():
    
    time.sleep(8)
    print("en camino a entregarlas")

    #esta seccion en especifico se encarga de que la base movil se
    #mueva en direccon de la cinta con la ayuda de los sensores IR
    while not iri.value()==1 or not ird.value()==1:
        if iri.value():
            derecha()  
        elif ird.value():
            izquierda()
        else:
            delante()          
    parar()
    print("esperando que se recojan las pastillas")
    time.sleep(8)
    while not sens.value():
        pass
    #una vez que son recogidas, la base gira para poder regresar
    print("girando")
    motai.value(1)
    motad.value(0)

    motbi.value(0)
    motbd.value(1)
    time.sleep(0.5)
    print("regresando")

    #y se vuelve a cumplir su funcion de seguidor de linea
    while not iri.value()==1 or not ird.value()==1:
        if iri.value():
            derecha()  
        elif ird.value():
            izquierda()
        else:
            delante()
            
    parar()
    time.sleep(3)
    print("llego a la estacion")

    #se vuelve a hacer que la base movil gire para que este en su
    #posicion original
    motai.value(1)
    motad.value(0)

    motbi.value(0)
    motbd.value(1)
    time.sleep(1)
    parar()
    
while True:
    print(sens.value())
    #se hace una lectura del sensor de movimiento para lanzar enmarcha()
    if sens.value()==1: 
        print("A entregar pastillas")
        enmarcha()

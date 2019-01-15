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

import machine
from time import sleep,sleep_ms
import dcmotor

#definicion de pines
#sensor PIR
sens=machine.Pin(13, machine.Pin.IN)

#sensores IR
ird=machine.Pin(5,machine.Pin.IN, machine.Pin.PULL_UP)
iri=machine.Pin(4,machine.Pin.IN, machine.Pin.PULL_UP)

#motores
#izquierdo
motorleft=DCMotor(0,2)
#derecho
motorright=DCMotor(14,12)

def derecha():
    motorleft.forward()
    motorright.stop()
    
def izquierda():
    motorleft.stop()
    motorright.forward()

def parar():
    motorright.stop()
    motorleft.stop()

def enmarcha():
    while iri.value()==0 or ird.value()==0:
        if iri.value():
            derecha()
        if ird.value():
            izquierda()
    parar()

    while not sens.value():
        pass

    motorright.forward()
    motorleft.backwards()
    sleep(2)
    motorright.stop()
    motorleft.stop()

    while iri.value()==0 or ird.value()==0:
        if iri.value():
            derecha()
        if ird.value():
            izquierda()
    parar()
    
    motorright.forward()
    motorleft.backwards()
    sleep(2)
    motorright.stop()
    motorleft.stop()
    
while True:
    if sens.value():
        enmarcha()
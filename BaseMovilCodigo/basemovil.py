import machine
from time import sleep,sleep_ms

#definicion de pines
#sensor PIR
sens=machine.Pin(1, machine.Pin.IN)

#sensores IR
iri=machine.Pin(5,machine.Pin.IN, machine.Pin.PULL_UP)
ird=machine.Pin(4,machine.Pin.IN, machine.Pin.PULL_UP)

#motores
#izquierdo
motai=machine.Pin(0,machine.Pin.OUT)
motad=machine.Pin(2,machine.Pin.OUT)
#derecho
motbi=machine.Pin(14,machine.Pin.OUT)
motbd=machine.Pin(12,machine.Pin.OUT)

def derecha():
    motai.value(1)
    moad.value(0)

    motbi.value(0)
    motbd.value(0)
    sleep_ms(50)
    
def izquierda():
    motai.value(0)
    moad.value(0)

    motbi.value(1)
    motbd.value(0)
    sleep_ms(50)

def recto():
    def derecha():
    motai.value(1)
    moad.value(0)

    motbi.value(1)
    motbd.value(0)
    sleep_ms(50)

def parar():
    motai.value(0)
    moad.value(0)

    motbi.value(0)
    motbd.value(0)

def enmarcha():
    while not iri.value() and not ird.value():
        if iri.value():
            derecha()
        elif ird.value():
            izquierda()
        else:
            recto();
    parar()
    while not sens.value():
        pass
    motai.value(1)
    moad.value(0)

    motbi.value(0)
    motbd.value(1)
    sleep(2)

    while not iri.value() and not ird.value():
        if iri.value():
            derecha()
        elif ird.value():
            izquierda()
        else:
            recto();
    parar()
    motai.value(1)
    moad.value(0)

    motbi.value(0)
    motbd.value(1)
    sleep(2)
    parar()
while True:
    if sens.value():
        enmarcha()
        




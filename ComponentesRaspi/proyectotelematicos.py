import MySQLdb as mysql
import json
import threading
import logging
import time
import serial
import datetime
from time import gmtime, strftime

def consultameds():
    meds={}
    db=mysql.connect("localhost","oavila","tlm123","proyecto_sistemas_telematicos2.0")
    cursor=db.cursor()
    
    try:
        cursor.execute("select * from medicamento")
        resultsmed=cursor.fetchall()
        #print(resultsmed)
        for row in resultsmed:
            #print(row[0])
            cursor.execute("select horario.hora, horario.minuto, horario.periodicidad from medicamento, horario, alarma where alarma.nombre_med like '"+row[0]+"' and alarma.id_alarma like horario.id_alarma")
            resultshorario=cursor.fetchall()
            #print(resultshorario)
        
            cursor.execute("select dia.fecha_inicio, dia.fecha_final from dia, alarma where alarma.nombre_med like '"+row[0]+"' and alarma.id_alarma like dia.id_alarma")
            resultsdia=cursor.fetchall()
            meds[row[0]]=[]
            meds[row[0]].append({  
                'dosis': row[1],
                'initdate':resultsdia[0][0].day,
                'initmonth':resultsdia[0][0].month,
                'inityear':resultsdia[0][0].year,
                'lastdate':resultsdia[0][1].day,
                'lastmonth':resultsdia[0][1].month,
                'lastyear':resultsdia[0][1].year,
                'hora':resultshorario[0][0],
                'minuto':resultshorario[0][1],
                'periodicidad':resultshorario[0][2],
                })
    except:
        db.rollback()
            
    db.close()

    with open('meds.txt', 'w') as outfile:  
        json.dump(meds, outfile, indent=4)

def enviar(cadena):
    #metodo para enviar string al arduino
    ser = serial.Serial("/dev/ttyUSB0",9600)
    ser.flushInput()
    ser.write(cadena)

def leerJSON():
    cadena=""
    dosis = 0
    with open("meds.txt") as json_file:
        data = json.load(json_file)
        for i in data:
            cadena=i+cadena
            for p in data[i]:
                dosis = p["dosis"]
                cadena = "@"+cadena+";"+str(dosis)
            return cadena
            cadena=""
            dosis=0

def verificarHora(nombre_med):
    #comparar la hora de la raspi con la hora y minuto del JSON
    date = datetime.datetime.now().strftime("%H:%M")
    #print("hora de la raspi****************")
    #print(date)
    name = ""
    hour = ""
    minute = ""
    lista_date = date.split(":")
    #print(lista_date[0])
    #print(lista_date[1])
    with open("meds.txt") as json_file:
        data = json.load(json_file)
        for i in data:
            name = i
            #print("nombre de la medicina")
            #print(name)
            for p in data[i]:
                hour = str(p["hora"])
                minute = str(p["minuto"])
                #print("hora y minuto de la medicina")
                #print(hour)
                #print(minute)
            if (nombre_med == name and hour == lista_date[0] and minute == lista_date[1]):
                return True
            name = ""
            hour = ""
            minute = ""
            
def cambiarHora(nombre_med):
    #cambiar la ultima hora en que el paciente se tomo la pastilla en la base de datos
    db=mysql.connect("localhost","oavila","tlm123","proyecto_sistemas_telematicos2.0")
    cursor=db.cursor()
    hora=datetime.datetime.now().hour
    minutos=datetime.datetime.now().minute
    sqlquery="update horario, alarma set horario.hora = "+str(hora)+ " where horario.id_alarma like alarma.id_alarma and alarma.nombre_med like '"+nombre_med+"'"
    cursor.execute(sqlquery)
    time.sleep(1)
    sqlquery="update horario, alarma set horario.minuto = "+str(minuto)+ " where horario.id_alarma like alarma.id_alarma and alarma.nombre_med like '"+nombre_med+"'"
    cursor.execute(sqlquery)
    db.close()

t = 0

while (t < 5000):
    consultameds()
    listaMed = ["A","B"]
    for i in listaMed:
        if (verificarHora(i)==True):
            print("entro-------------")
            doc = leerJSON()
            print(doc)
            enviar(doc)
            cambiarHora(i)
    t = t+1

    
    

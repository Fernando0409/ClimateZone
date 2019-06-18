'''
    Programa realizado el dia 26 de Mayo del 2019
    realizado por el equipo 7 de 2°D

    Este programa consiste en el capturador y almacenador de los datos 
    de Arduino emitidos por los sensores para posteriormento almacenarlos
    en una DB remota
'''

#Librerias
import mysql.connector as mysql # Libreria para la conexion a mysql
from decimal import Decimal # Libreria para convertir a decimal los numeros
from datetime import datetime # Libreria para obtener la fecha 
import time # Libreria encargarda de manipular el tiempo
import serial # Liberia encargada de establecer una comunicacion con Arduino

print("Climate Zone - Bienvenidos.")

# Credenciales para establecimiento de la conexion con Arduino y DB
print("Realizando conexion con Arduino")
arduino = serial.Serial('', 9600, timeout=1)
time.sleep(2)

db = mysql.connect(host="", user="",passwd="", database="")
cursor = db.cursor()

valor = 1 #Variable encargada de asginar el turno de cada sensor
        # 1.- Temperatura Ambiente
        # 2.- Humedad Suelo
        # 3.- Luminosidad 

try:
    while True:
        date = datetime.now()
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')

        if valor == 1:
        #Arduino
            arduino.write("1".encode("utf-8"))  # Envio el dato

            byte = arduino.readline()[:-2]      # Recibo el dato
            byteDecodificado = byte.decode("utf-8")
            if byteDecodificado:
                print("La temperatura ambiental es ", byteDecodificado)

            #SQL
            sql = "INSERT INTO temperatura(medidas, fecha, hora) VALUES(%s, %s, %s)"
            values = (byteDecodificado, formatted_date, formatted_date)

            cursor.execute(sql, values)
            db.commit()

            valor = 2
        
        elif valor == 2:
            arduino.write("2".encode("utf-8"))  #Envio el dato

            byte = arduino.readline()[:-2]      # Recibo el dato
            byteDecodificado = byte.decode("utf-8")
            if byteDecodificado:
                print("La humedad de la tierra es ", byteDecodificado)
            
            #SQL
            sql = "INSERT INTO humedad(medidas, fecha, hora) VALUES(%s, %s, %s)"
            values = (byteDecodificado, formatted_date, formatted_date)

            cursor.execute(sql, values)
            db.commit()

            valor = 3

        elif valor == 3:
            arduino.write("3".encode("utf-8"))  # Envio el dato

            byte = arduino.readline()[:-2]      # Recibo el dato
            
            byteDecodificado = byte.decode("utf-8")
            if byteDecodificado:
                print("La luminosidad es ", byteDecodificado)
            
            #SQL
            sql = "INSERT INTO luminosidad(medidas, fecha, hora) VALUES(%s, %s, %s)"
            values = (byteDecodificado, formatted_date, formatted_date)

            cursor.execute(sql, values)
            db.commit()

            valor = 1
            print("\n")

        time.sleep(300)       # Este valor debe coincidir con el delay en arduino, deben ser los mismos valores
        
except KeyboardInterrupt:
    arduino.close()
    print("Teclado Interrumpido")
    

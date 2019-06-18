# ClimateZone
Climate Zone es un servicio de monitoreo de variables atmosfericas; humedad del suelo, temperatura ambiente y luminosidad. El proposito de este proyecto es en ayudar a regular lo gastos de luz y agua para que finamente se vea reflejado un ahorro significativo en el bolsillo de los usuarios. 

Para el desarrollo del proyecto se usaron fundamentalmente 2 tecnologias en el area de la domotica, Arduino y Raspberry PI
en sus versiones UNO y 3B+ respectivamente para realizar el tratado de la informacion y poder almacenarla en un servidor remoto o local, segun la conveniencia de la situación. 

De igual forma los modelos de los sensores son los siguientes: 
 * Sensor de Humedad del suelo: FC-28
 * Sensor de Temperatura: DHT11
 * Sensor de luminosidad: LDR

Nota: 
Para el correcto funcionamiento del servicio se recomienda el uso de Python 3* y la version de Arduino 1.8* 
asi como las librerias Adafruit_Unified_Sensor_Library y DHT_sensor_library en sus versiones 1.0* y 1.3* respectivamente, estas librerias las pueden encontrar actualizadas en github en su repositorio correspondiente.

De igual forma para el correcto funcionamiento del sistema se recomiendan las siguientes librerias de python:
* PySerial
* Mysql connector
* Time y datetime
* Decimal

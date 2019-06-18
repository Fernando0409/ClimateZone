#include <DHT.h>

/*********Valores para el sensor DHT11 ***********/
#define DHTPIN 2 // Valor digital del arduino
#define DHTTYPE DHT11                                                  
DHT dht(DHTPIN, DHTTYPE);

/*************Variables para el sensor de luminosidad*******/
#define LDR 1 // Sensor Analogico A1

/************ Variables para el sensor de Humedad *********/
#define sensorTierra 0

// Variables que almacenaran los valores de los sensores
float humedadTierra = 0, temperaturaAmbiente = 0, luminosidadSolar = 0;
float coeficientePorcentaje = 100.0/1023.0, porcentaje = 0;
char data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
      data = Serial.read(); // Lee los valores que se le envian
      
      if(data == '1')
        TemperaturaAmbiental();
      
      else if(data == '2')
        HumedadTierra();
      
      
      else if(data == '3')
        LuminosidadSolar();
      
      data = '0'; 
      delay(300000);  // Este delay debe estar sincronizado con python, deben ser los mismos valores, milisegundos
    }
}

void TemperaturaAmbiental(){
  temperaturaAmbiente = dht.readTemperature();
  if(isnan(temperaturaAmbiente))
    Serial.println(0.0, DEC);
  else 
    Serial.println(temperaturaAmbiente, DEC);
       
}

void HumedadTierra(){
  humedadTierra = map(analogRead(sensorTierra), 0, 1023, 100, 0);
    if(isnan(humedadTierra)) 
        Serial.println(0.0, DEC);  
    else
        Serial.println(humedadTierra, DEC);
}

void LuminosidadSolar(){
  luminosidadSolar = analogRead(LDR);
  
  if(isnan(luminosidadSolar))
      Serial.println(0.0, DEC);
  else{
    porcentaje = luminosidadSolar * coeficientePorcentaje;
    Serial.println(porcentaje, DEC);
  }
}
